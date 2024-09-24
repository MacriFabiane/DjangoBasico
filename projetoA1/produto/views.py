from django.shortcuts import render

# Create your views here.
def metodo(request):
    return render(request, 'produto/index.html')# requisição e o caminho do arquivo html