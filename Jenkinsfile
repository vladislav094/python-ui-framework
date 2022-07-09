#!groovy
//Run docker build
properties([disabledConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
        }
//     options {
//         buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10' ))
//         timestamps()
//     }
    stage("create docker image") {
        steps {
            echo "========== start building image =========="
            sh "docker build -t web_test"
            sh "docker run web_test pytest -s -v tests/test_heroku_app_1.py"
        }
    }
}

