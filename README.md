# Two-Tier Flask Application with Jenkins CI/CD and Docker on AWS

🚀 **Fully Automated CI/CD Pipeline** using Jenkins, Docker, GitHub, and AWS EC2.

---

## Overview

This project demonstrates a **two-tier Flask web application** deployed automatically via a **Jenkins CI/CD pipeline**. The pipeline pulls code from GitHub, builds a Docker image, and deploys it on an **AWS EC2 instance**, making it accessible on the browser.

---

## Features

- **Two-Tier Flask Application**  
  - Python Flask backend
  - Simple web UI displaying deployment status
- **CI/CD Automation**  
  - Jenkins pipeline monitors `main` branch
  - Automatic Docker build & deployment on code push
- **Containerization with Docker**  
  - Docker image built and run on EC2
- **AWS Deployment**  
  - Publicly accessible app through EC2 public IP
  - Security group configured for HTTP access
- **Resume / Portfolio Ready**  
  - Demonstrates end-to-end DevOps workflow

---

## Architecture

GitHub → Jenkins → Docker → AWS EC2 → Browser


1. Developer pushes code to GitHub (`main` branch)  
2. Jenkins detects change and triggers pipeline  
3. Jenkins builds Docker image (`flask-devops-app`)  
4. Jenkins deploys container on EC2 (mapped to port 80)  
5. Application live at `http://<EC2_PUBLIC_IP>`

---

## Getting Started

### Prerequisites

- AWS EC2 instance (Ubuntu)
- Docker installed on EC2
- Jenkins installed and running
- GitHub repository containing Flask app & Jenkinsfile
- Security group allows ports: 22, 80, 5000 (optional), 8080 (Jenkins)

---

### Steps to Run

1. **Clone repo:**

```bash
git clone https://github.com/irfanjat/Two-tier-flask-app.git
cd Two-tier-flask-app


Build Docker Image manually (if needed):

docker build -t flask-devops-app .


Run Docker Container:

docker stop flask-app || true
docker rm flask-app || true
docker run -d -p 80:5000 --name flask-app flask-devops-app


Access in Browser:

http://<EC2_PUBLIC_IP>


Should see:

Two Tier Flask Application
Deployed via Jenkins CI/CD 🚀

Jenkins Pipeline (Jenkinsfile)
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/irfanjat/Two-tier-flask-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-devops-app .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 80:5000 --name flask-app flask-devops-app
                '''
            }
        }
    }
}

Demo

App URL: http://<EC2_PUBLIC_IP>

Automatic deployment triggers with every push to main branch

Tech Stack

Frontend & Backend: Flask

CI/CD: Jenkins

Containerization: Docker

Cloud: AWS EC2

Version Control: GitHub
