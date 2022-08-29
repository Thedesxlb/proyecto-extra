from django.contrib import admin

from typing import Sequence

from .models import Cabañas, Promociones, Opinion


class AdministarCabañas(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('nombre', 'clave', 'descripcion', 'costo' ,'created', 'update')
    list_filter = ( 'clave', 'descripcion', 'costo')
    search_fields = ('nombre', 'clave', 'descripcion', 'costo')
    ordering = ('created',)
    date_hierarchy = 'created'
    list_per_page = 2
    list_display_links = ('nombre', 'descripcion', 'clave')

admin.site.register(Cabañas, AdministarCabañas)


class AdministrarPromociones(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('id','nombrePromo','descripcionPromo','costoPromo')
    list_filter = ( 'id', 'nombrePromo', 'costoPromo')
    search_fields = ('nombrePromo', 'descripcionPromo')
    ordering = ('created',)
    date_hierarchy = 'created'
    list_per_page = 2

admin.site.register(Promociones, AdministrarPromociones)



class AdministrarOpinion(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('id','nombreClien', 'nombreCabaña')
    search_fields: Sequence[str] = ('nombreClien', 'nombreCabaña')
    date_hierarchy = 'created'

admin.site.register(Opinion, AdministrarOpinion)