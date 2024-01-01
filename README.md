# Sample Python FastAPI Docker Microservice

This repository contains a sample Python FastAPI microservice that can be containerized using Docker and deployed to a Kubernetes cluster. 
The deployment process is automated using GitHub Actions workflows.

## Prerequisites

Make sure you have the following tools installed before proceeding:

- [Docker](https://www.docker.com/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [GitHub Actions](https://github.com/features/actions)

## Getting Started

1. Clone this repository:

    ```bash
    git clone git@github.com:mustafaguc/python-kube-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-kube-app
    ```

3. Build the Docker image:

    ```bash
    docker build -t my-python-kube-app .
    ```

4. Run the Docker container locally:

    ```bash
    docker run -p 80:80 my-python-kube-app
    ```

5. Open your web browser and navigate to [http://localhost](http://localhost) to confirm that the microservice is running.

6. Make changes and push the code. Github Action will build app and push a docker image to your ghcr.io docker registry

## Docker Image

The Docker image for this microservice is hosted on ghcr.io : [my-python-kube-app](https://ghcr.io/{your-username}/{your-app-name}:latest)
```
ghcr.io/{username}/{app-name}:latest
```

## Github Registry and Secrets on Kubernetes Cluster
- Add Github Docker Registry (ghcr.io) and create secrets on your Kubernetes Cluster
- Configure Kubernetes context value in ```.github/workflows/build-deploy.yml``` according to your Kubernetes cluster context

## Kubernetes Deployment 
The Kubernetes deployment, service and ingress manifests are located in the `kubernetes` directory. Modify the `project.yaml` file with your specific configurations.

### Deploy to Kubernetes Cluster
Whole process is performed by Github Action flow. 
No need to deploy the microservice manually. 
Add a ```KUBECONFIG``` repository secret that stores your kubernetes cluster configuration from [repository-secret](https://github.com/{your-username}/{app-name}/settings/secrets/actions/new) 
