from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


rev_status_choices = [('NoReview', 'Not Reviewed'),
                      ('Accepted', 'Reviewed - Accepted'),
                      ('NotAccepted', 'Reviewed - Not Accepted')]


class ParticipantInfo(models.Model):
    participant_name = models.CharField(max_length=50, primary_key=True)
    participant_age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    participant_siblings = models.CharField(
        max_length=3,
        choices=(('Yes', 'Yes'),
                 ('No', 'No')),
        default='No',
    )
    environmental_exposures = models.TextField()
    genetic_mutations = models.TextField()
    review_status = models.CharField(
        max_length=23,
        choices=rev_status_choices,
        default='Not Reviewed',
    )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.participant_name
