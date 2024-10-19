from rest_framework import serializers

from apps.dashboard.models import ParsedSessions

class ParsedSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParsedSessions
        fields = ('id',
                  'session',
                  'raw_json',
                  'parsed_json',
                  'feedback',
                  'band_score',
                  'fluency',
                  'vocabulary',
                  'grammar',
                  'pronunciation',
                  'used_topic_words',
                  'suggested_vocab',
                  'token_usage',
                  'wait_time',
                  'created_at')
        
        ref_name = "ParsedSessionsSerializer"  