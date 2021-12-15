from django.contrib.auth import get_user_model
from unittest import TestCase
from candidates.candidate.models import Candidate
from candidates.candidate.serializers import CandidateSerializer
from candidates.candidate.tests import mocks
from django.test import Client
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json

user = get_user_model


class TestCandidateTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        user = User.objects.get(username="nonato")
        self.client.force_authenticate(user)
        self.candidate = Candidate.objects.create(
            name="Esdras",
            email="esdras@gmail.com.br",
            cpf="90943252095",
            age=18,
            salary_claim="3000.00",
            is_immediate_availability_for_work=True
        )
        self.serializer = CandidateSerializer(instance=self.candidate)

    def test_error_authentication(self):
        c = Client()
        response = c.post(
            '/token/',
            data={
                'username': 'teste',
                'password': 'teste'
            }
        )
        self.assertEqual(response.status_code, 401)

    def test_candidate_serializer_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(mocks.candidate_serializer_fields)
        )

    def test_get_and_filter_candidate(self):
        url = '/candidate/candidates/'
        response = self.client.get(url+'1000/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get(url+'?age_lte=18')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url+'?name=Esdras')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            url+'?email=agathavitoriaalves_@3dmaker.com.br'
        )
        self.assertEqual(response.status_code, 200)

    def test_update_candidate(self):
        url = '/candidate/candidates/11/'
        data = dict(
            age=52
        )
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_error_update_candidate(self):
        url = '/candidate/candidates/11/'
        data = dict(
            age=17
        )
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 400)
        data = dict(
            cpf="07952939688"
        )
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, 400)

    def test_post_candidate(self):
        url = '/candidate/candidates/'
        data = dict(
            name="Conceição Carvalho",
            email="mariacarvalhoadm@gmail.com",
            cpf="90943252085",
            age=33,
            salary_claim="1200.00",
            is_immediate_availability_for_work=True
        )
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 201)

    def test_error_post_candidate(self):
        url = '/candidate/candidates/'
        data = dict()
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 400)

    def test_delete_candidate(self):
        candidate = Candidate.objects.get(
            cpf="90943252085",
            email="mariacarvalhoadm@gmail.com"
        )
        print("candidate", candidate.id)
        url = f'/candidate/candidates/{candidate.id}/'
        data = dict()
        response = self.client.delete(url, data=data)
        self.assertEqual(response.status_code, 204)

    def test_error_delete_candidate(self):
        url = '/candidate/candidates/1000/'
        data = dict()
        response = self.client.delete(url, data=data)
        self.assertEqual(response.status_code, 404)

    def test_candidate_serializer_get_age(self):
        data = self.serializer.data
        serialized_age = data['age']
        self.assertEqual(serialized_age, 18)

    def test_candidate_serializer_error_age(self):
        data = self.serializer.data
        serialized_age = data['age']
        self.assertNotEqual(serialized_age, 17)

    def test_candidate_equals_cpf_and_email(self):
        data = self.serializer.data
        serialized_cpf = data['cpf']
        serialized_email = data['email']
        self.assertEqual(serialized_cpf, self.candidate.cpf)
        self.assertEqual(serialized_email, self.candidate.email)

    def tearDown(self):
        User.objects.filter(username="api", email="api@admin.com").delete()
        Candidate.objects.filter(
            cpf="90943252095",
            email="esdras@gmail.com.br"
        ).delete()

