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
                    sh "sed -i 's/DOCKER_REGISTRY/${docker_user}/g' mydb.yaml"
                    sh "sed -i 's/BUILD_NUMBER/${BUILD_NUMBER}/g' mydb.yaml"
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yaml lngo@130.127.132.231:~/'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.231 kubectl apply -f /users/lngo/mydb.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.231 kubectl apply -f /users/lngo/mysql-secret.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no dp963106@130.127.132.231 kubectl apply -f /users/lngo/mysql-storage.yaml -n jenkins'                                        

                }
            }
        }
    }
}
