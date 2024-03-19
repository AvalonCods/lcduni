from django.shortcuts               import render
from django.core.mail               import EmailMessage
from django.contrib.auth.forms      import UserCreationForm
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth            import authenticate,login,logout
from django.http                    import HttpResponseRedirect
from tienda.models                  import Remoto
from tienda.models                  import Marca
from tienda.forms                   import ContactoForm
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from .models                        import Remoto
from django.db.models               import Q

def tienda(request):
    remotos_list = Remoto.objects.all()

    # Filtrar por tipo
    tipos = Remoto.TIPO
    tipo = request.GET.get('tipo', '')
    if tipo:
        remotos_list = remotos_list.filter(tipo=tipo)

    # Filtrar por marca
    marca_id = request.GET.get('marca', '')
    if marca_id:
        remotos_list = remotos_list.filter(marca=marca_id)

    # Ordenar
    orden = request.GET.get('orden', 'codigo')
    remotos_list = remotos_list.order_by(orden)

    # Paginar
    paginator = Paginator(remotos_list, 10)  # Show 10 remotos per page
    page = request.GET.get('page')

    try:
        remotos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        remotos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        remotos = paginator.page(paginator.num_pages)

    marcas = Marca.objects.all()

    return render(
        request,
        'tienda.html',
        {'remotos': remotos, 'marcas': marcas, 'tipos': tipos}
    )

def index(request):
    return render(request,'index.html')

def contacto(request):
    if request.method=='POST':
        formulario=ContactoForm(request.POST)
        if formulario.is_valid():
            asunto='Correo desde la Tienda'
            contenido= formulario.cleaned_data["mensaje"]+'\n\n'
            contenido+= 'Comunicarse al mail: ' + formulario.cleaned_data['correo']
            correo= EmailMessage(asunto,contenido,to=['jmendez@bios.edu.uy'])
            try:
                correo.send()
                return render(request, 'correo_enviado.html')
            except:
                return render(request, 'correo_no_enviado.html')
    else:
        formulario= ContactoForm()
        return render (request,'contacto.html',{'formulario':formulario})
    return render (request, "contacto.html")
def usuario_nuevo(request):
    if request.method== 'POST':
        formulario= UserCreationForm(request.POST)
        try:
            formulario.save()
            return render(request, 'usuario_creado.html')
        except:
            return render(request, 'usuario_nuevo.html', {'formulario':formulario})
    else: 
        formulario= UserCreationForm()
        return render(request,'usuario_nuevo.html',{'formulario':formulario})
def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/privado')
    elif request.method=='POST': 
        formulario= AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario= request.POST['username']
            clave= request.POST['password']
            acceso= authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
            else:
                return render(request, 'no_usuario.html')
    else:
        formulario= AuthenticationForm()
        return render(request, 'ingresar.html', {'formulario':formulario})
@login_required(login_url='/ingresar')    
def privado(request):
    usuario= request.user
    return render(request, 'privado.html', {'usuario':usuario})
def salir(request):
    if not request.user.is_anonymous:
        logout(request)
        return HttpResponseRedirect('/ingresar')
    else:
        return HttpResponseRedirect('/')

def error_404(request, exception):
    return render (request, '404.html', {})
def error_500(request):
    return render (request, '500.html', {})


def busqueda(request):
    if "buscar" in request.GET and request.GET["buscar"]:
        consulta = request.GET["buscar"]
        # Realiza una búsqueda que coincide con la marca o el código
        remotos = Remoto.objects.filter(Q(marca__icontains=consulta) | Q(codigo__icontains=consulta))
        return render(request, 'resultados.html', {'remotos': remotos})
    else:
        return render(request, 'resultados.html')    
    
def tienda_SM(request):
    remotos_smart = Remoto.objects.filter(tipo="smart")
    return render(request, 'tienda_SM.html', {'remotos': remotos_smart})
def tienda_NS(request):
    remotos_nosmart = Remoto.objects.filter(tipo="no_smart")
    return render(request, 'tienda_NS.html', {'remotos': remotos_nosmart})

