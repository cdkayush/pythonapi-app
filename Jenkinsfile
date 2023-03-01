pipeline {
  agent any
  stages {
    stage('checkout-code') {
      steps {
        git(url: 'https://github.com/cdkayush/pythonapi-app.git', branch: 'dev')
      }
    }

    stage('show-contents') {
      steps {
        sh 'ls -l'
      }
    }

  }
}