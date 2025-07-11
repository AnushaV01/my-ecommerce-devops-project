# Terraform AWS EKS + VPC Infrastructure

This Terraform configuration sets up a complete AWS infrastructure using **official Terraform modules**, including:
- A custom **VPC** with public and private subnets across two AZs
- A production-ready **EKS cluster** deployed in **private subnets**
- A **NAT Gateway** for private subnet internet access

---

## 🚀 What It Deploys

### 1. VPC
- CIDR block: `10.0.0.0/16`
- 2 Availability Zones: `us-east-1a`, `us-east-1b`
- 2 Public subnets
- 2 Private subnets
- 1 NAT Gateway (for private subnets)
- Tags for Terraform and environment

### 2. EKS Cluster
- Cluster name: `my-eks-cluster` (via variable)
- Kubernetes version: `1.29`
- Worker nodes:
  - Managed node group
  - 2 desired nodes (t3.medium)
  - Running in **private subnets**

---

## 📦 Modules Used

| Module                          | Source                               | Version   |
|---------------------------------|--------------------------------------|-----------|
| VPC                             | terraform-aws-modules/vpc/aws        | 4.0.2     |
| EKS                             | terraform-aws-modules/eks/aws        | 20.8.4    |

> ⚠️ Note: VPC module is pinned to `4.0.2` to maintain compatibility with AWS provider `< 6.0.0`, as EKS module is not yet compatible with AWS provider v6+.

---

## 📋 Requirements

- Terraform >= 1.3.2
- AWS Provider `~> 5.95`

---

## 📂 File Structure

terraform/
├── main.tf # Root module calling VPC and EKS
├── variables.tf # Input variables (e.g. cluster_name)
├── provider.tf # AWS provider configuration
├── outputs.tf # Useful outputs like vpc_id, cluster_name


---

## 🛡️ Security & Networking Notes

- **EKS nodes are in private subnets**, ensuring they don’t have public IPs
- A **NAT Gateway** allows outbound internet access (e.g., for pulling container images)
- Security groups and IAM roles are managed by the EKS module
- You can customize node group security group rules using `node_security_group_additional_rules`

---

## 🧪 How to Use

1. Initialize the working directory:
   ```bash
   terraform init
```
2. Review the plan:

```bash
terraform plan
```
3. Apply the configuration:
```bash
terraform apply
```
4. Update kubeconfig after creation:
```bash
aws eks update-kubeconfig --region us-east-1 --name my-eks-cluster
```

📤 Outputs
After successful apply, Terraform will output:
vpc_id
private_subnets
cluster_name

You can customize more outputs in outputs.tf as needed.

🧠 Tips
Don't forget to set up proper IAM roles and permissions for your Terraform user.
Use terraform destroy to clean up the infrastructure.

📚 References
terraform-aws-modules/vpc/aws
terraform-aws-modules/eks/aws
