import json
import sys
sys.path.append(r'C:\Users\Admin\PycharmProjects\course2_work\src\server\tgbot_app')
from ..tgbot_app.my_stuff.controller import Controller
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def handle_request(request):
    if request.method == 'POST':
        try:
            request_body = json.loads(request.body)
            Controller.handle_request(request_body)
        except Exception as e:
            print(str(e))

        return HttpResponse('', status=200)

    else:
        return Http404
