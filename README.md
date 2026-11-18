# DevOps Training – Automated CI/CD Pipeline

A hands-on DevOps project demonstrating how to build, publish, and automatically deploy a containerized Flask application using GitHub Actions, Docker, Docker Hub, Tailscale, and SSH.

## Project Overview

This project implements an automated CI/CD pipeline that deploys a Flask application to an Ubuntu server whenever new code is pushed to the `main` branch.

The pipeline automatically:

1. Retrieves the latest source code from GitHub.
2. Installs Python dependencies.
3. Validates Python code.
4. Builds a Docker image.
5. Pushes the image to Docker Hub.
6. Establishes a secure connection to the Ubuntu server using Tailscale and SSH.
7. Pulls the latest Docker image.
8. Replaces the previous application container.
9. Starts the updated container.

## Architecture

```text
Developer
   |
   | Git Push
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> Install Dependencies
   |
   +--> Validate Python Code
   |
   +--> Build Docker Image
   |
   v
Docker Hub
   |
   | Pull Image
   v
Tailscale + SSH
   |
   v
Ubuntu Server
   |
   +--> Stop and Remove Previous Container
   |
   +--> Start New Container
   |
   v
Flask Application
   |
   v
http://SERVER-IP:5008
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Ubuntu | Deployment server |
| Python | Application development |
| Flask | Web application framework |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Git & GitHub | Source code management |
| GitHub Actions | CI/CD automation |
| Tailscale | Secure network connectivity |
| SSH | Remote server access |
| YAML | Pipeline configuration |

## Project Structure

```text
devops-training/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Application

The application is built using Python and Flask.

It provides a simple web page displaying:

- Welcome To DevOps
- CI/CD Pipeline Successfully Deployed!
- Version: 2.0
- Deployed automatically using GitHub Actions.

## Docker Configuration

The application runs inside a Docker container.

**Container port:** `5006`

**Ubuntu host port:** `5008`

The application is accessible through:

```text
http://SERVER-IP:5008
```

Example Docker deployment command:

```bash
docker run -d \
  --name devops-training \
  --restart unless-stopped \
  -p 5008:5006 \
  waleednemer/devops-training:latest
```

## CI/CD Pipeline

The GitHub Actions workflow is stored at:

```text
.github/workflows/ci-cd.yml
```

### Continuous Integration (CI)

When code is pushed to GitHub, the pipeline:

- Checks out the repository.
- Sets up Python 3.12.
- Installs project dependencies.
- Validates Python syntax.
- Builds the Docker image.

### Continuous Delivery / Deployment (CD)

After a successful build on pushes to `main`:

- Authenticates with Docker Hub.
- Publishes the Docker image.
- Connects to the Ubuntu server through Tailscale.
- Authenticates using SSH.
- Pulls the latest image.
- Replaces the running application container.
- Starts the new container.

## GitHub Actions Secrets

The following repository secrets are required by the workflow:

| Secret | Description |
|---|---|
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |
| `TS_AUTHKEY` | Tailscale authentication key |
| `SSH_PRIVATE_KEY_B64` | Base64-encoded SSH private key |
| `SSH_HOST` | Ubuntu server Tailscale hostname or IP |
| `SSH_USER` | Ubuntu server username |

**Important:** Never store passwords, private keys, or access tokens directly in the repository. Use GitHub Actions Secrets.

## Verification

The deployment was verified by:

1. Confirming that the GitHub Actions deployment completed successfully.
2. Confirming that the Docker container started on the Ubuntu server.
3. Sending an HTTP request to the application:

```bash
curl -i http://127.0.0.1:5008/
```

4. Updating the application source code and pushing the changes to GitHub.
5. Confirming that the updated Version 2.0 page appeared automatically after deployment.

## Key DevOps Skills Demonstrated

- Git and GitHub version control.
- Python application development.
- Docker image creation and container management.
- Docker Hub image publishing.
- GitHub Actions workflow automation.
- CI/CD pipeline implementation.
- Linux server deployment.
- SSH remote administration.
- Secure networking with Tailscale.
- Automated application updates.

## Future Improvements

- Add Docker Health Checks.
- Add post-deployment automated HTTP tests.
- Implement automatic rollback on deployment failure.
- Introduce Docker Compose.
- Add application logging and monitoring.
- Integrate Kubernetes for container orchestration.

## Author

**Waleed Nemer**

GitHub: https://github.com/waleednemer

Docker Hub: https://hub.docker.com/u/waleednemer

Project: [devops-training](https://github.com/waleednemer/devops-training)
