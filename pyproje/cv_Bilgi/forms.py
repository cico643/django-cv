from django import forms
from  .models import Bilgi

class BilgiForm(forms.ModelForm):


    class Meta: #Kullanıcıya servis edilecek olan form
        model=Bilgi
        fields=[
            'Name',
            'Surname',
            'content',
            'experience',
            'hobi',
            'image',
            'job',
            'language',
            'adress',
            'phone',
            'email',
            'date',
            'dogumyeri',
            'medeni_hali',

        ]

