from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, Category
import random

def home(request):
    context = {'categories': Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'index.html', context)

def quiz_page(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'quiz.html', context)

def get_quiz_api(request):
    try:
        questions_objs = Question.objects.all()
        if request.GET.get('category'):
            questions_objs = questions_objs.filter(category__name__icontains=request.GET.get('category'))
        questions_objs = list(questions_objs)
        random.shuffle(questions_objs)
        data = []
        for question_obj in questions_objs:
            data.append({
                'uid': question_obj.uid,
                'category': question_obj.category.name,
                'question': question_obj.question,
                'marks': question_obj.marks,
                'difficulty': question_obj.difficulty,
                'answers': question_obj.get_answers()
            })
        payload = {'status': True, 'data': data}
        return JsonResponse(payload)
    except Exception as e:
        payload = {'status': False, 'error': str(e)}
        return JsonResponse(payload)



