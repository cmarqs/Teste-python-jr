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
    ordering = ['score']

    def retrieve(self, request, login=None):
        gitApi = GithubApi()
        queryset = models.Organization.objects.all()
        serializer = serializers.OrganizationSerializer
        organization = get_object_or_404(queryset, pk=login)
        response = gitApi.get_organization(login=organization.login)        

        org_public_repos = response.json()['public_repos']
        org_public_members = gitApi.get_organization_public_members(login=organization.login)

        organization.score = org_public_repos + org_public_members
        organization.save()
        org_serializer = serializer(organization)
        
        if(organization):
            res_status = status.HTTP_200_OK    
        else:
            res_status = status.HTTP_404_NOT_FOUND

        return Response(org_serializer.data, status=res_status)
        
 