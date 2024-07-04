from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            middle_name=validated_data.get('middle_name'),
            telegram=validated_data.get('telegram'),
            birth_date=validated_data.get('birth_date'),
            started_work=validated_data.get('started_work'),
            supervisor=validated_data.get('supervisor'),
            raiting=validated_data.get('raiting'),
            block=validated_data.get('block', False), 
            avatar=validated_data.get('avatar'),
            job=validated_data.get('job'),
        )
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance,attr,value)
        instance.save()
        return instance
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)