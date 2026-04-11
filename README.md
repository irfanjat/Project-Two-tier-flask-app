# 🐍 Two-Tier Flask Application with Jenkins CI/CD and Docker on AWS.

> Fully automated CI/CD pipeline using Jenkins, Docker, GitHub, and AWS EC2

---

## 📌 Overview.

This project demonstrates a **two-tier Flask web application** deployed automatically via a **Jenkins CI/CD pipeline**. The pipeline pulls code from GitHub, builds a Docker image, and deploys it on an **AWS EC2 instance** — making the app directly accessible in the browser.

---

## ✨ Features

| Feature | Details |
|---|---|
| **Flask Backend** | Two-tier web application powered by Python Flask |
| **CI/CD Automation** | Jenkins monitors the `main` branch and triggers the pipeline on every push |
| **Docker Containerization** | Docker image is automatically built and run on EC2 |
| **AWS Deployment** | App is publicly accessible via the EC2 public IP in any browser |

---

## 🏗️ Architecture

```
Developer → GitHub (main) → Jenkins → Docker Build → AWS EC2 → Browser
```

1. **Developer** pushes code to the `main` branch on GitHub
2. **Jenkins** detects the change and triggers the pipeline
3. **Jenkins** builds the Docker image (`flask-devops-app`)
4. **Jenkins** deploys the container on EC2 (mapped to port 80)
5. **Application** goes live at `http://<EC2_PUBLIC_IP>`

---

## 🛠️ Tech Stack

- **Backend / Frontend:** Python Flask
- **CI/CD:** Jenkins
- **Containerization:** Docker
- **Cloud Provider:** AWS EC2
- **Version Control:** GitHub

---

## ✅ Prerequisites

Make sure the following are in place before getting started:

- [ ] AWS EC2 instance (Ubuntu)
- [ ] Docker installed on EC2
- [ ] Jenkins installed and running (port `8080`)
- [ ] GitHub repository containing the Flask app & `Jenkinsfile`
- [ ] Security Group with the following ports open:

| Port | Purpose |
|------|---------|
| `22` | SSH Access |
| `80` | HTTP (App) |
| `8080` | Jenkins Dashboard |
| `5000` | Flask (optional, for direct access) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/irfanjat/Two-tier-flask-app.git
cd Two-tier-flask-app
```

### 2. Build the Docker Image (Manual — if needed)

```bash
docker build -t flask-devops-app .
```

### 3. Run the Container

```bash
docker stop flask-app || true
docker rm flask-app || true
docker run -d -p 80:5000 --name flask-app flask-devops-app
```

### 4. Open in Browser

```
http://<YOUR_EC2_PUBLIC_IP>
```

Once successfully deployed, you should see:

```
Two Tier Flask Application
Deployed via Jenkins CI/CD 🚀
```

---

## 🔄 Jenkins CI/CD Pipeline Flow

```
[Code Push to GitHub]
        ↓
[Jenkins Webhook Triggered]
        ↓
[Docker Image Build]
        ↓
[Old Container Stop & Remove]
        ↓
[New Container Deploy on Port 80]
        ↓
[App Live at EC2 Public IP]
```

> ⚡ Every push to the `main` branch triggers an **automatic deployment**.

---

## 📁 Project Structure

```
Two-tier-flask-app/
├── app.py              # Flask application
├── Dockerfile          # Docker image configuration
├── Jenkinsfile         # CI/CD pipeline definition
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Web UI
```

---

## 🌐 Live Demo

| Item | Value |
|------|-------|
| App URL | `http://<EC2_PUBLIC_IP>` |
| Trigger | Auto-deploy on every `main` branch push |
| Jenkins Dashboard | `http://<EC2_PUBLIC_IP>:8080` |

---

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ by <a href="https://github.com/irfanjat">irfanjat</a></p>
