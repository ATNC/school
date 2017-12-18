import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Child, Journal


class ChildAndJournalTest(APITestCase):

    def setUp(self):
        self.create_list_child_url = reverse('child_list_or_create')
        Child.objects.bulk_create([
            Child(
                name=f'Child {item}',
                gender='B',
                birthday=datetime.date(2010, 1, item)
            )
            for item in range(1, 11)
        ])
        self.test_child = Child.objects.latest('id')
        self.test_journal_record = Journal.objects.create(
            bring_time=datetime.datetime.now(),
            child=self.test_child
        )

    def test_create_child(self):
        child_data = {
            'name': 'Vasia',
            'gender': 'B',
            'birthday': datetime.date(2010, 1, 1),


        }
        response = self.client.post(
            self.create_list_child_url,
            child_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('name'), child_data.get('name'))

    def test_list_of_child(self):
        response = self.client.get(
            self.create_list_child_url
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_list_of_learn_child(self):
        self.test_child.learn = True
        self.test_child.save()
        response = self.client.get(
            self.create_list_child_url,
            data={'learn': True}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.create_list_child_url,
            data={'learn': False}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 9)

    def test_edit_child(self):
        edit_data = {
                'name': 'Changed name'
            }
        edit_url = reverse(
            'children_edit_info',
            kwargs={'pk': self.test_child.id}
        )
        response = self.client.patch(
            edit_url,
            data=edit_data
        )
        self.test_child.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.test_child.name, edit_data.get('name'))

    def test_add_parents(self):
        parents_url = reverse(
            'children_add_parents',
            kwargs={'pk': self.test_child.id}
        )
        parents_data = {
            'mother': 'Mother name',
            'father': 'Father name',
        }
        response = self.client.put(parents_url, data=parents_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_journal_record(self):
        journal_url = reverse('journal_add_record')
        journal_data = {
            'bring_time': '2017-12-12 12:12',
            'child_id': self.test_child.id
        }
        response = self.client.post(journal_url, data=journal_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_journal_record(self):
        journal_url = reverse('journal_edit_record', kwargs={'pk': self.test_journal_record.id})
        journal_data = {
            'pick_up_time': '2017-12-12 12:12',
        }
        response = self.client.patch(journal_url, data=journal_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)









# coverage run manage.py test api.api_user.tests.test_api_user.UserUpdatedData.test_resend_phone_code # не валідний






