#!/usr/bin/env groovy
pipeline {
    agent { any }
    environment {
        TEST_PREFIX = "HelloWorld!!"
    }
    stages {
        stage("Hello World!!") {
            steps {
                echo $TEST_PREFIX
            }
        }
    }
}
