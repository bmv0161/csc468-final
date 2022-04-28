pipeline {
    agent none 
    environment {
        docker_user = "dominicpisano"
    }
    stages {
        stage('Publish') {
            agent {
                kubernetes {
                    inheritFrom 'agent-template'
                }
            }
            steps{
                container('docker') {
                    sh 'echo $DOCKER_TOKEN | docker login --username $DOCKER_USER --password-stdin'
                    sh 'cd database; docker build -t $DOCKER_USER/database:$BUILD_NUMBER .'
                    sh 'docker push $DOCKER_USER/database:$BUILD_NUMBER'
                }
            }
        }
        stage ('Deploy') {
            agent {
                node {
                    label 'deploy'
                }
            }
            steps {
                sshagent(credentials: ['cloudlab']) {
                    sh "sed -i 's/DOCKER_REGISTRY/${docker_user}/g' database.yaml"
                    sh "sed -i 's/BUILD_NUMBER/${BUILD_NUMBER}/g' database.yaml"
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml dp963106@130.127.132.207:~/'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.207 kubectl apply -f /users/dp963106/database.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.207 kubectl apply -f /users/dp963106/database_services.yaml -n jenkins'
                }
            }
        }
    }
}
