from django.db import models
from django.utils import timezone

rev_status_choices = [('Not Reviewed', 'Not Reviewed'),
                      ('Reviewed - Accepted', 'Reviewed - Accepted'),
                      ('Reviewed - Not Accepted', 'Reviewed - Not Accepted')]

class ParticipantInfo(models.Model):
    participant_name = models.CharField(max_length=50)
    participant_age = models.PositiveIntegerField()
    participant_siblings = models.CharField(
        max_length=3,
        choices = (('Yes', 'Yes'),
                   ('No', 'No')),
        default = 'No',
    )
    env_exposures = models.TextField()
    gen_mutations = models.TextField()
    # rev_status = models.CharField(ReviewStatus)
    rev_status = models.CharField(
        max_length=23,
        choices = rev_status_choices,
        default = 'Not Reviewed',
    )
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.participant_name

    def print_participant_info(self):
        print("Participant Name : {}".format(self.participant_name))
        print("Participant Age : {}".format(self.participant_age))
        print("Participant Siblings: {}".format(self.participant_siblings))
        print("Environmental Exposures: {}".format(self.env_exposures))
        print("Genetic Mutations: {}".format(self.gen_mutations))
        print("Review Status: {}".format(self.rev_status))

    def add_participant(self):
        self.date_create = models.DateTimeField(default=timezone.now)
        self.save()


class ReviewStatus(models.Model):
    rev_status = models.CharField(
        max_length=23,
        choices = rev_status_choices,
        default = 'Not Reviewed',
    )