from django.shortcuts import render, redirect, get_object_or_404
from .models import Reply, QandA
from .forms import ReplyForm, QandAForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):     # 메인 페이지에 가장 먼저 보여줄 것들
    return render(request, 'reservation/index.html')

def board(request):     # 필요한 사진과 정보를 올려둘 board
    return render(request, 'reservation/board.html')

def notice(request):    # 공지사항을 위해
    return render(request, 'reservation/notice.html')

def QandA_list(request):
    QandAs = QandA.objects.all()    
    context = {
        'QandAs' : QandAs
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
    form = ReplyForm()
    context = {
        'qanda':qanda,
        'form':form
    }
    return render(request, 'reservation/QandA_detail.html', context)

@require_POST
@login_required
def reply_create(request, qanda_pk):
    qanda = get_object_or_404(QandA, pk=qanda_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply=form.save(commit=False)
        reply.user = request.user
        reply.qanda = qanda
        reply.save()
    return redirect('reservation:QandA_detail',qanda.pk)

@login_required
def reply_delete(request, reply_pk, qanda_pk):
    reply = Reply.objects.get(pk=reply_pk)
    reply.delete()
    return redirect('reservation:QandA_detail',qanda_pk)