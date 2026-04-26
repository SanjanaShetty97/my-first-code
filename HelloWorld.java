🔧 PART 1 — Update Required Jenkins Plugins

Go to:

👉 Manage Jenkins → Manage Plugins → Available / Installed

Search and install/update:

Git Plugin
Pipeline Plugin
Maven Integration Plugin
(Also install) Slack Notification Plugin

✔ After installing → Restart Jenkins

⚙️ PART 2 — Configure Maven in Jenkins

Go to:

👉 Manage Jenkins → Tools → Maven installations

Click Add Maven

Fill:

Name: Maven3
Uncheck ❌ Install automatically

MAVEN_HOME:

C:\Program Files\maven

✔ Click Save

📁 PART 3 — Create Jenkinsfile (VERY IMPORTANT)

In your project repo (GitHub), create a file named:

👉 Jenkinsfile

Paste this:

pipeline {
    agent any

    tools {
        maven 'Maven3'
    }

    stages {
        stage('CHECKOUT') {
            steps {
                git 'your_github_repo_link'
            }
        }

        stage('Build') {
            steps {
                dir('demo') {
                    bat 'mvn clean install'
                }
            }
        }

        stage('Test') {
            steps {
                dir('demo') {
                    bat 'mvn test'
                }
            }
        }
    }
}

✔ Replace:

your_github_repo_link

with your actual repo URL

✔ Then:

git add Jenkinsfile
git commit -m "Added Jenkins pipeline"
git push
🚀 PART 4 — Create Pipeline Job in Jenkins

Go to Jenkins Dashboard:

👉 New Item

Name: MyPipeline
Select: Pipeline
Click OK

Now configure:

Scroll to Pipeline section
Definition → Pipeline script from SCM
SCM → Git
Repo URL → paste your GitHub link
Script Path → Jenkinsfile

✔ Save
✔ Click Build Now

💬 PART 5 — Setup Slack Notifications
Step 1: Create Slack Workspace

Go to:

👉 Slack

Create workspace (example: hello-odm9638)
Create a channel (e.g. #jenkins)
Step 2: Generate Slack Token

Open:

👉 https://my.slack.com/services/new/jenkins-ci

Select your workspace
Click Add Jenkins CI integration
Copy the Token
Step 3: Configure Slack in Jenkins

Go to:

👉 Manage Jenkins → Configure System

Scroll to Slack section

Fill:

Workspace: hello-odm9638
Credential:
Click Add → Secret Text
Secret: (paste token)
ID: slack-token
Default Channel: #jenkins

✔ Save

🧪 PART 6 — Test Slack Notification (Freestyle Job)

Create test job:

👉 New Item → Freestyle Project

Configure:

Build Step:

Add → Execute Windows batch command:
echo Jenkins Test

Post-build Action:

Select Slack Notifications
Tick all:
✔ Notify Success
✔ Notify Failure
✔ Notify Start

✔ Save

▶️ PART 7 — Run & Verify

Click:

👉 Build Now

✔ You should see:

Build runs in Jenkins
Message appears in Slack channel
