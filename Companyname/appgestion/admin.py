from django.contrib import admin

# Register your models here.
from appgestion.models import Cliente,Articulo,Pedido

admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Pedido)


