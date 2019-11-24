from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def  Indexpage(request):
    return render(request, 'index.html')
def countpage(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    worddictionary = {}
    for word in wordList:
        if word  in worddictionary:
                worddictionary[word] +=1
        else:
            worddictionary[word] = 1
#    sortedWord = sorted(worddictionary.items(), key = operator.itemgetter(1),reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordList) , "worddictionary":sorted(worddictionary.items(), key=operator.itemgetter(1),reverse = True)})


def startagain(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request, 'contact.html')
