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
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml dp963106@130.127.132.237:~/'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.237 kubectl apply -f /users/dp963106/chatbot.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.237 kubectl apply -f /users/dp963106/chatbot_services.yaml -n jenkins'

                }
            }
        }
    }
}
