from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

users = [
    {
        "name": "Alice",
        "email": "alice@gmail.com",
    },
    {
        "name": "Bob",
        "email": "bob@gmail.com",
    },{
        "name": "Ricardo",
        "email": "ricardo@gmail.com",
    }
]


def user_view(request):

    context = {
        "users": users,
    }

    return render(request, "user_page.html", context)


def edit_user(request, email):

    context = {
        "email": email,
    }

    return render(request, "edit_user.html", context)


def delete_user(request, email, user):
    global users

    for u in users:
        if u["name"] == user and u["email"] == email:
            users.remove(u)
            return redirect("/users/")

    context = {
        "email": email,
    }

    return render(request, "edit_user.html", context)
