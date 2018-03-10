from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from .forms import ParticipantInfoForm
from .models import ParticipantInfo
from .forms import AddParticipantForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import redirect

# from django.views import generic
#
# from .models import ParticipantInfo
# path = 'LaurasForms'

# Create your views here.
# def index(request):
#     return HttpResponse("Participant information")
# class IndexView(generic.ListView):
#     template_name = '{}/index.html'.format(path)
#     context_object_name = 'add_or_list_participants'
#
#     def get_queryset(self):
#         return ParticipantInfoForm.objects.order_by('-pub_date')[:5]
#
#
# class InputView(generic.DetailView):
#     model = ParticipantInfoForm
#     template_name = '{}/input.html'.format(path)
#
#
# class ShowAllView(generic.DetailView):
#     # model = ParticipantInfoForm
#     model = ParticipantInfo
#     # template_name
#

# def verify_participant(request, pk):
#     # participant = ParticipantInfo.objects.filter(pk=pk)
#     participant = get_object_or_404(ParticipantInfo, pk=pk)
#     return render(request, 'participants/verify_participant.html', {'participant': participant})


#    # def verify_participant(request, pk):
#    #     # participant = ParticipantInfo.objects.filter(pk=pk)
#    #     # participant = get_object_or_404(ParticipantInfo, pk=pk)
#    #     if request.method == "POST":
#    #         form = VerifyParticipantForm(request.POST, instance=ParticipantInfo)
#    #         if form.is_valid():
#    #             participant = form.save(commit=False)
#    #             participant.author = request.user
#    #             participant.published_date = timezone.now()
#    #             participant.save()
#    #             return redirect('verify_participant', pk=pk)
#    #         else:
#    #             form = VerifyParticipantForm(instance=ParticipantInfo)
#    #     return render(request, 'participants/verify_participant.html', {'pk': pk})
#    #
#    #     # return render(request, 'participants/verify_participant.html', {'pk': participant.pk})


def add_participant(request):
    if request.method == "POST":
        form = AddParticipantForm(request.POST)
        if form.is_valid():
            ParticipantInfo = form.save(commit=False)
            ParticipantInfo.name = request.user
            ParticipantInfo.date_created = timezone.now()
            ParticipantInfo.save()
            return redirect('list_participants')

            # return redirect('verify_participant', pk=ParticipantInfo.pk)
        print("in views.add_participant POST")
    else:
        form = AddParticipantForm()
        print("in else of views.add_participant")
    return render(request, 'participants/add_participant.html', {'form': form})

# def add_participant(request):
#     if request.method == "POST":
#         form = AddParticipantForm(request.POST)
#         print("AddParticipantForm with args")
#         if form.is_valid():
#             p = form.save(commit=False)
#             p.name = request.Name
#             p.age = request.Age
#             p.date_created = timezone.now
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = AddParticipantForm()
#         print("AddParticipantForm with no args")
#     # participant = ParticipantInfo.objects.create(
#     #     participant_name=request.participant_name,
#     #     participant_age=request.participant_age,
#     #     participant_siblings=request.participant_sibs,
#     #     env_exposures=request.env_exposures,
#     #     gen_mutations=request.gen_mutations,
#     #     rev_status=request.rev_status)
#     return render(request, 'participants/add_participant.html', {'form': form})


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
