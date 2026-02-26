from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from polls.forms import QuestionForm
from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class AllView(generic.ListView):
    model = Question
    template_name = "polls/all.html"
    context_object_name = "all_question_list"

    def get_queryset(self):
        return Question.objects.all()

class StatisticsView(generic.ListView):
    model = Question
    template_name = "polls/statistics.html"
    context_object_name = "all_question_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions_count"] = Question.objects.all().count()
        context["choices_count"] = Choice.objects.all().count()
        context["votes_count"] = 0
        for choice in Choice.objects.all():
            context["votes_count"] += choice.votes
        context["moy_votes_per_poll"] = round(context["votes_count"] / context["questions_count"], 2)
        context["popular_question"] = Question.most_popular_question()
        context["less_popular_question"] = Question.less_popular_question()
        context["last_question"] = Question.objects.order_by("pub_date").last()
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create( question_text=form.cleaned_data['question_text'], pub_date=form.cleaned_data['pub_date'])
            choices = [ form.cleaned_data['choice1'],form.cleaned_data['choice2'], form.cleaned_data['choice3'], form.cleaned_data['choice4'], form.cleaned_data['choice5']]
            for choice_text in choices:
                if choice_text:
                    Choice.objects.create( question=question,choice_text=choice_text,votes=0)
            return redirect('polls:index')
    else:
        form = QuestionForm()

    return render(request, 'polls/questionForm.html', {'form': form})