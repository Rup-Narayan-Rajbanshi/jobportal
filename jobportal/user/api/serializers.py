from rest_framework.serializers import (
	ModelSerializer,
	EmailField,
	CharField,
	HyperlinkedIdentityField
	)
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
User = get_user_model()

class UserCreateSerializer(ModelSerializer):
	email=EmailField(label='Email Address')
	email2=EmailField(label='Confirm Email')
	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email',
			'email2',
			'password',
			]
		extra_kwargs={"password":
						{"write_only":True}
					}

	def create(self, validated_data):
		username=validated_data['username']
		first_name=validated_data['first_name']
		last_name=validated_data['last_name']
		email=validated_data['email']
		password=validated_data['password']
		user_obj=User(username=username,
					first_name=first_name,
					last_name=last_name,
					email=email,
					password=password
					)
		user_obj.set_password(password)
		user_obj.save()

		return validated_data
		

	def validate_email2(self, value):
		data=self.get_initial()
		email1=data.get('email')
		email2=value
		if email1 != email2:
			raise serializers.ValidationError("Email must match")

		return value

class UserLoginSerializer(ModelSerializer):
	token=CharField(allow_blank=True,read_only=True)
	username=CharField(required=False, allow_blank=True)
	email=EmailField(label='Email Address',required=False, allow_blank=True)

	class Meta:
		model=User
		fields=[
			'username',
			'email',
			'password',
			'token',
			]
		extra_kwargs={"password":
						{"write_only":True}
					} 

	def validate(self,data):
		user_obj=None
		email=data.get('email',None)
		username=data.get('username',None)
		password=data['password']
		if not email and not username:
			raise serializers.ValidationError('A username or email is required to login')
		user=User.objects.filter(
			Q(username=username)|
			Q(email=email)
			).distinct()
		user=user.exclude(email__isnull=True).exclude(email__iexact=' ')
	
		if user.exists() and user.count() == 1:
			user_obj=user.first()
		else:
			raise serializers.ValidationError('This Username or email is not valid')

		if user_obj:
			if not user_obj.check_password(password):
				raise serializers.ValidationError("Incorrect credentials")

		data["token"]="Some Randon Token "
		return data

class UserSerializer(ModelSerializer):
	url=HyperlinkedIdentityField(
		view_name='account-api:detail',
		lookup_field='username'
		)
	class Meta:
		model=User
		fields=[
			'url',
			'username',
			'first_name',
			'last_name',
			'email',
			'id',
			]

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model=User
		fields=[
			'username',
			'first_name',
			'last_name',
			'email',
			]