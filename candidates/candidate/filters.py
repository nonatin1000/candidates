from django_filters import rest_framework as filters
from .models import Candidate


class CandidateFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    age_lte = filters.NumberFilter(field_name="age", lookup_expr="lte")
    age_gte = filters.NumberFilter(field_name="age", lookup_expr="gte")

    class Meta:
        model = Candidate
        fields = [
            "name",
            "age_lte",
            "age_gte",
            "email",
            "cpf",
            "salary_claim",
            "is_immediate_availability_for_work"
        ]
