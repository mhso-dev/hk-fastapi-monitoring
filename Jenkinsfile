pipeline {
	agent any
	stages {
		stage("Checkout") {
			steps {
				checkout scm
			}
		}
		stage("Build") {
			steps {
				sh 'docker compose build web'
			}
		}
		stage("deploy") {
			steps {
				sh "docker compose up -d"
			}
		}
        stage("Update Model"){
            steps {
                sh "docker exec -i hk-fastapi-monitoring python train.py"
            }
        }
	}
}