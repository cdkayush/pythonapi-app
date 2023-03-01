pipeline {
  agent any
  stages {
    stage('checkout-code') {
      steps {
        git(url: 'https://github.com/cdkayush/pythonapi-app.git', branch: 'dev')
      }
    }

    stage('show-contents') {
      parallel {
        stage('show-contents') {
          steps {
            sh 'ls -l'
          }
        }

        stage('print cwd') {
          steps {
            sh 'pwd'
            echo 'Hello this is my first pipeline'
          }
        }

        stage('install deps for python code') {
          steps {
            sh 'pip install -r requirements.txt'
          }
        }

      }
    }

  }
}