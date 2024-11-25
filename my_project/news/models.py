from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    announcement = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date Posting')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
