from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import GuestMessage
import json

@csrf_exempt
def guestbook_api(request):
    if request.method == 'GET':
        messages = GuestMessage.objects.order_by('-written_at')
        data = [
            {'author': m.author, 'message': m.message, 'written_at': m.written_at.strftime('%Y-%m-%d %H:%M')}
            for m in messages
        ]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            author = body.get('author')
            message = body.get('message')
            if author and message:
                GuestMessage.objects.create(author=author, message=message)
                return JsonResponse({'success': True}, status=201)
            else:
                return JsonResponse({'error': 'Missing author or message'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
