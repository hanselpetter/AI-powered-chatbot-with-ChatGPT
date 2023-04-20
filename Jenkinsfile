pipeline {
    agent any
    stages {
        stage("Build") {
            steps {
                sh '''
                    echo "Setting up the virtual environment."
                    ./setup.sh
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
