# I have created this file-Naman

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc=='on':
     analyzed=" "
     for char in djtext:
        if char not in punctuations:
            analyzed=analyzed+char
     params={'purpose':'remove punctuation','analyzed_text':analyzed}
     return render(request,'analyze.html',params)

    elif fullcaps=='on':
      analyzed=" "
      for char in djtext:
          analyzed=analyzed+char.upper()
      params = {'purpose': 'FULL CAPITIALIZE', 'analyzed_text': analyzed}
      return render(request,'analyze.html',params)

    elif newlineremover=='on':
        analyzed=" "
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    elif extraspaceremover=='on':
        analyzed=" "
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    else:

        return HttpResponse("Error")
