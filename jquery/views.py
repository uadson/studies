from http import server
from django.http import JsonResponse

from django.views import generic

from jquery.models import Username

from django.shortcuts import render

from jquery.serializers import UsernameSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class IndexView(generic.TemplateView):
    template_name = 'jquery/index.html'


class ListView(generic.TemplateView):
    template_name = 'jquery/list.html'


def get_form(request):
	return render(request, 'jquery/ajax.html')


@api_view(['GET'])
def get_username(request):
	usernames = Username.objects.all()
	serialized = UsernameSerializer(usernames, many=True)
	if usernames:
		return Response(serialized.data)
	else:
		return Response({})


def username_exists(request):
    data = {'msg': ''}
    if request.method == 'GET':
        username = request.GET.get('username')
        exists = Username.objects.filter(name=username).exists()
        if exists:
            data['msg'] = f'{username} already exists.'
        else:
            data['msg'] = f'{username} does not exists.'
    return JsonResponse(data)
