from django.db import models

# Test model - Contains a set of passages
class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title

# Passage model - Each passage is linked to a specific test
class Passage(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='passages')
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Question for {self.title}"
    
class Paragraph(models.Model):
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE, related_name='paragraphs')
    paragraph = models.TextField()

    def __str__(self):
        return f"Paragraph for {self.passage.title}"

# Question model - Linked to a passage, each passage has multiple questions
class Question(models.Model):
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text

# Choice model - Linked to a question, each question has multiple choices
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class TestScore(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='scores')
    user_name = models.CharField(max_length=100)
    score = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.score} points"

