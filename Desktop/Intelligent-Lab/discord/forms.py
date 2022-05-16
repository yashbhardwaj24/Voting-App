from django.forms import ModelForm
from .models import Room 

class RoomModelForm(ModelForm):
    class Meta:
        model = Room 
        fields = '__all__'
        exclude = ['host','participants']

    def __init__(self,*args, **kwargs):
        super(RoomModelForm,self).__init__(*args, **kwargs)

        for key , field in self.fields.items():
            field.widget.attrs.update({
                'class':'input',
                'placeholder': f'Enter your {key}'
            })
    pass 