import traceback
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from amadeus_connector import AmadeusNothingFound, AmadeusServerError, AmadeusBadRequest
from fluginfo.settings import DEBUG, amadeus_connector
from schemas import airport_search_response_schema


class AirportSearch(APIView):

    serializer_class = None

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
        responses={
            HTTP_200_OK: airport_search_response_schema,
            HTTP_404_NOT_FOUND: OpenApiResponse(description="No airports matching the keyword were found."),
            HTTP_400_BAD_REQUEST: None,
            HTTP_503_SERVICE_UNAVAILABLE: OpenApiResponse(
                description="The internally used service provider has server problems."),
        },
    )
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
            airports = amadeus_connector.airport.search(request.GET.get('s'))
            return JsonResponse(
                data={
                    'data': airports,
                },
                status=HTTP_200_OK,
            )
        except AmadeusBadRequest:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        except AmadeusNothingFound:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
        except AmadeusServerError:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_503_SERVICE_UNAVAILABLE,
            )


class AirportDetails(APIView):

    serializer_class = None

    @extend_schema(
        deprecated=True,
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
            airport = amadeus_connector.airport.details(
                request.GET.get('iata'))
            return JsonResponse(
                data=airport,
                status=HTTP_200_OK,
            )
        except AmadeusBadRequest:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        except AmadeusNothingFound:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
        except AmadeusServerError:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_503_SERVICE_UNAVAILABLE,
            )
