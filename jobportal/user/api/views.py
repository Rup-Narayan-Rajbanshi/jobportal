from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	DestroyAPIView
	)
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)
from django.contrib.auth import get_user_model
from django.db.models import Q
from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer,
	UserSerializer,
	UserDetailSerializer
	)
from .pagination import UserLimitOffsetPagination, UserPageNumberPagination

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
	queryset=User.objects.all()
	serializer_class=UserCreateSerializer

class UserLoginAPIView(APIView):
	serializer_class=UserLoginSerializer
	permission_class=[AllowAny]

	def post(self, request, *args, **kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)

		if serializer.is_valid(raise_exception=True):
			new_data=serializer.data
			return Response(new_data,status=HTTP_200_OK)
		return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



class UserListAPIView(ListAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer
	pagination_class=UserPageNumberPagination
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields=['username','first_name','last_name']

	def get_queryset(self, *args, **kwargs):
		queryset_list=User.objects.all()
		query=self.request.GET.get('q')
		if query:
			queryset_list=User.objects.filter(
				Q(username__icontains=query)|
				Q(first_name__icontains=query)|
				Q(last_name__icontains=query)
				)
		return queryset_list

class UserDetailAPIView(RetrieveAPIView):
	queryset=User.objects.all()
	serializer_class=UserDetailSerializer
	lookup_field='username'

class UserUpdateAPIView(UpdateAPIView):
	queryset=User.objects.all()
	serializer_class=UserDetailSerializer
	lookup_field='username'

class UserDeleteAPIView(DestroyAPIView):
	queryset=User.objects.all()
	serializer_class=UserDetailSerializer
	lookup_field='username'