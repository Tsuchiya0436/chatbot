import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, Answer
from django.views.decorators.csrf import csrf_exempt

API_KEY = 'ZZihX12RJZuCJSrBVn7i7eyqx7LcKklA'
TALK_URL = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        question_text = request.POST.get('question')
        
        # Save the question to the database
        question = Question(question_text=question_text)
        question.save()

        # Call Talk API
        response = requests.post(TALK_URL, data={'apikey': API_KEY, 'query': question_text})
        result = response.json()

        if result['status'] == 0:
            answer_text = result['results'][0]['reply']
        else:
            answer_text = "I'm sorry, I couldn't understand that."

        # Save the answer to the database
        answer = Answer(question=question, answer_text=answer_text)
        answer.save()

        return JsonResponse({'answer': answer_text})

    return render(request, 'chatbot/chat.html')
