from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination
	)

class JobLimitOffsetPagination(LimitOffsetPagination):
	default_limit=3
	max_limit=5

class JobPageNumberPagination(PageNumberPagination):
	page_size=3