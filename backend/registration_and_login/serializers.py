from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Provider, Receiver, Volunteer

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['establishment_name', 'activity_type', 'commercial_registration_number', 'address', 'person_in_charge_full_name', 'person_in_charge_phone']

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = ['entity_name', 'registration_license_number', 'address', 'person_in_charge_full_name', 'person_in_charge_phone']

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'national_id_number', 'means_of_transportation', 'addresses']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class SignupSerializer(serializers.Serializer):
    user_type = serializers.ChoiceField(choices=['provider', 'receiver', 'volunteer'])
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    # Profile fields
    provider = ProviderSerializer(required=False)
    receiver = ReceiverSerializer(required=False)
    volunteer = VolunteerSerializer(required=False)
    
    def validate(self, data):
        user_type = data.get('user_type')
        
        if data.get(user_type) is None:
            raise serializers.ValidationError(f"{user_type} data is missing")
        
        return data
        
    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        user_data = {k: v for k, v in validated_data.items() if k in ['username', 'email', 'password']}
        user = User.objects.create_user(**user_data)

        if user_type == 'provider':
            Provider.objects.create(user=user, **validated_data['provider'])
        elif user_type == 'receiver':
            Receiver.objects.create(user=user, **validated_data['receiver'])
        elif user_type == 'volunteer':
            Volunteer.objects.create(user=user, **validated_data['volunteer'])

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User account is disabled.')
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include username and password.')
        return data
