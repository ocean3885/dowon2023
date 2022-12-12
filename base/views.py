from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory,modelform_factory
from .forms import JmSubmitForm, JmPersonForm
from .models import Submit, Person

def home(request):
    return render(request, 'base/home.html')

def sub_intro(request):
    return render(request, 'base/sub_intro.html')

def submit_jm(request):
    if request.method == "POST":
        form1 = JmSubmitForm(request.POST)
        form2 = JmPersonForm(request.POST)
        if all([form1.is_valid(),form2.is_valid()]):
            obj = form1.save(commit=False)
            obj.category = "jm"
            obj.save()
            person = form2.save(commit=False)
            person.submit = obj
            person.save()
            context = {'submit':obj,'person':person}
            return render(request,'base/submit_complete.html',context)
    form1 = JmSubmitForm()
    form2 = JmPersonForm()
    context = {'form1': form1, 'form2':form2}
    return render(request,'base/submit_jm.html', context)

def edit_submit_jm(request, pk):
    obj1 = get_object_or_404(Submit, id=pk)
    obj2 = Person.objects.filter(submit__id=pk).first()
    form1 = JmSubmitForm(request.POST or None, instance=obj1)
    form2 = JmPersonForm(request.POST or None, instance=obj2)
    context = {
        'form1': form1,
        'form2': form2,
        'submit': obj1,
        'person': obj2
        }
    if all([form1.is_valid(),form2.is_valid()]):
        parent = form1.save(commit=False)
        parent.save()
        child = form2.save(commit=False)
        child.submit = parent
        child.save()
        return render(request,'base/submit_edit_complete.html',context)
    
    return render(request,'base/submit_jm.html', context)


def find_submit(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        f_number = request.POST.get('f_number')
        f_submit = Submit.objects.get(name=f_name, phonnumber=f_number)
        context = { 'f_submit': f_submit}
        return render(request,'base/submit_check.html', context)

    return render(request,'base/find_submit.html')







# def edit_submit_jm(request, pk):
#     obj = get_object_or_404(Submit, id=pk)
#     form = JmSubmitForm(request.POST or None, instance=obj)
#     PersonFormset = modelformset_factory(Person, form=PersonForm, extra=0, can_delete=True)
#     persons = obj.persons.all()
#     formset = PersonFormset(request.POST or None, queryset=persons)
#     context = {
#         'form': form,
#         'formset': formset,
#         'obj': obj,
#         'persons':persons
#         }
#     if all([form.is_valid(),formset.is_valid()]):
#         parent = form.save(commit=False)
#         parent.save()
#         for form in formset:
#             child = form.save(commit=False)
#             if form.cleaned_data["DELETE"]:
#                 child.delete()
#             else:
#                 child.submit = parent
#                 child.save()
#         return render(request,'base/submit_complete.html',context)
    
#     return render(request,'base/submit_jm.html', context)