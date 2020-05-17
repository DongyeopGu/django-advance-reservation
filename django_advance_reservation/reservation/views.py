from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from accounts.models import User
from django.contrib import messages
from .models import Reply, QandA
from .forms import ReplyForm, QandAForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

def index(request):     # 메인 페이지에 가장 먼저 보여줄 것들
    users = User.objects.all()
    context= {
        'users':users
    }
    return render(request, 'reservation/index.html', context)

def board(request):     # 필요한 사진과 정보를 올려둘 board
    return render(request, 'reservation/board.html')

def notice(request):    # 공지사항을 위해
    return render(request, 'reservation/notice.html')

def QandA_list(request):
    QandAs = QandA.objects.order_by('-pk')    
    paginator = Paginator(QandAs, 4) #한 페이지 당 몇개 씩 보여줄 지 지정
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    reviews_all = get_list_or_404(QandA)
    total_count = len(reviews_all)
    total_page = total_count//4 + 1
    page_range = range(1,total_page+1)
    context = {
        'QandAs' : QandAs,
        'page_obj': page_obj,
        'page_range': page_range,
    }
    return render(request, 'reservation/QandA.html', context)

@login_required
def QandA_create(request):
    if request.method == 'POST':
        form = QandAForm(request.POST)
        if form.is_valid():
            QandA = form.save(commit=False)
            QandA.user = request.user
            QandA.save()
            return redirect('reservation:QandA_list')
    else:
        form = QandAForm()
    context = {
        'form' : form
    }
    return render(request, 'reservation/QandA_create.html', context)

@login_required    
def QandA_detail(request, qanda_pk):
    qanda = get_object_or_404(QandA, pk=qanda_pk)

    if qanda.user == request.user:
        form = ReplyForm()
        context = {
            'qanda':qanda,
            'form':form
        }
        return render(request, 'reservation/QandA_detail.html', context)
    else:
        messages.warning(request, '본인 글만 확인 가능합니다.')
        return redirect('reservation:QandA_list')

@login_required
def QandA_update(request, qanda_pk):
    qanda = get_object_or_404(QandA, pk=qanda_pk)
    if request.method == 'POST':
        form = QandAForm(request.POST, instance=qanda)
        if form.is_valid():
            qanda = form.save(commit=False)
            qanda.user = request.user
            qanda.save()
            return redirect('reservation:QandA_detail', qanda.pk)
    else:
        form = QandAForm(instance=qanda)
    context = {
        'form': form
    }
    return render(request, 'reservation/QandA_create.html', context)

@login_required
def QandA_delete(request, qanda_pk):
    qanda = get_object_or_404(QandA, pk=qanda_pk)
    if request.user == qanda.user:
        qanda.delete()
    return redirect('reservation:QandA_list')

        

@require_POST
@login_required
def reply_create(request, qanda_pk):
    qanda = get_object_or_404(QandA, pk=qanda_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply=form.save(commit=False)
        reply.user = request.user
        reply.QandA = qanda
        reply.save()
    return redirect('reservation:QandA_detail',qanda.pk)

@login_required
def reply_delete(request, reply_pk, qanda_pk):
    reply = Reply.objects.get(pk=reply_pk)
    reply.delete()
    return redirect('reservation:QandA_detail',qanda_pk)
