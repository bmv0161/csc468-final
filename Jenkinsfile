pipeline {
    agent none 
    stages {
        stage ('Deploy') {
            agent {
                node {
                    label 'deploy'
                }
            }
            steps {
                sshagent(credentials: ['cloudlab']) {
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml dp963106@130.127.132.207:~/'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.207 kubectl apply -f /users/dp963106/database.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.207 kubectl apply -f /users/dp963106/database-services.yaml -n jenkins'

                }
            }
        }
    }
}
