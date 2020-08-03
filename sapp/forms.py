from django import forms
from .models import StudentInformation

class StudentInfo(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = (
            'id_number', 'first_name','last_name','email','phone','father_name','mother_name','cgpa'
        )
