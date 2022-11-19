pipeline {
    // Select a Jenkins slave with Docker capabilities
    agent {
        label 'built-in-node'
    }

    environment {
        PRODUCT = 'worldofgames'
        GIT_REPO = 'https://github.com/hanrikos/WorldOfGames'
        GIT_MAIN_BRANCH = 'main'
    }

    stages {
        // Ⓐ Retrieve the project code from the repository. Extract the branch
        // name from the context of execution which can be a branch build or a pull
        // request build.
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main',
                    credentialsId: '150b0133-ca98-4845-91d8-d6d19e9657d9',
                    url: 'ssh://git@github.com/hanrikos/WorldOfGames.git'
                }
            }
        }


	// ③ Build a container with the code source of the application
        stage('Build') {
            steps {
                script {
                    sh "docker build -t worldofgames -f Dockerfile ."
                }
            }
        }



	// ④ Create container from image
        stage("Run") {
            steps {
                sh "docker-compose up -d"
                sh """
                    docker run --rm worldofgames
                """
            }
        }


	// ④ Run the test using the built docker image
        stage('Test') {
            steps {
                script {
                    sh "docker exec -it worldofgames python ./tests/e2e.py"
                }
            }
        }

		stage('Login') {
			steps {
			    script {
				    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
				}
			}
		}


		stage('Push') {
			steps {
			    script {
				    sh 'docker push devopshenry/worldofgames:latest'
			    }
			}
		}
	}
	// ⑧ Cleanup
    post {
        always {
            script {
                sh "docker rm ${env.PRODUCT}"
            }
            deleteDir()
        }
    }
}