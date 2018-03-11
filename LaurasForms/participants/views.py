from django.shortcuts import render, get_object_or_404, render
# from django.http import HttpResponseRedirect
# from .forms import ParticipantInfoForm
from .models import ParticipantInfo, ReviewStatus
from .forms import AddParticipantForm, ReviewStatusForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import redirect


# def verify_participant(request, pk):
#     # participant = ParticipantInfo.objects.filter(pk=pk)
#     participant = get_object_or_404(ParticipantInfo, pk=pk)
#     return render(request, 'participants/verify_participant.html', {'participant': participant})


def add_participant(request):
    if request.method == "POST":
        form = AddParticipantForm(request.POST)
        if form.is_valid():
            ParticipantInfo = form.save(commit=False)
            ParticipantInfo.name = request.user
            ParticipantInfo.date_created = timezone.now()
            ParticipantInfo.save()
            return redirect('list_participants')
        print("in views.add_participant POST")
    else:
        form = AddParticipantForm()
        print("in else of views.add_participant")
    return render(request, 'participants/add_participant.html', {'form': form})


def list_participants(request):
    participant = ParticipantInfo.objects.all()
    return render(request, 'participants/list_participants.html', {'participant': participant})
#
#
#
# def input(request, participant_id):
#     participant = get_object_or_404(ParticipantInfo, pk=participant_id)
#     try:
#         participant.
#         selected_choice = participant.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#     if request.method == 'POST':
#         form = ParticipantInfoForm(request.POST)
#         if form.is_valid():
#             pass
#         else:
#             form = ParticipantInfoForm()
#         return render(request, 'info.html', {'form': form})
#
# # def list(request):
# #     response

def review_status(request):
    form=ReviewStatusForm()
    return render(request, 'participants/list_participants.html', {'form': form})