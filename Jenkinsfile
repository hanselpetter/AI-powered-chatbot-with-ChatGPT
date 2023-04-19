pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                    echo "Setting up the virtual environment."
                    ./python-api/setup.sh
                    pip install -r /python-api/requirements.txt
                    echo "Running the Flask server"
                    flask run
                   '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    echo "Running test script"
                    python3 /python-api/test.py
                   '''
            }
        }
        stage('Email Notification') {
            steps {
                mail(body: "${JOB_NAME}, build ${BUILD_NUMBER} Pytest completed.", subject: 'Pytest completed.', to: 'ibrahima.diallo1289@gmail.com')
                }
            }
            post {
                always {
                    echo 'The pipeline completed'
                    junit 'test_result/test_result_${BUILD_NUMBER}.xml'
                }
                success {                   
                    echo "Flask App Up and running!!"
                }
                failure {
                    echo 'Build stage failed'
                    error('Stopping early…')
                }
            }
        }
    }
