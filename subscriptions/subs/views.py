from django.shortcuts import render, redirect
from subs.forms import SubsForm
from subs.models import Subs
from django.db.models import Sum


def subs(request):
    data = Subs.objects.filter(user=request.user).order_by('-start_date')
    sum_cost = Subs.objects.filter(user=request.user).aggregate(Sum('cost'))['cost__sum']
    return render(request, 'subs/subs.html', {'data': data, 'sum_cost': sum_cost})


def add_sub(request):
    error = ''
    if request.method == 'POST':
        data = request.POST.copy()
        data.update({'user': request.user.id})
        form = SubsForm(data)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('subs')
        else:
            error = 'Incorrect values'

    form = SubsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'subs/add-sub.html', data)
