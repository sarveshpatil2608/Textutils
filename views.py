from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("<h1>Sarvesh Patil</h1>")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', "off")
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # analyzed = djtext

        params = {'purpose': 'Removed punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'New lines removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = len(djtext)

        params = {'purpose': 'character count', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on" ):
        return HttpResponse("please select any operation and try again.")

    return render(request, 'analyze.html', params)
