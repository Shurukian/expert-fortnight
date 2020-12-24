from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.flashcard import Flashcard
from ..serializers import FlashcardSerializer, UserSerializer

class Flashcards(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=FlashcardSerializer
    def get(self, request):
        """Index request for Flashcard"""
        flashcards = Flashcard.objects.filter(owner=request.user.id)

        data = FlashcardSerializer(flashcards, many=True).data
        return Response({ 'flashcards': data })

    def post(self, request):
        """Create request"""
        # Add the user to request the data object
        request.data['flashcard']['owner'] = request.user.id
        # Serialize and create the flashcard
        flashcard = FlashcardSerializer(data=request.data['flashcard'])

        if flashcard.is_valid():
            # Save the created flashcard and store the response.
            flashcard.save()
            return Response({ 'flashcard': flashcard.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid then return an error response
        return Response(flashcard.errors, status=status.HTTP_400_BAD_REQUEST)

class FlashcardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show the request"""
        # Locate the flashcard data to show
        flashcard = get_object_or_404(Flashcard, pk=pk)
        # Check to see who the flashcard owner is before making the show request.
        if not request.user.id == flashcard.owner.id:
            raise PermissionDenied('Unauthorized, you do not own the flashcard you requested')

        data = FlashcardSerializer(flashcard).data
        return Response({ 'flashcard': data })

    def delete(self, request, pk):
        """Delete request"""
        # locate the specfic flashcard to delete
        flashcard = get_object_or_404(Flashcard, pk=pk)
        # Check for the flashcard owner against the user making the request
        if not request.user.id == flashcard.owner.id:
            raise PermissionDenied('Unauthorized, you do not own the flashcard you requested')
        # Only delete the flashcard if the user is the owner
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['mango'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['flashcard'].get['owner', False]:
          del request.data['flashcard']['owner']

        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        flashcard = get_object_or_404(Flashcard, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == flashcard.owner.id:
            raise PermissionDenied('Unauthorized, you do not own the flashcard you requested')

        # Add owner to data object now that we know this user owns the resource
        request.data['flashcard']['owner'] = request.user.id
        # Validate the updates with the Serializer
        data = FlashcardSerializer(flashcard, data=request.data)
        if data.is_valid():
            # Save and send the response after the request is made
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, then return a response with the errors
        return Reponse(data.errors, status=status.HTTP_400_BAD_REQUEST)
