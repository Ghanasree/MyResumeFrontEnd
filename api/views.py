from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def contact_form(request):
    if request.method == 'POST':
        subject = request.data.get('subject', 'No Subject')
        message = request.data.get('message', '')
        from_email = request.data.get('email', '')
        send_mail(subject, message, from_email, ['djangoreact12@gmail.com'])
        return Response({'success': 'Email sent successfully'})
    return Response({'error': 'Invalid request'}, status=400)
