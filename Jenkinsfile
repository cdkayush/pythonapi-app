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

    stage('build pyc') {
      steps {
        sh 'python3 -m py_compile apicall.py'
        fileExists '__pycache__/apicall.cpython-310.pyc'
        writeFile(file: 'status.txt', text: 'On Stage3')
      }
    }

    stage('run test') {
      steps {
        sh 'python3 -m pytest .'
        readFile 'status.txt'
      }
    }

    stage('build docker img') {
      steps {
        sh 'docker build -t myapp:v1 .'
      }
    }

  }
}