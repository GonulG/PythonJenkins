pipeline {
    agent any
    environment {
        DEVELOPER BRANCH = 'develop'
        BRANCH = "${BRANCH_NAME}"
        ANSIBLE_FORCE_COLOR = 'true'
    }
    stages {
        stage('Get Branch Name'){
            steps{
                script{
                    branch = env.BRANCH
                    }
        }
    }

    stage('Set Pending Status'){
        steps{
            script{
                sh 'echo "Pending"'
            }
        }
    }

    stage("Automation process"){
        steps{
            scripts{
                dir('C:\Program Files\GONUL\pipelinetest1'){
                    echo 'Automation process running...'
                        sh 'pip3 install -r requirements.txt'
                        sh 'pwd'
                }
            }
        }
    }

    post{
        always{
            echo 'Automation Process finished...'
        }
    }


}