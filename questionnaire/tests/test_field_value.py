from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from questionnaire.models import Questionnaire, QuestionnaireField, \
    FieldValue, QuestionnaireAnswer
from users.models import User


class FieldValueTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.users = [
            User.objects.create_user('test1', email='test1@email.com',
                                     password='test1')
        ]
        self.questionnaires = [
            Questionnaire.objects.create(author=self.users[0],
                                         description='Test description')
        ]

    def test_default_value_is_used(self):
        self.client.force_login(self.users[0])
        respondent_url = reverse('user-detail', kwargs={'pk': self.users[0].id})
        questionnaire_url = reverse('questionnaire-detail',
                                    kwargs={'pk': self.questionnaires[0].id})

        # make new text field
        default_value = 'default text value'
        field = QuestionnaireField.objects.create(
            questionnaire=self.questionnaires[0], position=1,
            field_type='TXT', text_before='just field',
            default_val=default_value)

        # make test answer
        answer_data = {'questionnaire': questionnaire_url,
                       'respondent': respondent_url,
                       'field_values': [{'field': field.id}]}
        r = self.client.post(reverse('questionnaireanswer-list'), answer_data)
        self.assertEqual(r.status_code, 201)
        answer_id = r.json()['id']

        fval = FieldValue.objects.get(answer=answer_id, field=field.id)
        self.assertEqual(fval.value, default_value)

    def test_checkbox_value_can_be_either_true_or_false(self):
        self.client.force_login(self.users[0])
        respondent_url = reverse('user-detail', kwargs={'pk': self.users[0].id})
        questionnaire_url = reverse('questionnaire-detail',
                                    kwargs={'pk': self.questionnaires[0].id})

        # make new text field
        field = QuestionnaireField.objects.create(
            questionnaire=self.questionnaires[0], position=1,
            field_type='CHK', text_before='just field')

        def check_val(val, res):
            field_value = {'field': field.id, 'value': val}
            answer_data = {'questionnaire': questionnaire_url,
                           'respondent': respondent_url,
                           'field_values': [field_value]}
            r = self.client.post(reverse('questionnaireanswer-list'), answer_data)
            self.assertEqual(r.status_code, res, msg='Value is {}'.format(val))
            if r.status_code == 201:
                QuestionnaireAnswer.objects.get(id=r.json()['id']).delete()

        values_to_check = [('true', 201), ('false', 201), ('bad', 400)]
        for val, res in values_to_check:
            check_val(val, res)
