from rest_framework import serializers


from . import models as common_models

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = common_models.User
        fields = [
            'full_name',
            'email',
            'contact',
            'password',

        ]

        extra_kwargs = {
            'full_name': {'required': True},
            'email': {'required': True},
            'contact': {'required': True},
            'password': {'required': True},
            }

    def validate(self, data):
        
        if len(data['password']) < 8:
            raise serializers.ValidationError('Password Length is less than 8..')


        return data
