
from main import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers


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
    """Attendance"""
    data = models.Attendance.objects.all()
    serializer_datas = serializers.AttendanceCreateSerializer(data, many=True)
    return Response(serializer_datas.data)


