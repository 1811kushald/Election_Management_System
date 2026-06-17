from electapp.models import Election,Candidate
from django import forms

class ElectionForm(forms.ModelForm):

    class Meta():
        model = Election
        fields = ('election_name','post')

class CandidateForm(forms.ModelForm):

    class Meta():
        model = Candidate
        fields = ('election_name','candidate_name','grade','photo')
