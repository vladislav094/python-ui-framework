pipeline {

    agent any

    environment {
        HEADLESS = '-e RUN_HEADLESS=True'
        RUN_HEADLESS = 'True'
    }

    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t web_test ."
//                 sh "env"
//                 sh "docker run --rm $HEADLESS web_test pytest"
                sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/negative_tests/test_authorization_user_negative.py"
                sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_making_orders_positive.py"
                sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_search_module_operation.py"
                sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_registration_and_authorization_positive.py"
            }
        }
    }
}

