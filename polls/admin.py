from secrets import choice
from django.contrib import admin
from django.forms import fields_for_model
from polls.models import Choice, Question

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields 그룹화
    fieldsets = (
        (None,               {"fields": (['question_text'])}),
        ('Date Information', {"fields": (['pub_date'])}),
    )

    # admin 화면에서 보이는 field, 속성 등 편집
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # inline 집어넣기
    inlines = [ChoiceInline]

    # filter 기능을 추가한다.
    list_filter = ['pub_date']
    # 검색 기능을 추가한다.
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)