from django import forms
from .models import Elementos, Participantes

class ElementosForm(forms.ModelForm):
    class Meta:
        model = Elementos
        fields = '__all__'
        
class ParticipantesForm(forms.ModelForm):
    class Meta:
        model = Participantes
        fields = '__all__'

