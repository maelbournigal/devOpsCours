pipeline {
    agent any
   
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'ssh mbournigal@192.168.213.128 mkdir -p /home/mbournigal/temp_deploy'
                sh 'scp -r dist mbournigal@192.168.213.128:/home/mbournigal/temp_deploy'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy ....'
            }
        }
    }
}
