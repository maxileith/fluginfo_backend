from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import AmadeusBadRequest, AmadeusNothingFound, StatusTimings, AmadeusServerError
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
import traceback
from fluginfo.settings import DEBUG


class Timings(APIView):

    serializer_class = None

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='flightNumber',
                description='The flight number to check the delay for.',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'LH438',
                        summary='LH438',
                        value='LH438',
                    ),
                ],
            ),
            OpenApiParameter(
                name='date',
                description='the date on which the flight will depart. Dates are specified in the ISO 8601 YYYY-MM-DD format, e.g. 2017-12-25',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'The 1st of November 2021',
                        summary='The 1st of November 2021',
                        value='2021-11-01',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='Delay of a flight.',
    )
    def get(self, request):
        """
        This endpoint returns the current delay of a flight.
        class.
        """
        if 'flightNumber' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        if 'date' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            timings = StatusTimings.get(
                flight_number=request.GET.get('flightNumber'),
                date=request.GET.get('date'),
            )

            return JsonResponse(
                data=timings,
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
