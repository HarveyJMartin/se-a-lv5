from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import LoginView


# Create your views here.
def landing_page(request):
    return render(request, "landing_page.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or elsewhere
            return redirect("/tickets/")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "login.html"
