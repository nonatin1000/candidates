from unittest.mock import MagicMock
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
import json


candidate_data = {
    "name": "Esdras Carvalho Rodrigues",
    "email": "esdrascarvalho@imhpicos.com.br",
    "cpf": "90943252091",
    "age": 28,
    "salary_claim": "3000.00",
    "is_immediate_availability_for_work": True
}

candidate_serializer_fields = [
    'id',
    'name',
    'cpf',
    'age',
    'email',
    'salary_claim',
    'is_immediate_availability_for_work'
]

RETURN_MOCK1 = {
    "id": 1,
    "name": "Esdras Carvalho Rodrigues",
    "email": "esdrascarvalho@imhpicos.com.br",
    "cpf": "90943252091",
    "age": 28,
    "salary_claim": "3000.00",
    "is_immediate_availability_for_work": True
}


MOCK2 = {
    "name": "Esdras Carvalho Rodrigues",
    "email": "esdrascarvalho@imhpicos.com.br",
    "cpf": "90943252091",
    "age": 28,
    "salary_claim": "3000.00",
}


RETURN_MOCK2 = {
    "id": 1,
    "name": "Esdras Carvalho Rodrigues",
    "email": "esdrascarvalho@imhpicos.com.br",
    "cpf": "90943252091",
    "age": 28,
    "salary_claim": "3000.00",
}


MOCK3 = {
    "time_to_retry": 30,
}


RETURN_MOCK3 = {
    'url': [
        ErrorDetail(
            string='Este campo é obrigatório.',
            code='required'
        )
    ]
}


MOCK4 = {
    "time_to_retry": "Ola"
}


RETURN_MOCK4 = {
    'url': [
        ErrorDetail(
            string='Este campo é obrigatório.',
            code='required'
        )
    ],
    'time_to_retry': [
        ErrorDetail(
            string='Um número inteiro válido é exigido.',
            code='invalid'
        )
    ]
}