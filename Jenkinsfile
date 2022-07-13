pipeline {
    agent {
        label 'master'
        }
    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "docker build -t web_test ."
                sh "docker run web_test pytest -s -v tests/negative_tests/test_authorization_user_negative.py"
            }
        }
    }
}

