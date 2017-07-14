from django.shortcuts import render, redirect
from .models import Worker
from django.core.exceptions import PermissionDenied
from .forms import SearchForm, UserForm, AssignForm


def test_view(request):

    form = SearchForm(request.POST, request.FILES)
    context = {'form': form, 'submit_message': 'Search'}

    form = UserForm(request.POST, request.FILES)
    context.update({'form2': form, 'submit_message2': 'Assign Work'})

    return render(request, "maintenance/maintenance.html", context)


def search_worker(request):

    if request.user.is_superuser:
        form = SearchForm(request.POST, request.FILES)
        context = {'form': form, 'submit_message': 'Search'}

        form = UserForm(request.POST, request.FILES)
        context.update({'form2': form, 'submit_message2': 'Assign Work'})

        try:
            query = request.GET.get('worker_type')
            if query != '\0':
                result = Worker.objects.filter(worker_type=query)
                context.update({'result': result})
        except (KeyError, ValueError, Worker.DoesNotExist,):
                return redirect("maintenance:test-view")

        return render(request, 'maintenance/maintenance.html', context)

    else:
        raise PermissionDenied


def assign_worker(request):

    if request.user.is_superuser:

        try:
            query = request.GET.get('user')
            if query != '\0':
                result = Worker.objects.get(user=query)
                form = AssignForm(request.POST, request.FILES, instance=result)
                if request.method == "POST":
                    if form.is_valid():
                        spots = form.save(commit=False)
                        spots.save()

                        return redirect("maintenance:test-view")
                else:
                    form = AssignForm(instance=result)

                return render(request, 'maintenance/maintenance_form.html', {'title_message': 'Assign Work to Worker',
                                                                             'submit_message': 'Update',
                                                                             'form': form})
        except (KeyError, ValueError, Worker.DoesNotExist,):
                return redirect("maintenance:test-view")

    else:
        raise PermissionDenied
