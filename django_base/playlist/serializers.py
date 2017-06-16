from rest_framework import serializers
from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = ('inner', 'real_id', 'channel_id', 'name',
                  'channel_title', 'description',
                  'thumbnails')
