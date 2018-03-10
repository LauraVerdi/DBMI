from django.shortcuts import get_object_or_404, render
#from django.shortcuts import render
from .forms import ParticipantForm

from django.http import HttpResponse
from django.template import loader
# from .models import ParticipantInfo, ParticipantId
# from .models import Question, ParticipantInfo, ParticipantId
    #, ParticipantAge, ParticipantSiblings, EnvironmentalExposures, GeneticMutations

def input(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ParticipantForm()
    return render(request, 'info.html', {'form': form})
    # # name = get_object_or_404(ParticipantId)
    # name = get_object_or_404(ParticipantInfo.participant_name)
    # ## name = ParticipantInfo.participant_name, pk=id)
    # # age = ParticipantInfo.participant_age
    # # sibs = ParticipantInfo.participant_siblings
    # # exposures = ParticipantInfo.env_exposures
    # # mutations = ParticipantInfo.gen_mutations
    # response = "This is the participant_info page for %s", name
    # return HttpResponse(response, " - Done")

def list(request):
    response = "This is the page to list all participant information"
    return HttpResponse(response, "list")

# # Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # return HttpResponse("You're looking at question %s." % question_id)
#     return render(request, 'DBMI/detail.html', {'question': question})
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
