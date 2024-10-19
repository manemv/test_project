from django.contrib import admin
from .models import Test, Passage, Paragraph, Question, Choice

# Inline for Choice model under Question
class ChoiceInline(admin.TabularInline):
    model = Choice

# Inline for Question model under Passage
class QuestionInline(admin.StackedInline):
    model = Question
    inlines = [ChoiceInline]  # Remove this, as nested inlines are not supported.

#Inline for Paragraph model under Passage
class ParagraphInline(admin.StackedInline):
    model = Paragraph

# Admin class for Passage to display paragraphs and questions inline
@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline, QuestionInline]  # Show Paragraphs and Questions inline under Passage

# Admin class for Question to display choices inline
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Show Choices inline under Question

admin.site.register(Test)
