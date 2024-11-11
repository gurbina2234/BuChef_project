from django import forms
from .models import Review, Local
from PIL import Image

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False 
        self.fields['date'].required = True
        self.fields['score'].required = True


    class Meta:
        model = Review
        fields = ['score', 'date', 'message', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class AgregarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AgregarForm, self).__init__(*args, **kwargs)
        self.fields['local_image'].required = False 

    class Meta:
        model = Local
        fields = ['nombre', 'direccion', 'local_image']
        widgets = {
            'nombre': forms.Textarea(attrs={'rows': 2}),
            'direccion': forms.Textarea(attrs={'rows': 2}),
        }
