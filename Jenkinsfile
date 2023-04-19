pipeline {
    agent any
    stages {
        stage("Build") {
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
        stage("Test") {
            steps {
                sh '''
                    echo "Running test script"
                    python3 /python-api/test.py
                   '''
            }
        }
        
    }
}
