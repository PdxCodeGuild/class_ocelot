from django.shortcuts import render, get_object_or_404, reverse

from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, 'color': 'blue'}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    choice = Choice.objects.get(pk=1)
    print(choice.choice_text)
    print(choice.question.question_text)

    for choice in question.choice_set.all():
        print(choice.choice_text)




    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     print(request.POST)
#     print(request.POST['first_name'])
#     print(request.POST['last_name'])
#     print(request.POST['age'])
#     print(type(request.POST['age']))
#     return HttpResponse("You're voting on question %s." % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #selected_choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #print(reverse('polls:results', args=(question.id,)))
        #return HttpResponseRedirect(f'polls/{question.id}/results')
        #return HttpResponseRedirect('http://www.google.com')
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
