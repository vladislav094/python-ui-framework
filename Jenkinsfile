pipeline {

    agent {
        dockerfile true
    }

    environment {
        RUN_HEADLESS = 'True'
    }

    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                   sh "env"
                   sh "pytest -s tests/negative_tests/test_authorization_user_negative.py::TestAuthorizationRegistrationNegative::test_authorization_with_invalid_credentials_negative --alluredir='$WORKSPACE'/allure-report"
//                 sh "docker build -t web_test ."
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/negative_tests/test_authorization_user_negative.py"
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_making_orders_positive.py"
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_search_module_operation.py"
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_registration_and_authorization_positive.py"

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

