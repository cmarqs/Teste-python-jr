from django.test import TestCase
from api.integrations.github import GithubApi
import requests

# Create your tests here.
gitApi = GithubApi()

class GithubApiTestCase(TestCase):
  
  def test_get_organization(self):
    
    #Consulta se org que existe retorna 200
    response = gitApi.get_organization(login='Netflix')    
    self.assertEqual(response.status_code, 200)
    
    #Consulta se org que não existe retorna 404
    response = gitApi.get_organization(login='abcdef1235673')    
    self.assertEqual(response.status_code, 404)

  def test_get_organization_public_members(self):
    
    response = gitApi.get_organization_public_members(login='Netflix')    
    self.assertEqual(response, 21)
  
  def test_calculate_organization_score(self):
    
    url = 'https://api.github.com/orgs/Netflix'
    response = requests.get(url)
    org_public_repos = response.json()['public_repos']
    
    url = 'https://api.github.com/orgs/Netflix/public_members'
    response = requests.get(url)
    org_public_members = len(response.json())

    url = 'http://localhost:8000/api/orgs/Netflix'
    response = requests.get(url)
    score_from_voughAPI = response.json()['score']    

    score_from_githubApi = org_public_repos + org_public_members    

    self.assertEqual(score_from_voughAPI, score_from_githubApi)

  def test_organizations_list(self):
    
    orgs = [ 
      'adobe',
      'RedHatOfficial',
      'cfpb',
      'Netflix',
      'Esri',
      'square',
      'twitter',
      'gilt',
    ]

    for org in orgs:
      url = 'http://localhost:8000/api/orgs/'+org
      response = requests.get(url)
    
    url = 'http://localhost:8000/api/orgs/'
    response = requests.get(url)
    
    self.assertEqual(len(orgs), response.json()['count'])


