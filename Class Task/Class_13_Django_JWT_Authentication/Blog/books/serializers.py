from rest_framework import serializers
from .models import Book, Author, Publisher
from django.utils import timezone
from datetime import timedelta


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        # Validate title length
        if attrs.get('title') and len(attrs['title']) > 100:
            raise serializers.ValidationError('Title is too long.')

        # Validate description word count
        if attrs.get('description') and len(attrs['description'].split()) < 3:
            raise serializers.ValidationError('Description is too short.')
        
        # Validate price: Must be between 100 and 10,000
        if attrs.get('price'):
            if attrs['price'] < 100 or attrs['price'] > 10000: 
                raise serializers.ValidationError('Price is out of range.')

        # Validate publication date
        if attrs.get('publication_date'):
            one_month_ago = timezone.now() - timedelta(days=30)
            if attrs['publication_date'] > one_month_ago.date():
                raise serializers.ValidationError("Publication date must be at least one month old.")

        return attrs
    
    def create(self, validated_date):
        author = validated_date.pop('author')
        author_serializer = AuthorSerializer(data=author)
        publisher = validated_date.pop('publisher')
        publisher_serializer = PublisherSerializer(data=publisher)
        
        if author_serializer.is_valid():
            author_instance = author_serializer.save()
            validated_date['author'] = author_instance

            # or , validated_date['author'] =  author_serializer.save()
        if publisher_serializer.is_valid():
            publisher_instance = publisher_serializer.save()
            validated_date['publisher'] = publisher_instance

        return super().create(validated_date)
    
    def update(self, instance,validated_date):
        validated_date['validated_date'] =  timezone.now()
        
        return super().update(instance, validated_date)