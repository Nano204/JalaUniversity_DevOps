pipeline {
    agent any
    environment { 
        TEST_PREFIX = 'Hello Wolrd!'
    }
    stages {
        stage('Example') {
            steps {
                sh 'printenv TEST_PREFIX'
                sh './20221117_HW/scripts/hello_world.sh'
            }
        }
    }
}