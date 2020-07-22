from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination
	)

class UserLimitOffsetPagination(LimitOffsetPagination):
	default_limit=5
	max_limit=5

class UserPageNumberPagination(PageNumberPagination):
	page_size=5