from django import forms

class SugerenciaFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()


class CrearSugerenciaFormulario(SugerenciaFormularioBase):
    ...
    
    
class ModificarSugerenciaFormulario(SugerenciaFormularioBase):
    ...


class BuscarSugerenciaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)