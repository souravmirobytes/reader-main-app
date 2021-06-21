from .models import Book, BookContent, BookRevision
from .serializers import BookListSerializer, BookViewSerializer, BookCreateSerializer, BookUpdateSerializer, BookRevisionCreateSerializer,BookRevisionListSerializer, BookRevisionViewSerializer, BookRevisionUpdateSerializer, BookContentCreateSerializer,BookContentListSerializer, BookContentViewSerializer, BookContentUpdateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse

# BOOK
class CreateBookAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    # permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookCreateSerializer(queryset, many=True)
        return Response(serializer.data)

class ListBookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookListSerializer(queryset, many=True)
        return Response(serializer.data)

class GetBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookViewSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookViewSerializer(queryset, many=True)
        return Response(serializer.data)
        
class UpdateBookAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookUpdateSerializer(queryset, many=True)
        return Response(serializer.data)



# REVISION
class CreateBookRevisionAPIView(generics.CreateAPIView):
    queryset = BookRevision.objects.all()
    serializer_class = BookRevisionCreateSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookCreateSerializer(queryset, many=True)
        return Response(serializer.data)

class ListBookRevisionAPIView(generics.ListAPIView):
    queryset = BookRevision.objects.all()
    serializer_class = BookRevisionListSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookRevisionListSerializer(queryset, many=True)
        return Response(serializer.data)

class GetBookRevisionAPIView(generics.RetrieveAPIView):
    queryset = BookRevision.objects.all()
    serializer_class = BookRevisionViewSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookRevisionViewSerializer(queryset, many=True)
        return Response(serializer.data)

class UpdateBookRevisionAPIView(generics.UpdateAPIView):
    queryset = BookRevision.objects.all()
    serializer_class = BookRevisionUpdateSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookRevisionUpdateSerializer(queryset, many=True)
        return Response(serializer.data)


# CONTENT
class CreateBookContentAPIView(generics.CreateAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentCreateSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookContentCreateSerializer(queryset, many=True)

class ListBookContentAPIView(generics.ListAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentListSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookContentListSerializer(queryset, many=True)
        return Response(serializer.data)

class GetBookContentAPIView(generics.RetrieveAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentViewSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookContentViewSerializer(queryset, many=True)
        return Response(serializer.data)

class UpdateBookContentAPIView(generics.UpdateAPIView):
    queryset = BookContent.objects.all()
    serializer_class = BookContentUpdateSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BookContentUpdateSerializer(queryset, many=True)
        return Response(serializer.data)