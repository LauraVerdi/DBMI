from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import ParticipantInfo, rev_status_choices
from .forms import AddParticipantForm


def add_participant(request):
    """
    :param request:
    :return: takes the participant information and renders the List Participants page with the added participant
    """
    if request.method == "POST":
        form = AddParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.date_created = timezone.now()
            participant.save()
            return redirect('list_participants')
    else:
        form = AddParticipantForm()
    return render(request, 'participants/add_participant.html', {'form': form})


def update_rev_status(name, new_rev_status):
    """
    :param name: the name of the participant whose status is changing
    :param new_rev_status: the review status change
    :return: none
    """
    ParticipantInfo.objects.filter(participant_name__icontains=name).update(review_status=new_rev_status)
    return


def list_participants(request):
    """
    :param request:
    :return: lists all participant info, the internal POST for loop is to change the review status
    """
    participant = ParticipantInfo.objects.all()
    if request.method == "POST":
        for name in ParticipantInfo(request.POST).participant_name:
            if name != 'csrfmiddlewaretoken':
                update_rev_status(name, request.POST.get(name))

    return render(request, 'participants/list_participants.html',
                  {'participant': participant, 'choices': rev_status_choices})
