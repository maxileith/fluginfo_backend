from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from amadeus_connector import OfferDetails, AmadeusBadRequest, AmadeusNothingFound
from drf_spectacular.utils import extend_schema, OpenApiParameter


class Details(APIView):

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='id',
                description='the id of the offer (see "/offers/search")',
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
        ],
        auth=None,
        summary='Give me some details about an offer.',
    )
    def get(self, request):
        """
        This endpoint returns details of the matching offer.
        """
        if 'id' not in request.GET.dict().keys():
            return HttpResponse(
                content='',
                status=HTTP_400_BAD_REQUEST,
            )

        try:
            return JsonResponse(
                data=OfferDetails.get(request.GET.get('id')),
                status=HTTP_200_OK,
            )
        except AmadeusNothingFound:
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
