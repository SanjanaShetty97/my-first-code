✅ 1. Requirements (What you need)

Before starting, you need these tools:

🔧 Core Tools
Java JDK (11 or higher) → to run Java programs
Apache Maven → build tool
Visual Studio Code → code editor
Git → version control
GitHub account → for CI/CD pipeline
⚙️ 2. Install Required Tools (Step-by-Step)
🔹 Step 1: Install Java (JDK 11+)

Use:

Oracle JDK OR OpenJDK
Steps:
Download JDK (11 or above)
Install it
Set environment variables:

👉 In Windows:

Open Environment Variables
Add:
JAVA_HOME = C:\Program Files\Java\jdk-XX
Edit PATH → Add:
%JAVA_HOME%\bin
Verify:
java -version
🔹 Step 2: Install Apache Maven

Use:

Apache Maven
Steps:
Download ZIP
Extract to:
C:\apache-maven
Set variables:
MAVEN_HOME = C:\apache-maven

Add to PATH:

%MAVEN_HOME%\bin
Verify:
mvn -version
🔹 Step 3: Install Visual Studio Code

Use:

Visual Studio Code

Install normally.

🔹 Step 4: Install VS Code Extensions

Inside VS Code Extensions tab, install:

Extension Pack for Java
Maven for Java
Debugger for Java
🔹 Step 5: Install Git

Use:

Git

Verify:

git --version
🧱 3. Create Maven Project in VS Code
Steps:
Open VS Code
Press:
Ctrl + Shift + P
Type:
Java: Create Java Project
Select:
Maven → Create from Archetype
Choose:
maven-archetype-quickstart
Enter:
Group Id: com.example
Artifact Id: demo
Select folder → project auto-creates
📁 Project Structure
demo/
 ├── src/
 ├── pom.xml
📤 4. Push Project to GitHub

Use:

GitHub
Steps:

Inside project folder:

git init
git add .
git commit -m "Initial commit"

Create repo on GitHub → then:

git remote add origin https://github.com/your-username/demo.git
git branch -M main
git push -u origin main
⚙️ 5. Create CI/CD Pipeline (GitHub Actions)
📁 Step 1: Create Folder Structure

Inside your project:

demo/
 ├── .github/
      └── workflows/
            └── maven.yml
📝 Step 2: Add maven.yml

Paste this:

name: Java CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: windows-latest

    env:
      FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '11'

      - name: Build using Maven
        run: mvn clean install
        working-directory: demo
🚀 6. Push Pipeline Code
git add .
git commit -m "Added CI/CD pipeline"
git push
🔍 7. Check CI/CD Pipeline
Go to your GitHub repo
Click Actions tab
You will see:
Java CI/CD Pipeline → Running / Success
✅ What This Pipeline Does
Runs on every push to main
Installs Java
Builds project using Maven
Verifies build success
🧠 Quick Summary

You just built:

✔ Maven Java project
✔ GitHub repository
✔ CI/CD pipeline using GitHub Actions
