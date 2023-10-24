from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Jobs , AppliedJob
from .serializers import JobsSerializers, AppliedJobsSerializers
from django.core.files.storage import default_storage


@csrf_exempt
def jobsAPI(request, id=0):
    if request.method=='GET':
        job = Jobs.objects.all()
        job_serializer = JobsSerializers(job, many=True)
        return JsonResponse(job_serializer.data, safe=False)
    
    elif request.method == 'POST':
        job_data = JSONParser().parse(request)
        job_serializer = JobsSerializers(data=job_data)
        if job_serializer.is_valid():
            job_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        job_data = JSONParser().parse(request)
        job = Jobs.objects.get(id=job_data['id'])
        jobs_serializer = JobsSerializers(job, data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Updated Successfully!!" , safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    
    elif request.method == 'DELETE':
        job = Jobs.objects.get(id=id)
        job.delete()
        return JsonResponse("Deleted Successfully!!" , safe=False)
    


@csrf_exempt
def appliedJobsAPI(request, id=0):
    if request.method=='GET':
        job = AppliedJob.objects.all()
        job_serializer = AppliedJobsSerializers(job, many=True)
        return JsonResponse(job_serializer.data, safe=False)
    
    elif request.method == 'POST':
        job_data = JSONParser().parse(request)
        job_serializer = AppliedJobsSerializers(data=job_data)
        if job_serializer.is_valid():
            job = AppliedJob()
            job.name = job_data['name']
            job.email = job_data['email']
            job.job_id = job_data['job_id']
            job.resume = job_data['resume']
            job.phone = job_data['phone']
            job.gender = job_data['gender']
            job.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        job_data = JSONParser().parse(request)
        job = AppliedJob.objects.get(id=job_data['id'])
        jobs_serializer = AppliedJobsSerializers(job, data=job_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse("Updated Successfully!!" , safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    
    elif request.method == 'DELETE':
        job = AppliedJob.objects.get(id=id)
        job.delete()
        return JsonResponse("Deleted Successfully!!" , safe=False)