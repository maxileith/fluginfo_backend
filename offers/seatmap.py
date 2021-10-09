from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
import amadeus_connector
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample


class Seatmap(APIView):

    def get(self, request):
        return JsonResponse(
            data={},
            status=HTTP_200_OK,
        )
