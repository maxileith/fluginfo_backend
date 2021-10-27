from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import OfferSeatmap, AmadeusBadRequest, AmadeusNothingFound
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class Seatmap(APIView):

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
    )
    @method_decorator(cache_page(1800))
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
        
        seatmap = OfferSeatmap(request.GET.get('id'), request.GET.get('segment'))
        try:
            return JsonResponse(
                data=seatmap.get(),
                status=HTTP_200_OK,
            )
        except AmadeusNothingFound:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )