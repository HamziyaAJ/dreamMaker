from django.urls import path
<<<<<<< HEAD
from .views import my_profile_view
=======
from .views import (
    my_profile_view, 
    invites_received_view, 
    profiles_list_view, 
    invite_profiles_list_view, 
    ProfileDetailView,
    ProfileListView, 
    send_invitations, 
    remove_from_friends,
    accept_invitation,
    reject_invitation,
)
>>>>>>> d5302132746921ea390fb3826529e2359b21a372

app_name = 'profiles'

urlpatterns = [
<<<<<<< HEAD
		path('myprofile/', my_profile_view, name='my-profile-view' ),
]
=======
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('myProfile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('to-invite/', invite_profiles_list_view, name='invite-profiles-view'),
    path('send-invite/',send_invitations, name='send-invite'),
    path('remove-friend/',remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/accept/', accept_invitation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject-invite'),
]

>>>>>>> d5302132746921ea390fb3826529e2359b21a372
