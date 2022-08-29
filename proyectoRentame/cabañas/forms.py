from django import forms

from.models import Cabañas, Opinion


class CabañasForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['duda',]



class ContactoForm(forms.ModelForm):
    class Meta:
        model= Opinion
        fields = ['nombreClien', 'nombreCabaña', 'duda','imagenOp']
