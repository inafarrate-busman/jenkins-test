pipeline {
    parameters {
        string(name: 'GITHUB_USERNAME', description: 'Nombre de usuario de GitHub')
        password(name: 'GITHUB_TOKEN', description: 'Token de acceso personal de GitHub')
        string(name: 'REPO_NAME', description: 'Nombre del repositorio a crear')
        string(name: 'BRANCH', defaultValue: 'main', description: 'Nombre de la rama a crear en el repositorio')
    }
    agent any
    stages {
        stage('Crear repositorio') {
            steps {
                script {
                    def response = sh returnStatus: true, script: "curl -u ${params.GITHUB_USERNAME}:${params.GITHUB_TOKEN} https://api.github.com/user/repos -d '{\"name\":\"${params.REPO_NAME}\",\"auto_init\":true}'"
                    if (response != 200) {
                        error "No se pudo crear el repositorio. El status code fue ${response}."
                    }
                }
            }
        }
    }
}
