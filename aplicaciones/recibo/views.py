from django.shortcuts import render
from .models import cliente

# Create your views here.
def home(request):
       clientesListados = cliente.objects.all()
       # Despliega informacion a la pagina principal
       return render(request, "gestionLista.html", {"listado": clientesListados})