import traceback
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import AmadeusBadRequest, AmadeusNothingFound, AmadeusServerError
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from fluginfo.settings import DEBUG, amadeus_connector
from schemas import seatmap_response_schema


class Seatmap(APIView):

    serializer_class = None

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                description='the id of the offer (see "/offers/search")',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='segment',
                description='the id of the segment you want the seatmap for',
                required=True,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
        ],
        auth=None,
        summary='How do the seatmap look like?',
        responses={
            HTTP_200_OK: seatmap_response_schema,
            HTTP_404_NOT_FOUND: OpenApiResponse(description="There is no seatmap for the specified flight."),
            HTTP_400_BAD_REQUEST: None,
            HTTP_503_SERVICE_UNAVAILABLE: OpenApiResponse(
                description="The internally used service provider has server problems."),
        },
    )
    def get(self, request):
        """
        This endpoint returns the seatmaps matching an offer.
        """
        if 'id' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )
        if 'segment' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            seatmap = amadeus_connector.offer_seatmap.get(request.GET.get(
                'id'), request.GET.get('segment'))
            return JsonResponse(
                data=seatmap,
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
