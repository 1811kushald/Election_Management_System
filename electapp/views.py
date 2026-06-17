from django.shortcuts import render
from electapp.models import Election,Candidate
from electapp.forms import ElectionForm,CandidateForm
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


# Create your views here.
class AboutPage(TemplateView):
    template_name = 'electapp/about.html'


class ElectionList(ListView):
    model = Election
    context_object_name = 'elections'


class ElectionDetail(DetailView):
    model = Election

    
class CreateElection(LoginRequiredMixin,CreateView):
    model = Election
    form_class = ElectionForm


class UpdateElection(LoginRequiredMixin,UpdateView):
    model = Election
    form_class = ElectionForm


class DeleteElection(LoginRequiredMixin,DeleteView):
    model = Election
    success_url = reverse_lazy('election_list')

class CreateCandidate(LoginRequiredMixin,CreateView):
    model = Candidate
    form_class = CandidateForm

class UpdateCandidate(LoginRequiredMixin,UpdateView):
    model = Candidate
    form_class = CandidateForm

class DeleteCandidate(LoginRequiredMixin,DeleteView):
    model = Candidate
    
    def get_success_url(self):
     return reverse('election_detail',kwargs={'pk': self.object.election_name.pk})
    
class ResultPage(LoginRequiredMixin,DetailView):
    model = Election
    template_name = 'electapp/result_page.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['winner'] = (self.object.candidates.order_by('-votes').first())
        return context


@login_required
def LogoutConfirmation(request):
    return render(request,'electapp/logout_page.html')


@login_required
def votecandidate(request,pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    candidate.votes = candidate.votes+1
    candidate.save()

    return redirect('election_detail',pk=candidate.election_name.pk)

@login_required
def EndElection(request,pk):
    election = get_object_or_404(Election,pk=pk)
    election.endelection()
    return redirect('election_list')

    
    













