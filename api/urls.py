from django.urls import path
from .views.felineStrong_views import FitnessPlan, FitnessPlanDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
	# Restful routing
    path('fitnessPlans/', Mangos.as_view(), name='fitnessPlans'),
    path('fitnessPlans/<int:pk>/', FitnessPlanDetail.as_view(), name='fitnessPlan_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
