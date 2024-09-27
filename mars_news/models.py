from django.db import models

class CategoryEn(models.Model):
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "CategoryEn"
        verbose_name_plural = "CategoryEn"

    def __str__(self):
        return self.title

class NewsEn(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="news_en/images")
    video = models.FileField(upload_to="news_en/videos")
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategoryEn, on_delete=models.CASCADE, related_name="news")
    
    class Meta:
        verbose_name = "NewsEn"
        verbose_name_plural = "NewsEn"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title