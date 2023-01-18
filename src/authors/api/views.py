from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from authors.models import *
from .serializers import *


class AuthorsViewSet(ModelViewSet):
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Author.objects.exclude(quote=None).filter(created_by=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AuthorGetSerializer
        elif self.request.method in ['POST', 'PUT', 'PATCH']:
            return AuthorPostSerializer

    def get_serializer_context(self):
        return { 'user': self.request.user }
    


# class QuoteView(APIView):

#     def get(self, request):
#         quotes = Quote.objects.filter(created_by=request.user)
#         serializer = QuoteSerializer(quotes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = QuoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk):
#         quote = Quote.objects.get(pk=pk)
#         quote.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)