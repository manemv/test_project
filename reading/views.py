from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Test, Question

def index(request):
    # Fetch all tests with their related passages, questions, and choices in one query
    tests = Test.objects.prefetch_related(
        'passages__questions__choices'  # Prefetch related passages, questions, and choices
    )
    return render(request, "reading/index.html", {'tests': tests})

def page(request, page_id):
    return HttpResponse("You're looking at page # %s." % page_id)

# View to retrieve a specific question and its related passage and choices
def question_detail(request, test_id, question_id=None):
    # Get the test by test_id
    test = get_object_or_404(Test, id=test_id)

    if question_id is None:
        # If no question_id is passed, get the first question from the first passage
        question = test.passages.first().questions.first()
    else:
        # Otherwise, get the question by its ID
        question = get_object_or_404(Question, id=question_id)

    # Retrieve related passage and choices
    passage = question.passage
    choices = question.choices.all()

    # Find the next and previous questions
    questions = list(Question.objects.filter(passage__test=test).order_by('id'))
    current_index = questions.index(question)
    next_question = questions[current_index + 1] if current_index + 1 < len(questions) else None
    prev_question = questions[current_index - 1] if current_index > 0 else None

    context = {
        'test': test,
        'passage': passage,
        'question': question,
        'choices': choices,
        'next_question': next_question,
        'prev_question': prev_question
    }

    return render(request, 'reading/single-question.html', context)