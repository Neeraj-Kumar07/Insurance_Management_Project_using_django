from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Policy, PolicyRecord, Question

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'sum_assured', 'premium', 'tenure']

@admin.register(PolicyRecord)
class PolicyRecordAdmin(admin.ModelAdmin):
    list_display = ['customer', 'policy', 'purchase_date', 'expiry_date']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['policy', 'question_text']
