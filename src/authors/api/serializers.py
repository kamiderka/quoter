from rest_framework import serializers
from authors.models import *
from quotes.models import *
from quotes.api.permissions import IsOwner

class AuthorPostSerializer(serializers.ModelSerializer):
    is_fav = serializers.BooleanField(default=False)



    class Meta:
        model = Author
        fields = ('name', 'is_fav')

    
    def create(self, validated_data):
        self.user = self.context['user']

        author_name = validated_data.pop('name')
        is_fav = validated_data.pop('is_fav')

        author = Author.objects.create(name=author_name, created_by=self.user, is_fav=is_fav )
        
        return author
    
    
    def update(self, instance, validated_data):

        self.user = self.context['user']
        
        author_name = validated_data.get('name', None)
        if author_name:
            validated_data['name'] = author_name
            
        return super().update(instance, validated_data)


class AuthorGetSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='name')
    # is_fav = serializers.BooleanField(source='is_fav')
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = Author
        fields = ('id', 'name', 'is_fav', 'created_by')

    


        


    