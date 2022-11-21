pipeline {
    agent { any }
    environment {
        TEST_PREFIX = "HelloWorld!!"
    }
    stages {
        stage('Checkout Scm') {
            steps {
                git 'https://github.com/Nano204/JalaUniversity_DevOps.git'
                echo "Hello world!"
            }
        }
        stage("build") {
            steps {
                echo $TEST_PREFIX
            }
        }
    }
}
