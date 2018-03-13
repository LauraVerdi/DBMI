from django.db import models
from django.utils import timezone


rev_status_choices = [('Not Reviewed', 'NoReview'),
                      ('Reviewed - Accepted', 'Accepted'),
                      ('Reviewed - Not Accepted', 'NotAccepted')]


class ParticipantInfo(models.Model):
    participant_name = models.CharField(max_length=50, primary_key=True)
    participant_age = models.PositiveIntegerField()
    participant_siblings = models.CharField(
        max_length=3,
        choices=(('Yes', 'Yes'),
                 ('No', 'No')),
        default='No',
    )
    env_exposures = models.TextField()
    gen_mutations = models.TextField()
    rev_status = models.CharField(
        max_length=23,
        choices=rev_status_choices,
        default='Not Reviewed',
    )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.participant_name

