from rest_framework import serializers

from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        instance = getattr(self, 'instance', None)
        if instance and instance.cpf and attrs.get('cpf', False):
            raise serializers.ValidationError(
                "Não é possível alterar o cpf. Favor enviar o data sem o CPF."
            )
        age = attrs.get('age', 0)
        if instance is None and age < 18 or instance and age <= 17:
            raise serializers.ValidationError(
                "Não é possível salvar os dados, pois a idade mínima exigida "
                "é de 18 anos. Quando você fizer 18 anos, "
                "você pode tentar novamente."
            )

        return attrs

    class Meta:
        model = Candidate
        fields = '__all__'

