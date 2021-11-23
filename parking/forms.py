from django.forms import ModelForm, DateInput
from parking.models import Cliente, Disponibilidad

class ClienteForm(ModelForm):
    """
    Formulario para crear clientes
    """
    class Meta:
        model=Cliente
        fields = '__all__'

class DisponibilidadForm(ModelForm):
    """
    Formulario para modificar Disponibilidad
    """
    class Meta:
        model=Disponibilidad
        fields = '__all__'


    