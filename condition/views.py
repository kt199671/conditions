from django.shortcuts import render
from django.shortcuts import redirect
from .models import Condition
from .forms import PostForm
from datetime import datetime,date
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from itertools import chain

User = get_user_model()

@login_required
def index(request,num=1):
    data = Condition.objects.all()
    data = data.filter(owner=request.user)
    page = Paginator(data,10)
    params = {
        'title': 'Condition TOP',
        'data': page.get_page(num),
    }
    return render(request, 'condition/index.html', params)

@login_required
def today(request):
    data = Condition.objects.all()
    data = data.filter(pub_date=date.today())
    data = data.order_by('owner__position')
    user = User.objects.all()
    posted_list = data.values_list('owner', flat=True)
    user_list = list(User.objects.values_list('id', flat=True))
    incomplete_list = list(set(posted_list)^set(user_list))
    incomplete_user = [User.objects.get(id=i).username for i in incomplete_list]
    if "superuser" in incomplete_user:
        incomplete_user.remove("superuser")
    params = {
        'title': 'Condition today',
        'data': data,
        'incomplete_user': incomplete_user,
        'user': user
    }
    return render(request, 'condition/today.html', params)

@login_required
def post(request):
    params = {
        'title': 'Condition POST',
        'form': PostForm(),
    }
    if (request.method == 'POST'):
        owner = request.user
        temperature = request.POST['temperature']
        conditioning = 'conditioning' in request.POST
        content = request.POST['content']
        pub_date = date.today()
        pub_time = datetime.now().time()
        data = Condition(owner=owner,temperature=temperature,conditioning=conditioning,\
                content=content,pub_date=pub_date,pub_time=pub_time)
        data.save()
        return redirect(to='url')
    return render(request, 'condition/post.html', params)

@login_required
def edit(request, num):
    params = {
        'title': 'Condition EDIT',
        'id':num,
        'form': PostForm(),
    }
    if (request.method == 'POST'):
        id = num
        owner = request.user
        temperature = request.POST['temperature']
        conditioning = 'conditioning' in request.POST
        content = request.POST['content']
        pub_date = date.today()
        pub_time = datetime.now().time()
        data = Condition(id=id,owner=owner, temperature=temperature, conditioning=conditioning, \
                         content=content, pub_date=pub_date, pub_time=pub_time)
        data.save()
        return redirect(to='url')
    return render(request, 'condition/edit.html', params)

@login_required
def delete(request, num):
    cond = Condition.objects.get(id=num)
    if (request.method == 'POST'):
        cond.delete()
        return redirect(to='url')
    params = {
        'title': 'Condition DELETE',
        'id':num,
        'obj': cond,
    }
    return render(request, 'condition/delete.html', params)
