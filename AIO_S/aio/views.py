from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserForm
from .models import OfferWork, User


def home(requests):
    return render(requests, "main.html")


def rus(requests):
    return render(requests, "RUS.html")


def uzb(requests):
    return render(requests, "UZB.html")


def eng(requests):
    return render(requests, "ENG.html")


def uzb_test(requests, user_id):
    user = get_object_or_404(User, pk=user_id)
    if requests.method == "POST":
        model = OfferWork(
            user = user,
            text=requests.POST.get("result", "So Problems, Sorry!!!"),
            score=int(requests.POST.get("score", "0")),
        )
        model.save()
        return redirect(reverse('calculate', kwargs={'work_id':model.id}))
    return render(requests, "uzb_test.html")


def rus_test(requests, user_id):
    user = get_object_or_404(User, pk=user_id)
    if requests.method == "POST":
        model = OfferWork(
            user = user,
            text=requests.POST.get("result", "So Problems, Sorry!!!"),
            score=int(requests.POST.get("score", "0")),
        )
        model.save()
        return redirect(reverse('calculate', kwargs={'work_id':model.id}))
    return render(requests, "rus_test.html")


def eng_test(requests, user_id):
    user = get_object_or_404(User, pk=user_id)
    if requests.method == "POST":
        model = OfferWork(
            user = user,
            text=requests.POST.get("result", "So Problems, Sorry!!!"),
            score=int(requests.POST.get("score", "0")),
        )
        model.save()
        return redirect(reverse('calculate', kwargs={'work_id':model.id}))
    return render(requests, "eng_test.html")


from django.shortcuts import render


def result_view(request, work_id):
    model = get_object_or_404(OfferWork, pk=work_id)

    return render(request, "score.html", {"message": model})


def UserInfo(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user_form = form.save()
            return redirect(reverse("uzb_test", kwargs={'user_id':user_form.id}))

    else:
        form = UserForm()

    return render(request, "uzb_login.html", {"form": form})


def UserInfoRus(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user_form = form.save()
            return redirect(reverse("rus_test", kwargs={'user_id':user_form.id}))
    else:
        form = UserForm()

    return render(request, "rus_login.html", {"form": form})


def UserInfoEng(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user_form = form.save()

            return redirect(reverse("eng_test", kwargs={'user_id':user_form.id}))
    else:
        form = UserForm()

    return render(request, "eng_login.html", {"form": form})
