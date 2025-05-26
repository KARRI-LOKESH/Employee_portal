from django import forms
from .models import Employee
from datetime import date

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        age = date.today().year - dob.year
        if age < 18:
            raise forms.ValidationError("Employee must be at least 18 years old.")
        return dob
