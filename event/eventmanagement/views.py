from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import status

from django.db.models import Q

@api_view(['GET'])
def get_events(request):
    title_query = request.query_params.get('title', '')

    if title_query:
        events = Event.objects.filter(title__icontains=title_query)
    else:
        events = Event.objects.all()

    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def event_detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=204)

# Similar functions for Registration API views...
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def registration_list(request):
    if request.method == 'GET':
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)