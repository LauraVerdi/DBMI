from django import forms
from .models import ParticipantInfo, ReviewStatus, rev_status_choices

# class ParticipantForm(forms.ModelForm):
#
#     class Meta:
#         model = ParticipantInfo
#         fields = ('Name', 'Age', 'Sibs')
#
# YES_OR_NO_CHOICE = ('YES', 'NO')
# REV_STATUS = ('Not Reviewed', 'Reviewed - Approved', 'Reviewed - Not Approved')

class AddParticipantForm(forms.ModelForm):

    class Meta:
        model = ParticipantInfo
        fields = ('participant_name', 'participant_age', 'participant_siblings', 'env_exposures', 'gen_mutations', 'rev_status')

class ReviewStatusForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super(ReviewStatusForm, self).__init__(*args, **kargs)

    class Meta:
        model = ReviewStatus
        fields = '__all__'
        # fields = rev_status_choices
        # print("fields=", fields)
        # fields = []
        # for i in rev_status_choices:
        #     fields.append(i[0])

    # status = forms.ChoiceField(choices=rev_status_choices)

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
