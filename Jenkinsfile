pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/irfanjat/Two-tier-flask-app.git'
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
                docker run -d -p 5000:5000 --name flask-app flask-devops-app
                '''
            }
        }
    }
}
