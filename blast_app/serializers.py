from rest_framework import serializers

from .models import BlastQuery, BlastResult


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

    def __str__(self):
        return '%d: %s' % (self.order, self.title)


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
