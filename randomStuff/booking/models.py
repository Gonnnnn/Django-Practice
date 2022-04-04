from django.conf import settings
from django.db import models

# Create your models here.
class Booking(models.Model):
    # AUTH_USER_MODEL -> 추후 더 알아볼것
    # PROTECT -> 게시글에 코멘트가 있으면 게시글을 지울 수 없는 것과 같은 내용
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='bookings')

    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    room = models.CharField(max_length=100)
    note = models.TextField()

    # auto_now_add -> 최초 저장시 현재 시각 저장
    # auto_now -> 수정될 때마다 현재 시각 저장
    # https://tomining.tistory.com/145
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriber.username + ' ' + self.room
    
    class Meta:
        ordering = ['-date_from']
