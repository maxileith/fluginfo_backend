from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from amadeus_connector import AmadeusNothingFound, Airport

class AirportSearch(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='s',
                description='string to search for',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'London',
                        summary='London',
                        value='London',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='Which airports match my keyword?',
    )
    @method_decorator(cache_page(1800))
    def get(self, request):
        """
        This endpoint returns data on airports that match
        the search input.
        """
        if 's' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            airports = Airport.search(request.GET.get('s'))
            return JsonResponse(
                data=airports,
                status=HTTP_200_OK,
            )
        except AmadeusNothingFound:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )


class AirportDetails(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='iata',
                description='iata of airport',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'München',
                        summary='München',
                        value='MUC',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='Give me details about an airport.',
    )
    @method_decorator(cache_page(86400))
    def get(self, request):
        """
        This endpoint returns data to the specified airport.
        """
        if 'iata' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            airport = Airport.details(request.GET.get('iata'))
            return JsonResponse(
                data=airport,
                status=HTTP_200_OK,
            )
        except AmadeusNothingFound:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
