from django import forms

class ParticipantForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Age = forms.IntegerField()
    EnvExp = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='List all Environmental Exposures here'
    )

    def clean(self):
        cleaned_data = super(ParticipantForm, self).clean()
        Name = cleaned_data.get('Name')
        Age = cleaned_data.get('Age')
        EnvExp = cleaned_data.get('EnvExp')
        if not Name and not Age and not EnvExp:
            raise forms.ValidationError('you have to input your info')