from django.contrib     import admin
from tienda.models      import *
from .models            import Remoto                   

admin.site.site_header = "LCDUNI"


class RemotoAdmin(admin.ModelAdmin):
    search_fields = ('codigo','marca')
    list_display = ('codigo', 'marca')
    list_filter = ('marca',)
    
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre', )


admin.site.register(Marca,MarcaAdmin)
admin.site.register(Remoto,RemotoAdmin)

