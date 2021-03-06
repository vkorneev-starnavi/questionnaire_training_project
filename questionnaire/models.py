from django.db import models
from django.db.models import fields
from django.db.models.fields import related

from users.models import User


class Questionnaire(models.Model):
    author = related.ForeignKey(User, on_delete=models.CASCADE)
    description = fields.TextField(max_length=1024)
    created_at = fields.DateTimeField(auto_now_add=True)


class QuestionnaireField(models.Model):
    FIELD_TYPES = (
        ('TXT', 'text'),
        ('RAD', 'radiobutton'),
        ('CHK', 'checkbox'),
        ('NUM', 'number_choice')
    )
    questionnaire = related.ForeignKey(Questionnaire, on_delete=models.CASCADE,
                                       related_name='fields')
    position = fields.IntegerField()
    field_type = fields.CharField(max_length=3, choices=FIELD_TYPES)
    text_before = fields.CharField(max_length=255)
    text_after = fields.CharField(max_length=255, blank=True)
    default_val = fields.CharField(max_length=255, blank=True)
    min_val = fields.IntegerField(null=True)
    max_val = fields.IntegerField(null=True)

    class Meta:
        unique_together = ('questionnaire', 'position')
        ordering = ['position']


class QuestionnaireAnswer(models.Model):
    questionnaire = related.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    respondent = related.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('questionnaire', 'respondent')


class FieldValue(models.Model):
    answer = related.ForeignKey(QuestionnaireAnswer, on_delete=models.CASCADE,
                                related_name='field_values')
    field = related.ForeignKey(QuestionnaireField, on_delete=models.CASCADE)
    value = fields.CharField(max_length=255)

    class Meta:
        unique_together = ('answer', 'field')
