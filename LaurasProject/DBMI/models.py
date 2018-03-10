# from django.db import models
#
# # Create your models here.
# # class Question(models.Model):
# #     question_text = models.CharField(max_length=200)
# #     pub_date = models.DateTimeField('date published')
# #
# # class Choice(models.Model):
# #     question = models.ForeignKey(Question, on_delete=models.CASCADE)
# #     choice_text = models.CharField(max_length=200)
# #     votes = models.IntegerField(default=0)
#
# class ParticipantId(models.Model):
#     participant_id = models.AutoField(primary_key=True, editable=False)
#     registration_date = models.DateTimeField('date registered')
#
# class ParticipantInfo(models.Model):
#     # participant_id = models.AutoField(primary_key=True, editable=False)
#     participant_id = models.ForeignKey(ParticipantId, on_delete=models.CASCADE)
#     participant_name = models.CharField(max_length=50)
#     participant_age = models.PositiveIntegerField()
#     # participant_siblings = models.Field.choices = (('Yes', 1), ('No', 0))
#     env_exposures = models.TextField()
#     # gen_mutations = models.TextField()
#     # rev_status = models.Field.choices = (
#     #     ('Not Reviewed', 1),
#     #     ('Reviewed - Accepted', 2),
#     #     ('Reviewed - Not Accepted', 3)
#     # )
