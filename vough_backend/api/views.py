from rest_framework import viewsets, status, filters
from rest_framework.views import Response

from api import models, serializers
from api.integrations.github import GithubApi

from django.shortcuts import get_object_or_404

# TODOS:
# 1 - Buscar organização pelo login através da API do Github - feito
# 2 - Armazenar os dados atualizados da organização no banco - feito
# 3 - Retornar corretamente os dados da organização - feito
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API -feito


class OrganizationViewSet(viewsets.ModelViewSet):

    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    lookup_field = "login"
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['score', 'login', 'name']
    ordering = ['-score']

    def retrieve(self, request, login=None):        
        serializer = serializers.OrganizationSerializer
        gitApi = GithubApi()        
        
        response = gitApi.get_organization(login=login)
        
        if(response.status_code == 200):
            response_dict = response.json()
            org_public_repos = response_dict['public_repos']
            org_public_members = gitApi.get_organization_public_members(login=response_dict['login'])
            score = org_public_repos + org_public_members
            organization = models.Organization(
                login=response_dict['login'], name=response_dict['name'], score=score
            )
            organization.save()
            data = serializer(organization).data
            res_status = status.HTTP_200_OK  
        else:
            data = {}
            res_status = status.HTTP_404_NOT_FOUND

        return Response(data, status=res_status)
        
 