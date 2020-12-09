from django.shortcuts import render
from django.http import HttpResponse
from appgestion.models import Articulo


def buscar(request):
    #si txt_producto viene con dato if devuelve true
    if request.GET["txt_producto"]:
        producto_recibido = request.GET["txt_producto"]
        #comandos usados en la shell
        articulos=Articulo.objects.filter(nombre__contains=producto_recibido)
        return render(request,"Metraje.html",{"articulos":articulos,"producto_consultado":producto_recibido})
    else:
        mensaje="Debe ingresar un producto a buscar"
    return HttpResponse(mensaje)
#listo
def ingresar_producto(request):
    nombre=request.GET["txt_nombre"]
    categoria=request.GET["txt_categoria"]
    precio=request.GET["txt_precio"]
    if len(nombre)>0 and len(categoria)>0 and len(precio)>0:
        pro=Articulo(nombre=nombre,categoria=categoria,precio=precio)
        pro.save()
        mensaje="Articulo ingresado"
    else:
        mensaje="Aticulo No ingresado. Faltan datos por ingresar..."
    return HttpResponse(mensaje)

def eliminar_producto(request):
    if request.GET["txt_id"]: #true si encuentra valor
        id_recibido=request.GET["txt_id"]
        producto=Articulo.objects.filter(id=id_recibido)        
        if producto:
            pro=Articulo.objects.get(id=id_recibido)
            pro.delete()            
            mensaje="Producto eliminado"
        else:
            mensaje="Producto No eliminado. No existe producto con ese id"
    else:
        mensaje="Debe ingresar un id"
    return HttpResponse(mensaje)


#Uso de varios formularios en 1 página
def busqueda_productos(request):
    return render(request,"Metraje.html")

def formulario_ingreso(request):
    return render(request,"Metraje.html")

def formulario_eliminar(request):
    return render(request,"Metraje.html")    
