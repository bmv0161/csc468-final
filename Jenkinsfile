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
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml bm935325@130.127.132.237:~/'
                    sh 'ssh -o StrictHostKeyChecking=no bm935325@130.127.132.237 kubectl apply -f /users/bm935325/webscraper.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no bm935325@130.127.132.237 kubectl apply -f /users/bm935325/webscraper_services.yaml -n jenkins'

                }
            }
        }
    }
}
