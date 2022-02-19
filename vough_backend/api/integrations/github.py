import os
import requests


class GithubApi:
    API_URL = os.environ.get("GITHUB_API_URL")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    def get_organization(self, login: str):
        """Busca uma organização no Github

        :login: login da organização no Github
        """
        url = self.API_URL+'/orgs/'+login
        head = {'Authorization': 'token {}'.format(self.GITHUB_TOKEN)}
        return requests.get(url, head)
        
    def get_organization_public_members(self, login: str) -> int:
        """Retorna todos os membros públicos de uma organização

        :login: login da organização no Github
        """
        url = self.API_URL+'/orgs/'+login+'/public_members'
        head = {'Authorization': 'token {}'.format(self.GITHUB_TOKEN)}
        response = requests.get(url, head)

        return len(response.json())
