# EKS + Prometheus Monitoring Commands

## 1️⃣ Create EKS Cluster
eksctl create cluster \
  --name eks-prometheus-demo \
  --region us-east-1 \
  --nodegroup-name workers \
  --node-type t2.micro \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3

## 2️⃣ Connect kubectl
aws eks update-kubeconfig --region us-east-1 --name eks-prometheus-demo
kubectl get nodes

## 3️⃣ Create New Node Group (t3.small)
eksctl create nodegroup \
  --cluster eks-prometheus-demo \
  --region us-east-1 \
  --name workers-small \
  --node-type t3.small \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3

kubectl cordon <old-node1> <old-node2>
kubectl drain <old-node1> <old-node2> --ignore-daemonsets --force

eksctl delete nodegroup \
  --cluster eks-prometheus-demo \
  --region us-east-1 \
  --name workers

## 4️⃣ Install Prometheus + Grafana
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring

## 5️⃣ Access UIs
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090 -n monitoring
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
