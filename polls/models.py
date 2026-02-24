import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"{self.question_text[:20]} ({self.pub_date})"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_choices(self):
        choices = self.choice_set.all()
        total_votes = sum(choice.votes for choice in choices)
        results = []
        for choice in choices:
            proportion = (choice.votes / total_votes) * 100
            results.append((choice.choice_text, choice.votes, proportion))
        return results

    def get_max_choice(self):
        choices = self.choice_set.all()
        if not choices:
            return None
        max_choice = max(choices, key=lambda c: c.votes)
        return max_choice.choice_text

    def age(self):
        current_year = timezone.now().year
        return current_year - self.pub_date.year

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_ordering = ("pub_date",)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text[:20]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes")
    list_filter = ["question"]
    search_fields = ["choice_text"]
    list_ordering = ("question",)


