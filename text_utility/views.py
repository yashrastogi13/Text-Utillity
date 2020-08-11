# i have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index (request) :
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if removepunc != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and newlineremover != 'on':
        params= {'analyzed_text': djtext}
        return render(request,'analyze.html', params)

    return render(request,'analyze.html', params)