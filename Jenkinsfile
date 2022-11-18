pipeline {
    // Select a Jenkins slave with Docker capabilities
    agent {
        label 'docker'
    }

    environment {
        PRODUCT = 'ghcli'
        GIT_REPO = 'https://github.com/hanrikos/WorldOfGames'
        GIT_MAIN_BRANCH = 'main'
    }

    options {
        ansiColor('xterm')
        skipDefaultCheckout()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        // Ⓐ Retrieve the project code from the repository. Extract the branch
        // name from the context of execution which can be a branch build or a pull
        // request build.
        stage('Checkout') {
            steps {
                script {
                    BRANCH_NAME = env.CHANGE_BRANCH ? env.CHANGE_BRANCH : env.BRANCH_NAME
                    deleteDir()
                    git url: "git@<githubHost>:<org>/<repo>.git", branch: BRANCH_NAME
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
        stage('Run') {
            steps {
                script {
                    sh " docker compose up"
                }
            }
        }


	// ④ Run the test using the built docker image
        stage('Test') {
            steps {
                script {
                    sh "python3 ./tests/e2e.py"
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