from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()  # 質問のテキストを保存するフィールド
    created_at = models.DateTimeField(auto_now_add=True)  # 質問が作成された日時

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # 質問との関連付け
    answer_text = models.TextField()  # 回答のテキストを保存するフィールド
    created_at = models.DateTimeField(auto_now_add=True)  # 回答が作成された日時

    def __str__(self):
        return self.answer_text