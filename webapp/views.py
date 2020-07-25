from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Lyrics
from . serializers import LyricsSerializer 
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
    # """
    # Second code
    # """
# class LyricsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Lyrics.objects.all()
#     serializer_class = LyricsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

   
    # """
    # First code
    # """
    # def get(self, request):
    #     lyrics1 = Lyrics.objects.all()
    #     serializer = LyricsSerializer(lyrics1, many=True)
    #     return Response(serializer.data)


    # def post(self, request, format=None):
    #     serializer = LyricsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LyricsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    # """
    # Retrieve, update or delete a lyrics instance.
    # """

    # """
    # Second code
    # """
    # queryset = Lyrics.objects.all()
    # serializer_class = LyricsSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

    # """
    # First code
    # """
    # def get_object(self, pk):
    #     try:
    #         return Lyrics.objects.get(pk=pk)
    #     except Lyrics.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     Lyrics = self.get_object(pk)
    #     serializer = LyricsSerializer(Lyrics)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     Lyrics = self.get_object(pk)
    #     serializer = LyricsSerializer(Lyrics, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     Lyrics = self.get_object(pk)
    #     Lyrics.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class LyricsList(generics.ListCreateAPIView):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer


class LyricsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer