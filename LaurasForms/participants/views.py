from django.shortcuts import render
from .models import ParticipantInfo, rev_status_choices
from .forms import AddParticipantForm
from django.utils import timezone
from django.shortcuts import redirect


def add_participant(request):
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
    ParticipantInfo.objects.filter(participant_name__icontains=name).update(review_status=new_rev_status)
    return


def list_participants(request):
    participant = ParticipantInfo.objects.all()
    if request.method == "POST":
        # m = ParticipantInfo(request.POST)
        for name in ParticipantInfo(request.POST).participant_name:
            if name != 'csrfmiddlewaretoken':
                update_rev_status(name, request.POST.get(name))

    return render(request, 'participants/list_participants.html',
                  {'participant': participant, 'choices': rev_status_choices})
