from django import forms
from .models import ParticipantInfo


class AddParticipantForm(forms.ModelForm):

    class Meta:
        model = ParticipantInfo
        fields = ('participant_name',
                  'participant_age',
                  'participant_siblings',
                  'environmental_exposures',
                  'genetic_mutations',
                  'review_status')
