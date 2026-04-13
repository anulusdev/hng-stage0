from django.http import JsonResponse
import requests
from datetime import datetime, timezone


def classify_name(request):
    if request.method != 'GET':
        return JsonResponse(
            {'status': 'error', 'message': 'Method not allowed'},
            status=405
        )
    name = request.GET.get('name', '').strip()

    if not name:
        return JsonResponse(
            {'status': 'error', 'message': 'name parameter is required'},
            status=400
        )

    if not isinstance(name, str) or any(char.isdigit() for char in name):
        return JsonResponse(
            {'status': 'error', 'message': 'name must be a valid string'},
            status=422
        )
    
    try:
        response = requests.get(
            'https://api.genderize.io',
            params={'name': name},
            timeout=5
        )
        response.raise_for_status()
        genderize_data = response.json()

    except requests.exceptions.Timeout:
        return JsonResponse(
            {'status': 'error', 'message': 'Genderize API timed out'},
            status=502
        )
    except requests.exceptions.RequestException:
        return JsonResponse(
            {'status': 'error', 'message': 'Failed to reach Genderize API'},
            status=502
        )
    
    gender = genderize_data.get('gender')
    count = genderize_data.get('count', 0)

    if gender is None or count == 0:
        return JsonResponse(
            {'status': 'error', 'message': 'No prediction available for the provided name'},
            status=400
        )

    probability = genderize_data.get('probability', 0)
    sample_size = count

    is_confident = probability >= 0.7 and sample_size >= 100

    processed_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    return JsonResponse({
        'status': 'success',
        'data': {
            'name': name,
            'gender': gender,
            'probability': probability,
            'sample_size': sample_size,
            'is_confident': is_confident,
            'processed_at': processed_at
        }
    }, status=200)