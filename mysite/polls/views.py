from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice

''' Old code: views as functions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse("Hello! You're at the polls index")
    #return HttpResponse(output)
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) # shortcut of last line

def anotherindex(request):
    return HttpResponse("Hello! You're at the polls from another index")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''
# New code: views as classes
# - ListView: “display a list of objects”
# - DetailView: “display a detail page for a particular type of object.”
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class NewQuestion(generic.ListView):
    model = Question
    template_name = 'polls/new_question.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Saving votes to database via Django API
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def create_question(request):   
    new_question = Question(question_text=request.POST['q_text'], pub_date=timezone.now())
    new_question.save()
    return HttpResponseRedirect(reverse('polls:index'))