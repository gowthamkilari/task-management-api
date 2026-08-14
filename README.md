# Task Management API — Kubernetes & CI/CD

A small FastAPI REST API created to practice containerization, Kubernetes deployment, OpenShift deployment concepts, Linux troubleshooting, and GitHub Actions CI/CD.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Test

```bash
pytest
```

## Docker

Replace `YOUR_DOCKERHUB_USERNAME` with your Docker Hub username.

```bash
docker build -t YOUR_DOCKERHUB_USERNAME/task-management-api:latest .
docker run -p 8000:8000 YOUR_DOCKERHUB_USERNAME/task-management-api:latest
```

## Kubernetes

Update `k8s/deployment.yaml` with your Docker Hub image, then:

```bash
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

kubectl get pods
kubectl get services
kubectl logs deployment/task-api
kubectl describe deployment task-api
```

For local access:

```bash
kubectl port-forward service/task-api-service 8000:80
```

Then open http://127.0.0.1:8000/docs

## OpenShift

The Kubernetes manifests can be used as a starting point on an OpenShift cluster:

```bash
oc login <OPENSHIFT_SERVER>
oc new-project task-api
oc apply -f k8s/configmap.yaml
oc apply -f k8s/deployment.yaml
oc apply -f k8s/service.yaml
oc get pods
oc logs deployment/task-api
```

For an externally reachable application, create an OpenShift Route according to the cluster's routing configuration.

## CI/CD

The GitHub Actions workflow:
1. Checks out the repository.
2. Installs Python dependencies.
3. Runs pytest.
4. Builds the Docker image.
5. Pushes the image to Docker Hub on pushes to `main`.

Create these GitHub repository secrets before using the Docker job:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## Resume focus

After you have actually deployed and tested the project, you can describe it as:

- Built a FastAPI REST API and containerized it using Docker.
- Created Kubernetes Deployment, Service, and ConfigMap manifests.
- Deployed and troubleshot the application using Kubernetes Pods, Services, logs, and health probes.
- Built a GitHub Actions CI/CD workflow to run automated tests and build/publish Docker images.
- Practiced deployment and troubleshooting using OpenShift CLI (`oc`).
