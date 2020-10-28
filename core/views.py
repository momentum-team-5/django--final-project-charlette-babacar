from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .models import Answer, Question
from .forms import AnswerForm, QuestionForm, SearchForm, ContactForm
from users.models import User
from django.http import JsonResponse
from django.core.mail import send_mail, mail_admins

# Create your views here.
def question_list(request):
    question = Question.objects.all()
    
    return render(request, 'question_list.html', {"question":question})

@login_required
def question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()

    if request.method =="GET":
        form = AnswerForm()

    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            success(request, "Answer saved!")

            return redirect(to="question_details", pk=question.pk)

        else:
            error(request, "Couldn't save your answer")

    return render(request, "question_details.html", {"question": question, "answers": answers, "form": form})
        
@login_required
def add_question(request):
    if request.method == 'GET':
        form = QuestionForm()

    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(to='question_list')
        else:
            error(request, "There is a problem with your submission!")

    return render(request, "add_question.html", {"form": form})        

@login_required
def add_answer(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'GET':
        form = AnswerForm()
        
    else:
        form = AnswerForm(data=request.POST)
    
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect(to='question_list')

        else:
            error(request, "Problem with your submission.")

    return render(request, "add_answer.html", {"form": form, "question": question})


@login_required
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.user:
        error(request, "Question can only be edited by the creator")
        return redirect(to='question_list')

    if request.method == 'GET':
        form = QuestionForm(instance=question)

    else:
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect(to='question_list')

    return render(request, "edit_question.html", {"form": form, "question": question})


@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user != question.user:
        error(request, "Question can only be deleted by the creator.")
        return redirect(to="question_list")

    if request.method == 'POST':
        question.delete()
        success(request, "Question deleted!")

        return redirect(to='question_list')

    return render(request, "delete_question.html", {"question": question})


@login_required
def delete_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.user != answer.user:
        error(request, "Answer can only be deleted by the creator.")
        return redirect(to="question_list")

    if request.method == 'POST':
        answer.delete()
        success(request, "Answer deleted!")

        return redirect(to='question_list')

    return render(request, "delete_answer.html", {"answer": answer})


def search(request):
    if request.method == "GET":
        form = SearchForm()

    elif request.method == "POST":
        form = SearchForm(data=request.POST)

    if form.is_valid():
        question = form.cleaned_data['question']
        question = Question.objects.filter(question__contains=question)

        return render(request, "search_results.html", {"question": question})

    return render(request, "search.html", {"form": form})


@login_required
def add_favorite(request, pk):
    answer = get_object_or_404(Answer, id=pk)

    if request.user.is_authenticated:
        if answer.favoriting_users.filter(id=request.user.pk).count() == 0:
            answer.favoriting_users.add(request.user)
            message = "Favorite added!"

        else:
            message = "You can only favorite an answer once."
        
    else:
        message = "Only signed in users can favorite answers."

    numLikes = answer.numfavorites()

    return JsonResponse({"message": message, "numLikes": numLikes})


def contact_us(request):
    if request.method == "GET":
        form = ContactForm()

    else:
        form = ContactForm(data=request.POST)

        if form.is_valid():
            user_email = form.cleaned_data['email']
            message_title = form.cleaned_data['title']
            message_body = form.cleaned_data['body']

            send_mail("Someone answered your question", "Your message has been answered! Go check out your message!", None, recipient_list=[user_email])
            mail_admins(message_title, message_body, fail_silently=True)

            success(request, "Your message was sent to a local server for testing, thank you!")

            return redirect(to='question_list')

        else:
            error("Your message couldn't be sent.")

    return render(request, "contact_us.html", {"form": form})