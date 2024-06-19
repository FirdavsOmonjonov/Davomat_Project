from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer
from main import models


class StaffListSerializer(ModelSerializer):
    """Serializer for staff list"""
    class Meta:
        model = models.Staff
        fields = ['first_name', 'last_name', 'staff_position']


class StaffDetailSerializer(ModelSerializer):
    """Serializer for staff detail"""
    class Meta:
        model = models.Staff
        fields = '__all__'

class AttendanceSerializer(ModelSerializer):
    """davomat"""
    class Meta:
        model = models.Attendance
        fields = ['staff']