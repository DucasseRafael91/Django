2.2.2.2

1:

from polls.models import Question

for question in Question.objects.all():
    print(f"Titre: {question.question_text} Date de Publication {question.pub_date}\n")

Titre: What's up? Date de Publication2026-02-23 11:55:04.445632+00:00

Titre: Quel age as tu ? Date de Publication2026-02-17 12:20:35+00:00

Titre: Fait il beau Date de Publication2026-02-02 12:22:43+00:00

Titre: Ou habites tu Date de Publication2026-01-09 12:24:07+00:00

Titre: Capitale de la France Date de Publication2026-02-04 12:26:31+00:00

Titre: Quel est la couleur du cheval blanc d Henry IV Date de Publication2026-02-09 12:27:48+00:00


2:

from polls.models import Question
from django.utils import timezone

current_year = timezone.now().year
current_month = timezone.now().month
current_day = timezone.now().day

print("Tri par Année")
for question in Question.objects.filter(pub_date__year=current_year):
    print(f"Titre: {question.question_text} - Date de Publication: {question.pub_date}\n")

print("Tri par Mois")
for question in Question.objects.filter(pub_date__month=current_month):
    print(f"Titre: {question.question_text} - Date de Publication: {question.pub_date}\n")

Tri par Année
Titre: What's up? - Date de Publication: 2026-02-23 11:55:04.445632+00:00

Titre: Quel age as tu ? - Date de Publication: 2026-02-17 12:20:35+00:00

Titre: Fait il beau - Date de Publication: 2026-02-02 12:22:43+00:00

Titre: Ou habites tu - Date de Publication: 2026-01-09 12:24:07+00:00

Titre: Capitale de la France - Date de Publication: 2026-02-04 12:26:31+00:00

Titre: Quel est la couleur du cheval blanc d Henry IV - Date de Publication: 2026-02-09 12:27:48+00:00

Tri par Mois
Titre: What's up? - Date de Publication: 2026-02-23 11:55:04.445632+00:00

Titre: Quel age as tu ? - Date de Publication: 2026-02-17 12:20:35+00:00

Titre: Fait il beau - Date de Publication: 2026-02-02 12:22:43+00:00

Titre: Capitale de la France - Date de Publication: 2026-02-04 12:26:31+00:00

Titre: Quel est la couleur du cheval blanc d Henry IV - Date de Publication: 2026-02-09 12:27:48+00:00


3

from polls.models import Question

question = Question.objects.get(pk=1)
print(f"Titre: {question.question_text} - Date de Publication: {question.pub_date}\n")

Titre: What's up? - Date de Publication: 2026-02-23 11:55:04.445632+00:00




4 et 5 et 11


from polls.models import Question

for question in Question.objects.all():
    print(f"Titre: {question.question_text}")
    print(f"Date de Publication: {question.pub_date}")
    print(f"Publié Récemment: {question.was_published_recently()}")

    for choice in question.choice_set.all():
        print(f"  - Choix: {choice.choice_text} (Votes: {choice.votes})")

    print("\n")


7

from polls.models import Question

for question in Question.objects.order_by("-pub_date"):
    print(f"{question.question_text} - {question.pub_date}")

What's up? - 2026-02-23 11:55:04.445632+00:00
Quel age as tu ? - 2026-02-17 12:20:35+00:00
Quel est la couleur du cheval blanc d Henry IV - 2026-02-09 12:27:48+00:00
Capitale de la France - 2026-02-04 12:26:31+00:00
Fait il beau - 2026-02-02 12:22:43+00:00
Ou habites tu - 2026-01-09 12:24:07+00:00


9


from django.utils import timezone
q = Question(question_text="Est ce que c'est gratuit ?", pub_date=timezone.now())
q.save()


10


q.choice_set.all()
q.choice_set.create(choice_text="Possible", votes=0)
q.choice_set.create(choice_text="Surement", votes=0)
q.choice_set.all()

 <QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Possible>, <Choice: Surement>]>








