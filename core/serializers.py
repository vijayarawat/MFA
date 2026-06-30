from rest_framework import serializers
from .models import UserDetails
from django.contrib.auth.hashers import make_password, check_password
vijaya added some code to test the feature.

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        email = data.get('email')
        # print("Email is ",email)
        password = data.get('password')
        # print(password)
        try:
            user = UserDetails.objects.get(email=email)
        except:
            raise serializers.ValidationError('User does not exist')

        try:
            password_decode = check_password(password, user.password)
        except:
            raise serializers.ValidationError('Password did not matched')
        
        data['user'] = user
        return data