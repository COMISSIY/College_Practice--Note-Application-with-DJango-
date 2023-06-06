from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Notes
from .forms import LoginForm, NoteForm


def index(request):
    notes = []
    username = "anon"
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                print("is valid!!!!")
                user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
                if user is not None:
                    print(login(request, user))
                    return HttpResponseRedirect("/diary")
            else:
                print("form is invalid((")
    else:
        if request.method == "POST" and "btn_new_note" in request.POST:
            note_form = NoteForm(request.POST)
            title = "New Note"
            text = ""
            print(request.POST)
            if note_form.is_valid():
                if note_form.cleaned_data["title"]:
                    title = note_form.cleaned_data["title"]
                if note_form.cleaned_data["text"]:
                    text = note_form.cleaned_data["text"]
                new_note = Notes(owner=int(request.user.id), title=title, text=text)
                new_note.save()
            return HttpResponseRedirect("/diary")
        elif request.method == "POST" and "btn_save_note" in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                if note_form.cleaned_data["noteId"]:
                    note = Notes.objects.get(id=int(note_form.cleaned_data["noteId"]))
                    if note:
                        note.title = note_form.cleaned_data["title"]
                        note.text = note_form.cleaned_data["text"]
                        note.save()
            return HttpResponseRedirect("/diary")
        elif request.method == "POST" and "btn_delete_note" in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                if note_form.cleaned_data["noteId"]:
                    note = Notes.objects.get(id=int(note_form.cleaned_data["noteId"]))
                    if note:
                        note.delete()

            return HttpResponseRedirect("/diary")
        else:
            username = request.user.username
            print(request.user.id)
            notes = Notes.objects.filter(owner=request.user.id)
    return render(request, "index.html", {"notes": notes, "username": username, "newNoteForm": NoteForm()})


    # if not request.user.is_authenticated:
    #     print("login again(((")
    #     user = authenticate(request, username="comissiy", password="amogus")
    #     if user is not None:
    #         login(request, user)
    # else:
    #     print("wtf i got logined&&&")
    # notes = []
    # if request.user.is_authenticated:
    #     notes = Notes.objects.filter(owner=request.user.id)
    # print("response is", notes)
    # return render(request, "index.html", {"notes": notes})


def auth(request):
    logout(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("form is valid!!!")
            print(form.cleaned_data["username"], form.cleaned_data["password"])
        else:
            print("form is invalid")
    else:
        form = LoginForm()
    return render(request, "auth_register.html", {"form":form})
