from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import GuestMessage
import json

@csrf_exempt
def guestbook_api(request):
    if request.method == 'GET':
        messages = GuestMessage.objects.order_by('-written_at')
        data = [
            {
                'id': m.id,
                'author': m.author,
                'belonging': m.belonging,
                'message': m.message,
                'written_at': m.written_at.strftime('%Y-%m-%d %H:%M')
            }
            for m in messages
        ]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            author = body.get('author')
            belonging = body.get('belonging')
            message = body.get('message')
            if author and message:
                GuestMessage.objects.create(author=author, belonging=belonging, message=message)
                return JsonResponse({'success': True}, status=201)
            else:
                return JsonResponse({'error': 'Missing author or message'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    elif request.method == 'PUT':
        try:
            body = json.loads(request.body)
            message_id = body.get('id')
            new_message = body.get('message')
            new_belonging = body.get('belonging')
            if not message_id or not new_message:
                return JsonResponse({'error': 'Missing id or message'}, status=400)

            try:
                guest_message = GuestMessage.objects.get(id=message_id)
                guest_message.message = new_message
                if new_belonging is not None:
                    guest_message.belonging = new_belonging
                guest_message.save()
                return JsonResponse({'success': True})
            except GuestMessage.DoesNotExist:
                return JsonResponse({'error': 'Message not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
