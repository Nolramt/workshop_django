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
def pagina(request):
    return render(request,"home.html")
def fazer_soma(request):
    resu = None

    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])

        resu = num1 + num2

    return render(request, 'home.html', {'resu': resu})