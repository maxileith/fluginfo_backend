from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import AmadeusBadRequest, AmadeusNothingFound, AvailabilitySeatmap
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from fluginfo.settings import CACHE_TIMEOUT


class Seatmap(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='flightNumber',
                description='The flight number to check the seatmap for.',
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
                        'The 1st of November 2021',
                        summary='The 1st of November 2021',
                        value='2021-11-01',
                    ),
                ],
            ),
        ],
        auth=None,
        summary='How does the seatmap looks like on a specific flight?',
    )
    @method_decorator(cache_page(CACHE_TIMEOUT))
    def get(self, request):
        """
        This endpoint returns a seatmap for the aircraft doing the
        given flight.
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
            s = AvailabilitySeatmap(
                flight_number=request.GET.get('flightNumber'),
                date=request.GET.get('date'),
            )
            seatmap = s.get()

            return JsonResponse(
                data=seatmap,
                status=HTTP_200_OK,
            )
        except AmadeusBadRequest:
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        except AmadeusNothingFound:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )