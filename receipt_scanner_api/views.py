from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST', ])
def scan_products(request):
    try:
        image = request.data.get('image', None)
        print(image)

        return Response({'products': {'mere': 5.63, 'lapte': 5.30}, 'total': 10.93})

        # return Response({'has_error': 'false'}, status=status.HTTP_200_OK)

    except:
        return Response({'has_error': 'true'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', ])
def api_info(request):
    return Response({'methods': {'/scan_products': {'input': 'receipt image', 'output': 'products as JSON'}}}, status=status.HTTP_200_OK)