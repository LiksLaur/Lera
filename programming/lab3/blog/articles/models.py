from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,          # обязательно указывать
        related_name="articles",           # полезно для обратных запросов
    )
    text = models.TextField()
    created_date = models.DateTimeField(   # лучшеQ DateTimeField
        auto_now_add=True,
        db_index=True,                     # ускорит сортировку/фильтрацию
    )

    class Meta:
        ordering = ["-created_date"]       # новые статьи сверху
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def __str__(self):
        return f"{self.author.username}: {self.title}"

    def get_excerpt(self):
        """Краткое содержание для списка / админки"""
        if len(self.text) > 140:
            return self.text[:137] + "..."
        return self.text