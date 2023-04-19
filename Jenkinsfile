pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage("Build") {
            steps {
                sh '''
                    echo "Setting up the virtual environment."
                    ./setup.sh
                    pip install -r requirements.txt
                    echo "Running the Flask server"
                    flask run
                   '''
            }
        }
        stage("Test") {
            steps {
                sh '''
                    echo "Running test script"
                    python3 test.py
                   '''
            }
        }
        
    }
}
