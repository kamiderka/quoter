from rest_framework import serializers
from quotes.models import *

class QuotePostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=40,) #source='author.name')
    source = serializers.CharField(max_length=100, allow_blank=True) #source='source.name')
    is_fav = serializers.BooleanField(default=False)



    class Meta:
        model = Quote
        fields = ('content', 'author', 'source', 'is_fav')

    
    def create(self, validated_data):
        self.user = self.context['user']

        author_name = validated_data.pop('author')
        source_name = validated_data.pop('source')
        is_fav = validated_data.pop('is_fav')

        try:
            author = Author.objects.get(name=author_name, created_by=self.user)
        except Author.DoesNotExist:
            author = Author(name=author_name, created_by=self.user)
            author.save()

        try:
            source = Source.objects.get(name=source_name, created_by=self.user)
        except Source.DoesNotExist:
            source = Source(name=source_name, author=author, created_by=self.user)
            source.save()
        
        content = validated_data.get('content')

        quote = Quote.objects.create(content=content, author=author, source=source, created_by=self.user, is_fav=is_fav )
        
        return quote
    
    
    def update(self, instance, validated_data):

        self.user = self.context['user']
        
        author_name = validated_data.get('author', None)
        if author_name:
            try:
                author = Author.objects.get(name=author_name, created_by=self.user)
            except Author.DoesNotExist:
                author = Author(name=author_name, created_by=self.user)
                author.save()
            
            validated_data['author'] = author
        
        source_name = validated_data.get('source', None)
        if source_name:
            try:
                source = Source.objects.get(name=source_name, created_by=self.user)
            except Source.DoesNotExist:
                source = Source(name=source_name, author=author, created_by=self.user)
                source.save()
            
            
            validated_data['source'] = source
        
        return super().update(instance, validated_data)


class QuoteGetSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    source = serializers.CharField(source='source.name')
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = Quote
        fields = ('id', 'content', 'author', 'source', 'is_fav', 'pub_date', 'created_by')

