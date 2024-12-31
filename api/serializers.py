from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario, Professor, Disciplina, Avaliacao, Comentario
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password')
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password")

        data['user'] = user
        return data

    def create(self, validated_data):
        user = validated_data.get('user')
        refresh = RefreshToken.for_user(user)
        return {
            'access_token': str(refresh.access_token),
            'id': user.id
        }


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('senha')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario


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

