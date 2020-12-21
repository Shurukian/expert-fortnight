from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.flashcard_views import Flashcards, FlashcardDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('flashcards/', Flashcards.as_view(), name='flashcards'),
    path('flashcards/<int:pk>/', FlashcardDetail.as_view(), name='flashcard_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
