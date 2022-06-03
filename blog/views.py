from django.shortcuts import render

posts = [
    {
        "author": "murtaza",
        "title": "blog post 1",
        "content": "First Post Content",
        "dated": "May 12, 2021",
    },
    {
        "author": "Ali",
        "title": "blog post 2",
        "content": "Second Post Content",
        "dated": "May 14, 2021",
    },
    {
        "author": "Akbar",
        "title": "blog post 3",
        "content": "Third Post Content",
        "dated": "May 15, 2021",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def contact(request):
    return render(request, "blog/contact.html", {"title": "contact"})
