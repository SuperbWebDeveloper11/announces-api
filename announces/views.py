from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import viewsets, permissions, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnnounceSerializer, CommentSerializer
from .models import Announce, Comment
from .permissions import IsOwnerOrReadOnly


# **************** announce views ****************  
class AnnounceList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        announces = Announce.objects.all()
        serializer = AnnounceSerializer(announces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnnounceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnnounceDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Announce.objects.get(pk=pk)
        except Announce.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        announce = self.get_object(pk)
        serializer = AnnounceSerializer(announce)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        announce = self.get_object(pk)
        serializer = AnnounceSerializer(announce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        announce = self.get_object(pk)
        announce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# **************** comment views ****************  
class CommentList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        announce = get_object_or_404(Announce, pk=pk) # get current announce
        comments = Comment.objects.filter(announce=announce)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        announce = get_object_or_404(Announce, pk=pk) # get current announce
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user, announce=announce)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk, comment_pk):
        try:
            announce = Announce.objects.get(pk=pk)
            comment = Comment.objects.get(pk=comment_pk, announce=announce)
            return comment
        except:
            raise Http404

    def get(self, request, pk, comment_pk, format=None):
        comment = self.get_object(pk, comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, comment_pk, format=None):
        comment = self.get_object(pk, comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, comment_pk, format=None):
        comment = self.get_object(pk, comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

