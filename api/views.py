from django.shortcuts import render
from django.utils import timezone
from main import models
from . import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


@api_view(['GET'])
def staff_list(request):
    """Staff list"""
    data = models.Staff.objects.all()
    serializer_datas = serializers.StaffListSerializer(data, many=True)
    return Response(serializer_datas.data)


@api_view(['GET'])
def staff_detail(request, id):
    """Staff detail"""
    data = models.Staff.objects.get(id=id)
    serializer_datas = serializers.StaffDetailSerializer(data)
    return Response(serializer_datas.data)


@api_view(['POST'])
def attendance_create(request):
    """Davomat yaratilishi va yangilanishi"""
    try:
        worker_id = request.data.get('staff')
        last_attendance = models.Attendance.objects.filter(staff=staff_id).order_by('-id').first()
        if not last_attendance or last_attendance.gone_time:
            models.Attendance.objects.create(
                staff_id=staff_id,
                come_time=timezone.now(),
                gone_time=None
            )
        else:
            if last_attendance.gone_time is None:
                last_attendance.gone_time = timezone.now()
                last_attendance.save()

        return Response({'success': True})
    except:
        return Response({'success': False})