from rest_framework import serializers

from apps.dashboard.models import ParsedSessions, SchoolProfiles

class ParsedSessionSerializer(serializers.ModelSerializer):
    session_source = serializers.SerializerMethodField()

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
                  'created_at',
                  'session_source')
        
        ref_name = "ParsedSessionsSerializer"

    def get_session_source(self, obj):
        if obj.session.school.id == 6:
            return 'bot'
        elif obj.session.school.id == 7:
            return 'sayra'
        return None
