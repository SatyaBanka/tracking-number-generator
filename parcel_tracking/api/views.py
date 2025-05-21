from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from datetime import datetime
from .utils import generate_tracking_number
from .models import TrackingNumber

class NextTrackingNumberView(APIView):
    def get(self, request):
        params = request.query_params
        required_fields = [
            'origin_country_id',
            'destination_country_id',
            'weight',
            'created_at',
            'customer_id',
            'customer_name',
            'customer_slug'
        ]

        for field in required_fields:
            if field not in params:
                return Response({"error": f"Missing required parameter: {field}"}, status=status.HTTP_400_BAD_REQUEST)

        # Extract parameters
        origin = params['origin_country_id']
        destination = params['destination_country_id']
        weight = params['weight']
        created_at = params['created_at']
        customer_id = params['customer_id']
        customer_name = params['customer_name']
        customer_slug = params['customer_slug']

        # Retry up to 5 times in case of collision
        for _ in range(5):
            tracking_number = generate_tracking_number(
                origin_country_id=origin,
                destination_country_id=destination,
                weight=weight,
                created_at=created_at,
                customer_id=customer_id,
                customer_name=customer_name,
                customer_slug=customer_slug
            )
            try:
                record = TrackingNumber.objects.create(tracking_number=tracking_number)
                return Response({
                    "tracking_number": record.tracking_number,
                    "created_at": record.created_at.isoformat()
                }, status=status.HTTP_200_OK)
            except IntegrityError:
                # Retry with a new timestamp
                created_at = datetime.utcnow().isoformat()

        return Response({"error": "Failed to generate unique tracking number after retries."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
