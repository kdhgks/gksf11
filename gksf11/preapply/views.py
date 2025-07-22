from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Application
import json

@csrf_exempt
def application_api(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            name = body.get('name')
            email = body.get('email')
            phone = body.get('phone')
            sessions = body.get('sessions', [])  # sessions는 선택

            if not all([name, email, phone]):
                return JsonResponse({'error': '이름, 이메일, 연락처는 필수입니다.'}, status=400)

            Application.objects.create(
                name=name,
                email=email,
                phone=phone,
                sessions=sessions
            )

            return JsonResponse({'success': True}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON 형식 오류'}, status=400)

    return JsonResponse({'error': '허용되지 않은 요청 방식입니다.'}, status=405)
