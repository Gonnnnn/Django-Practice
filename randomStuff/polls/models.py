import datetime
from django.utils import timezone
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # admin 페이지 관리를 위해 추가하는 부분
    # 임의의 메서드에 의한 값은 정렬이 불가능하다. 따라서 다른 값을 기준으로 정렬하도록 한다
    was_published_recently.admin_order_field = 'pub_date'
    # True, False에 따라 아이콘으로 표기된다
    was_published_recently.boolean = True
    # 항목의 헤더 설정
    was_published_recently.short_description = 'Published recently'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text