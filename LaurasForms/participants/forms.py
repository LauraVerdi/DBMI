from django import forms
from .models import ParticipantInfo

# class ParticipantForm(forms.ModelForm):
#
#     class Meta:
#         model = ParticipantInfo
#         fields = ('Name', 'Age', 'Sibs')
#
YES_OR_NO_CHOICE = ('YES', 'NO')
REV_STATUS = ('Not Reviewed', 'Reviewed - Approved', 'Reviewed - Not Approved')

class AddParticipantForm(forms.ModelForm):

    class Meta:
        model = ParticipantInfo
        fields = ('participant_name', 'participant_age', 'participant_siblings', 'env_exposures', 'gen_mutations', 'rev_status')


# class VerifyParticipantForm(forms.ModelForm):
#
#     class Meta:
#         model = ParticipantInfo
#         fields = ('participant_name', 'participant_age', 'participant_siblings', 'env_exposures', 'gen_mutations', 'rev_status')

# class AddParticipantForm(forms.Form):
#     Name = forms.CharField(widget=forms.TextInput())
#     # Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
#     Age = forms.IntegerField(widget=forms.NumberInput())
    # Sibs = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=YES_OR_NO_CHOICE
    # )
    # EnvExp = forms.CharField(
    #     max_length=2000,
    #     widget=forms.Textarea(),
    #     help_text='List all Environmental Exposures here.'
    # )
    # GenMuts = forms.CharField(
    #     max_length=2000,
    #     widget=forms.Textarea(),
    #     help_text='List all Genetic Mutations here.'
    # )
    # RevStatus = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=REV_STATUS
    # )
