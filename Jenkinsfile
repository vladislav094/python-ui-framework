pipeline {

    agent any

    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t web_test ."
                sh "docker run web_test pytest -s -v tests/negative_tests/test_authorization_user_negative.py"
                sh "docker run web_test pytest -s -v tests/positive_tests/test_making_orders_positive.py"
                sh "docker run web_test pytest -s -v tests/positive_tests/test_search_module_operation.py"
                sh "docker run web_test pytest -s -v tests/positive_tests/test_registration_and_authorization_positive.py"
            }
        }
    }
}

