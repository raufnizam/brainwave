from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import StudentProfile, InstructorProfile

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(
        choices=[('student', 'Student'), ('instructor', 'Instructor')],
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'user_type']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')
        validated_data.pop('password2')
        
        user = User(**validated_data)
        user.set_password(password)
        
        if user_type == 'student':
            user.is_student = True
        elif user_type == 'instructor':
            user.is_instructor = True
            
        user.save()
        
        # Create profile based on user type
        if user.is_student:
            StudentProfile.objects.create(user=user)
        elif user.is_instructor:
            InstructorProfile.objects.create(user=user)
            
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            if not user:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Must include username and password")

        attrs['user'] = user
        return attrs
    
    


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['enrollment_date']
        read_only_fields = ['enrollment_date']

class InstructorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorProfile
        fields = ['specialization']

class UserProfileSerializer(serializers.ModelSerializer):
    student_profile = StudentProfileSerializer(read_only=True)
    instructor_profile = InstructorProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name',
            'bio',
            'profile_picture',
            'is_student', 
            'is_instructor',
            'student_profile',
            'instructor_profile'
        ]
        read_only_fields = ['id','username', 'is_student', 'is_instructor']
 
    
    