#!/usr/bin/env groovy
pipeline {
    agent { any }
    environment {
        TEST_PREFIX = "HelloWorld!!"
    }
    stages {
        stage("build") {
            steps {
                echo $TEST_PREFIX
            }
        }
    }
}
