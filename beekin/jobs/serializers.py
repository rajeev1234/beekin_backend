from rest_framework import serializers
from .models import Jobs , AppliedJob

class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'



class AppliedJobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppliedJob
        fields = '__all__'