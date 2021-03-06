from django.db import models


class Announce(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='announces_announces', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    announce = models.ForeignKey(Announce, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='announces_comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
