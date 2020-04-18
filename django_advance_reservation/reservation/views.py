from django.shortcuts import render, redirect

# Create your views here.

def index(request):     # 메인 페이지에 가장 먼저 보여줄 것들
    return render(request, 'reservation/index.html')

def board(request):     # 필요한 사진과 정보를 올려둘 board
    return render(request, 'reservation/board.html')

def notice(request):    # 공지사항을 위해
    return render(request, 'reservation/notice.html')