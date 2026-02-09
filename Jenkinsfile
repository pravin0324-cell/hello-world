pipeline {
    agent any

    environment {
        IMAGE_NAME = "hello-world"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm $IMAGE_NAME pytest'
            }
        }
    }

    post {
        success {
            echo '✅ Build & Tests passed'
        }
        failure {
            echo '❌ Build or Tests failed'
        }
    }
}
