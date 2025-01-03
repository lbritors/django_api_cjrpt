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
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid email or password')
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
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'departamento', 'curso', 'fotoPerfil', 'is_active', 'is_staff', 'senha']
        extra_kwargs = {
            'senha': {'write_only': True},
        }

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        validated_data['password'] = senha
        usuario = Usuario(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            password = validated_data.pop('senha')
            instance.set_password(password)
        return super().update(instance, validated_data)


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    disciplina_id = serializers.PrimaryKeyRelatedField(
        queryset=Disciplina.objects.all(),  # Verifica se a disciplina existe
        write_only=True
    )
    disciplinas = DisciplinaSerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = ['id', 'nome', 'departamento', 'disciplina_id', 'disciplinas']

    def create(self, validated_data):
        disciplinas_data = validated_data.pop('disciplina_id')
        professor = Professor.objects.create(**validated_data)
        professor.disciplinas.set([disciplinas_data])
        return professor

    def update(self, instance, validated_data):
        disciplina = validated_data.pop('disciplina_id', None)
        if disciplina:
            instance.disciplinas.set([disciplina])
        return super().update(instance, validated_data)


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

