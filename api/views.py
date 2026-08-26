from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def consultar_cep(request):
    cep=input("Digite seu cep: ")
    url=f"https://viacep.com.br/ws/{cep}/json"

    resposta=requests.get(url)

    dados = resposta.json()

    return JsonResponse(dados)
