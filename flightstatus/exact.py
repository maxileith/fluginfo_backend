from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import AmadeusBadRequest, AmadeusNothingFound, StatusExact, AmadeusServerError
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from rest_framework import fields
import traceback
from fluginfo.settings import DEBUG
from schemas import status_exact_response_schema


class Exact(APIView):

    serializer_class = None

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='flightNumber',
                description='The flight number to check the availability for.',
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
                description='the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the ISO 8601 YYYY-MM-DD format, e.g. 2017-12-25',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
                examples=[
                    OpenApiExample(
                        'The 1st of March 2022',
                        summary='The 1st of March 2022',
                        value='2022-03-01',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='How many seats are available on a specific flight?',
        responses={
            HTTP_200_OK: status_exact_response_schema,
            HTTP_404_NOT_FOUND: OpenApiResponse(description="There are no availability information for the specified flight."),
            HTTP_400_BAD_REQUEST: None,
            HTTP_503_SERVICE_UNAVAILABLE: OpenApiResponse(
                description="The internally used service provider has server problems."),
        },
    )
    def get(self, request):
        """
        This endpoint return the number of seats that are available
        on a specific flight. The number of seats is categorized by
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
            status = StatusExact.get(
                flight_number=request.GET.get('flightNumber'),
                date=request.GET.get('date'),
            )

            return JsonResponse(
                data=status,
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
