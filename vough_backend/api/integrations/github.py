import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        url = 'https://api.github.com/orgs/'+login
        response = requests.get(url)
        
        
        return response.json()
        
    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        url = 'https://api.github.com/orgs/'+login+'/public_members'
        response = requests.get(url)

        return len(response.json())
