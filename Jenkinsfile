pipeline {
    agent any

    environment {
        RUN_HEADLESS = 'True'
        HEADLESS = '-e RUN_HEADLESS=True'
    }

    stages {
        stage("create docker image") {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                echo "========== start building image =========="
                   sh "env"
                   sh "docker rm example1"
                sh "docker build -t web_test ."
                sh "docker run \
                    -e RUN_HEADLESS=True \
                    --name example1 \
                    --rm \
                    --volume ${WORKSPACE}/allure-results/:/code/allure-results/ \
                    web_test \
                    pytest tests/negative_tests/test_general_checks.py::TestGeneralChecks::test_check_wrong_title_of_the_page"

//                     web_test pytest -s tests/negative_tests/test_authorization_user_negative.py
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_making_orders_positive.py"
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_search_module_operation.py"
//                 sh "docker run --rm -e RUN_HEADLESS=True web_test pytest -s tests/positive_tests/test_registration_and_authorization_positive.py"
                echo "========== finish building image =========="
            }
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
