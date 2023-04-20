pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh '''
                    echo "Checking out SCM."
                   '''
            }
        }
        stage("Test") {
            steps {
                sh '''
                    echo "Running test script"
                   '''
            }
        }
        stage("Push to DockerHub") {
            steps {
                sh '''
                    echo "Deploying to DockerHub"
                   '''
            }
        }
        stage("Push to AWS ECR") {
            steps {
                sh '''
                    echo "Deploying docker image to ECR"
                   '''
            }
        }
        
    }
}
