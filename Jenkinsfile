pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Setup') {
            steps {
                bat '''
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                pip install -r requirements.txt
                pip install allure-pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                pytest tests/ -v --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                allure generate allure-results -o allure-report --clean
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
