from django.urls import path
from electapp import views

urlpatterns =[
    path('',views.ElectionList.as_view(),name='election_list'),
    path('election/<int:pk>/',views.ElectionDetail.as_view(),name='election_detail'),
    path('election/new/',views.CreateElection.as_view(),name='create_election'),
    path('election/<int:pk>/update/',views.UpdateElection.as_view(),name='update_election'),
    path('election/<int:pk>/remove',views.DeleteElection.as_view(),name='remove_election'),
    path('about/',views.AboutPage.as_view(),name='about'),
    path('logout_page/',views.LogoutConfirmation,name='logout_page'),
    path('candidate/new/',views.CreateCandidate.as_view(),name='create_candidate'),
    path('candidate/<int:pk>/edit/',views.UpdateCandidate.as_view(),name='edit_candidate'),
    path('candidate/<int:pk>/remove',views.DeleteCandidate.as_view(),name='remove_candidate'),
    path('candidate/<int:pk>/vote/',views.votecandidate,name='vote_candidate'),
    path('elction/<int:pk>/end/',views.EndElection,name='end_election'),
    path('elction/<int:pk>/result',views.ResultPage.as_view(),name='election_result'),
]