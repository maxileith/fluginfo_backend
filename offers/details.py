import traceback
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.http.response import JsonResponse, HttpResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from amadeus_connector import AmadeusNothingFound
from fluginfo.settings import DEBUG, amadeus_connector
from schemas import offer_details_response_schema


class Details(APIView):

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
        ],
        auth=None,
        summary='Give me some details about an offer.',
        responses={
            HTTP_200_OK: offer_details_response_schema,
            HTTP_404_NOT_FOUND: OpenApiResponse(description="No flight there with the specified ID."),
        },
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
                data=amadeus_connector.offer_details.get(
                    request.GET.get('id')),
                status=HTTP_200_OK,
            )
        except AmadeusNothingFound:
            if DEBUG:
                traceback.print_exc()
            return HttpResponse(
                content='',
                status=HTTP_404_NOT_FOUND,
            )
