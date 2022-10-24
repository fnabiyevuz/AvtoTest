from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    if request.method=="POST":
        id = request.POST['bilet_id']
        return redirect(f'/bilet/{id}/1')
    else:
        context = {
            'title':'Biletlar',
            'biletlar': Biletlar.objects.all()
        }
        return render(request, 'index.html', context)

def bilet(request, id, num):
    if request.method=="POST":
        correct = int(request.POST['correct'])
        incorrect = int(request.POST['incorrect'])
        question = Questions.objects.get(id=num-1)
        bilet = question.bilet
        try:
            answer = request.POST['answer']
        except:
            context = {
                'title':f"{bilet}-bilet {num}-savol",
                'correct':correct,
                'incorrect':incorrect,
                'id':id,
                'num':num+1,
                'question':bilet.quest_bilet.get(number=num)
            }
            return redirect(f'/bilet/{id}/{num-1}?correct={correct}&incorrect={incorrect}')
        
        if question.correct == answer:
            correct += 1
        else:
            incorrect += 1
        if num == 11:
            messages.success(request, f"Savollar soni: 10 ta | To'g'ri javob: {correct} ta | Noto'gri javob: {incorrect} ta")
            return redirect('/')
        context = {
            'title':f"{bilet}-bilet {num}-savol",
            'correct':correct,
            'incorrect':incorrect,
            'id':id,
            'num':num+1,
            'question':bilet.quest_bilet.get(number=num)
        }
    else:
        question = Questions.objects.get(bilet_id=id, number=num)
        if request.GET['correct'] and request.GET['incorrect']:
            correct=request.GET['correct']
            incorrect=request.GET['incorrect']
        else:
            correct=0
            incorrect=0

        context = {
                    'title':f"{id}-bilet {num}-savol",
                    'correct':correct,
                    'incorrect':incorrect,
                    'id':id,
                    'num':num+1,
                    'question':question
                }
    return render(request, 'question.html', context)


def question(request):
    if request.method == "POST":
        try:
            id = request.POST['bilet_id']
            bilet = Biletlar.objects.get(id=id)
            context = {
                'title':f"{bilet}-bilet 1-savol",
                'correct':0,
                'incorrect':0,
                'question':bilet.quest_bilet.get(number=1)
            }
        except:
            ques = request.POST['question']
            number = int(request.POST['number'])
            answer = request.POST['answer']
            correct = int(request.POST['correct'])
            incorrect = int(request.POST['incorrect'])
            question = Questions.objects.get(id=ques)
            bilet = question.bilet
            if question.correct == answer:
                correct += 1
            else:
                incorrect += 1
            context = {
                'title':f"{bilet}-bilet {number+1}-savol",
                'correct':correct,
                'incorrect':incorrect,
                'question':bilet.quest_bilet.get(number=number+1)
            }
        return render(request, 'question.html', context)