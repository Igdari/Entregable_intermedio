from django.shortcuts import render

from django.http import HttpResponse

from plans.models import Plans
from plans.forms import PlanForm

def add_plan(request):
    if request.method == 'GET':
        context = {
            'form': PlanForm()
        }

        return render(request, 'plans/add_plan.html', context=context)

    elif request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            Plans.objects.create(
                name=form.cleaned_data['Nombre'],
                cost=form.cleaned_data['Costo'],
            )
            context = {
                'message': 'Plan añadido Correctamente'
            }
            return render(request, 'plans/add_plan.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': PlanForm()
            }
            return render(request, 'plans/add_plan.html', context=context)

def list_plans(request):
    if 'search' in request.GET:
        search = request.GET['search']
        plans = Plans.objects.filter(name__icontains=search)
    else:
        plans = Plans.objects.all()
    context = {
        'plans':plans,
    }
    return render(request, 'plans/list_plans.html', context=context)
