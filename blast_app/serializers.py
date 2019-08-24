from rest_framework import serializers

from .models import BlastQuery, BlastResult


class BlastQuerySerializer(serializers.ModelSerializer):
    results = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'id',
            'query_id',
            'pub_date',
            'results'
        )
        model = BlastQuery


class BlastResultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'query_id',
            'subject_id',
            'sstart',
            'send'
        )
        model = BlastResult
