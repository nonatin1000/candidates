from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django.db.models.expressions import Exists, OuterRef, Subquery
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from candidates.candidate.serializers import CandidateSerializer
from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Candidate
from .filters import CandidateFilter


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = CandidateFilter