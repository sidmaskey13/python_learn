from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.forms import  PollQuestionForm, PollChoiceForm
from .models import Question, Choice
# Create your views here.


def polls_index_view(request):
    queryset = Question.objects.order_by('-pub_date')[:5]
    context = {
        'object_list': queryset
    }

    return render(request,"polls/index.html", context)


def polls_show_view(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html', {'question': question})


def results(request,question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request,'polls/results.html', {'question': question})

def add_question_page(request):

    formQuestion = PollQuestionForm(request.POST or None)
    formChoice = PollChoiceForm(request.POST or None)

    if formQuestion.is_valid():
        que = formQuestion.save(commit=False)
        que.save()
        print(que.id)

    if formChoice.is_valid():
        cho = formChoice.save(commit=False)
        cho.question = que
        cho.save()
    else:  # invalid case
        # print(formChoice.is_valid())  # form contains data and errors
        print(formChoice.errors)

    context = {
        'formQ': formQuestion,
        'formC': formChoice,

    }

    return render(request,'polls/add_question.html',context)


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'polls/index.html')

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:polls-result',args=(question.id,)))



