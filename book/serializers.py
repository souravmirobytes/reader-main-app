from rest_framework import serializers
from .models import Book, BookRevision, BookContent

class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'isPublished',
            'latest',
            'modifiedBy',
        )

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isPublished',
            'createdAt',
            'updatedAt',
        )


class BookViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'updatedAt',
            'author',
            'revisionPublished',
            'isPublished',
            'latest',
            'createdAt',
            'updatedAt',
            'book',
            'revisionCode',
            'googleDoc',
        )

class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'isPublished',
            'latest',
            'publisher',
            'modifiedBy',
        )



# BOOK REVISION
class BookRevisionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRevision
        fields = (
            'id',
            'title',
            'author',
            'publisher',
            'book',
            'content',
            'modifiedBy',
            'isPublished',
            'content',
        )

class BookRevisionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRevision
        fields = (
            'id',
            'title',
            'author',
            'publisher',
            'book',
            'content',
            'modifiedBy',
            'isPublished',
            'content',
        )

class BookRevisionViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRevision
        fields = (
            'id',
            'title',
            'author',
            'publisher',
            'book',
            'content',
            'modifiedBy',
            'isPublished',
            'content',
        )

class BookRevisionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookRevision
        fields = (
            'id',
            'title',
            'author',
            'publisher',
            'book',
            'content',
            'modifiedBy',
            'isPublished',
            'content',
        )

# BOOK CONTENT
class BookContentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookContent
        fields = ('__all__')

class BookContentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookContent
        fields = ('__all__')

class BookContentViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookContent
        fields = ('__all__')

class BookContentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookContent
        fields = ('__all__')