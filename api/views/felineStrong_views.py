from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.fitnessPlan import FitnessPlan
from ..serializers import FitnessPlanSerializer, UserSerializer

# Create your views here.
class FitnessPlans(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request):
    """Index request"""
  # mangos = Mango.objects.all()
    fitnessPlans = FitnessPlan.objects.filter(owner=request.user.id)
    data = FitnessPlanSerializer(fitnessPlans, many=True).data
    return Response(data)

  serializer_class = FitnessPlanSerializer
  def post(self, request):
    """Create request"""
    # Add user to request object
    request.data['fitnessPlan']['owner'] = request.user.id
    # Serialize/create mango
    fitnessPlan = FitnessPlanSerializer(data=request.data['fitnessPlan'])
    if fitnessPlan.is_valid():
      m = fitnessPlan.save()
      return Response(fitnessPlan.data, status=status.HTTP_201_CREATED)
    else:
      return Response(fitnessPlan.errors, status=status.HTTP_400_BAD_REQUEST)

class FitnessPlanDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request, pk):
    """Show request"""
    fitnessPlan = get_object_or_404(FitnessPlan, pk=pk)
    data = FitnessPlanSerializer(fitnessPlan).data
    # Only want to show owned fitnessPlans?
    # if not request.user.id == data['owner']:
    #     raise PermissionDenied('Unauthorized, you # Don't really need to change anything UNLESS
    # We want to return just the mangos owned by the currently
    # signed in user!
    # We want to compare the `request.user` against the owner
    # of the mango we find above with `get_object_or_404`
    # If they're not the same, give the client a error that they
    # do not have access to this mango.do not own this fitnessPlan')
    if not request.user.id == fitnessPlan.owner.id:
            raise PermissionDenied('Unauthorized, owner doesnt match.')
    return Response(data)

    def delete(self, request, pk):
      """Delete request"""
      FitnessPlan = get_object_or_404(FitnessPlan, pk=pk)
      if not request.user.id == fitnessPlan.owner.id:
        raise PermissionDenied('Unauthorized, you do not own this fitnessPlan')
        fitnessPlan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
      """Update Request"""
      # Remove owner from request object
      if request.data['fitnessPlan'].get('owner', False):
        del request.data['fitnessPlan']['owner']

        # Locate FitnessPlan
      fitnessPlan = get_object_or_404(FitnessPlan, pk=pk)

      # Check if user is  the same
      if not request.user.id == fitnessPlan.owner.id:
        raise PermissionDenied('Unauthorized, you do not own this fitnessPlan')

      # Add owner to data object now that we know this user owns the resource
      request.data['fitnessPlan']['owner'] = request.user.id
      # Validate updates with serializer
      ms = FitnessPlanSerializer(fitnessPlan, data=request.data['fitnessPlan'])
      if ms.is_valid():
        ms.save()
        # print(ms)
        return Response(ms.data)
      return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
