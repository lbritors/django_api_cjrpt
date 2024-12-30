from rest_framework import serializers
from .models import Usuario, Professor, Disciplina, Avaliacao, Comentario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = '__all__'



class AvaliacaoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    disciplina = DisciplinaSerializer(read_only=True)

    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='usuario', write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(), source='professor', write_only=True)
    disciplina_id = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all(), source='disciplina', write_only=True)

    class Meta:
        model = Avaliacao
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    avaliacao = AvaliacaoSerializer(read_only=True)

    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='usuario', write_only=True)
    avaliacao_id = serializers.PrimaryKeyRelatedField(queryset=Avaliacao.objects.all(), source='avaliacao', write_only=True)

    class Meta:
        model = Comentario
        fields = '__all__'

