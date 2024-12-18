# Flask App with Docker and Jenkins Continuous Integration

## Overview
This repository demonstrates a **Flask** application containerized using **Docker** and integrated with **Jenkins** for Continuous Integration. With this setup, every code change can trigger a build pipeline to ensure code quality and deployment readiness.

## Features
- Flask-based web application.
- Dockerized application environment.
- CI pipeline configured using Jenkins.
- GitHub webhook for continuous integration.

---

## **Getting Started**

### Prerequisites
Ensure you have the following installed:
1. **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
2. **Python 3.8+**: [Installation Guide](https://www.python.org/downloads/)
3. **ngrok**: [Installation Guide](https://ngrok.com/download)
4. **Jenkins**: Follow installation steps below.

---

## **Installation Guide**

### Clone the repository
```bash
# Clone the Flask app with CI setup
$ git clone https://github.com/yass-arafat/hello-world.git --branch flask-docker-jenkins-ci

# Navigate into the project directory
$ cd hello-world
```

### Install Jenkins
1. **Install Java**:
   Jenkins requires Java to run. Install the latest version:
   ```bash
   sudo apt update
   sudo apt install -y openjdk-11-jre
   ```

2. **Download Jenkins**:
   ```bash
   wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc
   echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
   sudo apt update
   sudo apt install jenkins
   ```

3. **Start Jenkins**:
   ```bash
   sudo systemctl start jenkins
   sudo systemctl enable jenkins
   ```

4. **Access Jenkins**:
    - Open your browser and navigate to `http://localhost:8080`.
    - Follow the on-screen instructions to complete the setup.

   Retrieve the initial admin password:
   ```bash
   sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   ```
   Copy this password to log in and install the recommended plugins.

---

### Configure ngrok to expose Jenkins
1. **Start ngrok for Jenkins**:
   Open a terminal and run:
   ```bash
   ngrok http 8080
   ```
2. Copy the **public URL** provided by ngrok (e.g., `https://abcd1234.ngrok.io`).
3. Update the Jenkins configuration:
    - Go to **Manage Jenkins** → **Configure System**.
    - Set the Jenkins URL to the ngrok public URL.

---

### Set Up GitHub Webhook
1. **Enable GitHub Integration**:
    - In Jenkins, install the **GitHub Integration Plugin**: Go to **Manage Jenkins** → **Plugin Manager** → **Available Plugins**, search for `GitHub`, and install it.

2. **Create a New Pipeline Job**:
    - Navigate to **New Item** and create a **Pipeline** job.
    - Under **Build Triggers**, check **GitHub hook trigger for GITScm polling**.

3. **Configure GitHub Webhook**:
    - Navigate to the repository on GitHub.
    - Go to **Settings** → **Webhooks** → **Add webhook**.
        - **Payload URL**: `<ngrok-URL>/github-webhook/` (e.g., `https://abcd1234.ngrok.io/github-webhook/`).
        - **Content Type**: `application/json`.
        - **Secret**: (optional) Add a secret token.

4. **Test the Webhook**:
   Push a new commit to the branch or use the GitHub "Test webhook" feature to trigger Jenkins.

---

## **Building the Application**

### Using Docker
1. **Build Docker Image**:
   ```bash
   docker build -t flask-docker-jenkins .
   ```
2. **Run the Container**:
   ```bash
   docker run -p 5000:5000 flask-docker-jenkins
   ```
3. Open the application:
    - Navigate to `http://localhost:5000` in your browser.

---

## **Jenkins Pipeline Configuration**
### Example Pipeline Script
Use the following script for your Jenkins pipeline job:
```groovy
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yass-arafat/hello-world.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-docker-jenkins .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run flask-docker-jenkins pytest'
            }
        }
    }
}
```

---

## **Troubleshooting**

1. **Webhook Not Triggering**:
    - Ensure Jenkins URL matches the ngrok public URL.
    - Verify the "GitHub hook trigger for GITScm polling" is enabled.

2. **403 Errors from Webhook**:
    - Check webhook secret configuration in both GitHub and Jenkins.

3. **Pipeline Errors**:
    - Verify Docker and Python dependencies are correctly installed.
