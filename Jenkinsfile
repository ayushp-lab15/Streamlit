pipeline {
    agent {
        node {
            label 'Ubuntu_Slave'
        }
    }
    stages {
        stage("checkout Code") {
            steps {
                git url:'https://github.com/ayushp-lab15/Streamlit.git', branch:'main'
            }
        }
        stage("Cleanup Stage") {
            steps {
                sh 'docker rm -f $(docker ps -aq)'
            }
        }
        stage("Build Docker image") {
            steps {
                sh 'docker build -t myimage .'
            }
        }
        stage("Create Container") {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}

