from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Watering
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'watering/index.html'
    context_object_name = 'watering_list'

    def get_queryset(self):
        """Return all the latest watering."""
        return Watering.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Watering.objects.create(title=title)

    return redirect('watering:index')

def delete(request, watering_id):
    watering = get_object_or_404(Watering, pk=watering_id)
    watering.delete()

    return redirect('watering:index')

def update(request, watering_id):
    watering = get_object_or_404(Watering, pk=watering_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    watering.isCompleted = isCompleted

    watering.save()
    return redirect('watering:index')