from rest_framework import viewsets
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, filters

# API Views
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

class ApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Application.objects.select_related('job', 'user')
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

class PublicJobListView(generics.ListAPIView):
    queryset = Job.objects.filter(status=True)
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location']
    search_fields = ['title', 'description']

class ApplyJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job_id = self.request.data.get('job')
        if Application.objects.filter(user=self.request.user, job_id=job_id).exists():
            raise ValidationError("You have already applied for this job.")
        serializer.save(user=self.request.user)

class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)



# UI Views
def job_list_view(request):
    location = request.GET.get('location')
    min_salary = request.GET.get('min_salary')
    jobs = Job.objects.filter(status='open')

    if location:
        jobs = jobs.filter(location__icontains=location)
    if min_salary:
        jobs = jobs.filter(salary__gte=min_salary)

    return render(request, 'job_list.html', {
        'jobs': jobs,
        'location': location,
        'min_salary': min_salary,
    })

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if Application.objects.filter(job=job, user=request.user).exists():
        return redirect('my_applications')
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            # messages.success(request, "Application submitted successfully.")
            return redirect('my_applications')
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {'form': form, 'job': job})

@login_required
def my_applications_view(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'my_applications.html', {'applications': applications})

def user_login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('job_list')
        else:
            error = 'Invalid username or password.'

    return render(request, 'user_login.html', {'error': error})

def user_logout_view(request):
    logout(request)
    return redirect('user_login')
