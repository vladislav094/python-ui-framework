pipeline {
    agent any
//     {
//         dockerfile true
//     }
    environment {
        RUN_HEADLESS = 'True'
        HEADLESS = '-e RUN_HEADLESS=True'
    }
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                   sh "env"
                sh "docker build -t web_test ."
                sh "docker-compose up -d allure allure-ui"
                sh "docker run -e RUN_HEADLESS=True --name example1 web_test pytest -s tests/negative_tests/test_authorization_user_negative.py"
                sh "docker cp example1:/code/allure-results/ ${WORKSPACE}/"
                sh "docker rm example1"

                echo "========== finish building image =========="
            }
        }
        stage('reports') {
            steps {
            script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'allure-results']]
                    ])
            }
            }
        }

    }
}
