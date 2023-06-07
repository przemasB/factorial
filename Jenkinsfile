pipeline {
  agent { docker { image 'ubuntu:22.04' } }
  stages {
    stage('Build') {
      steps {
        sh 'apt update'
        sh 'apt install -y python3 pip'
        sh 'pip install pyinstaller'
	sh 'python3 -m py_compile factorial.py'
	stash(name: 'compiled-results', includes: '*.py*')
      }
    }
    stage('Test') {
      steps {
        sh 'python3 factorial_test.py'
      }   
    }
    stage('Deliver') {
      steps {
        sh 'echo "deliver"'
	dir(path: env.BUILD_ID) { 
	  unstash(name: 'compiled-results') 
          sh 'pyinstaller -F factorial.py' 
        }
     }   
     post {
       success {
         archiveArtifacts "${env.BUILD_ID}/dist/factorial" 
         sh 'rm -rf build dist'
    }
   }
  }
 }
}
