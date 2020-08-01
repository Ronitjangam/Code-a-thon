from django.shortcuts import render
from .models import quotemodel,author,topic
import wikiquotes
# Create your views here.












#home page
#q=quotemodel(title="",author="",description="")

#fetching all the quotes foerm database
def quotes(request):
    q=quotemodel.objects.all()
    return render(request,"quotes.html",{"quote":q})

#fetching all the authors foerm database
def authors(request):
    q=author.objects.all()
    return render(request,"author.html",{"author":q})

#fetching all the topics foerm database
def topics(request):
    q=topic.objects.all()
    return render(request,"topic.html",{"topic":q})



#fetching all the quotes frmo database of specific author
def quoteauthor(request):
    a=request.GET.get("id")

    q=quotemodel.objects.filter(author_id=a)
    print(q)
    return render(request,"qa.html",{"qa":q})



#fetching all the quotes frmo databaseof specific topic
def quotetopic(request):
    a=request.GET.get("id")

    q=quotemodel.objects.filter(topic_id=a)
    print(q)
    return render(request,"ta.html",{"ta":q})