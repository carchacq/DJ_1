from django.contrib import admin

from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tag_counter += 1
        if main_tag_counter == 0:
            raise ValidationError('Установите основной тег')
        if main_tag_counter > 1:
            raise ValidationError('Можно установить только один основной тег')
        return super().clean()
class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
