from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, help_text='Введите описание автора:')

    class Meta:
        ordering = ['user', 'summary']
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.user.id)])
    
    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=2000, help_text='Введите текст поста', verbose_name='Содержание')
    date_of_post = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_of_post', 'title']
        verbose_name = 'Публикация'

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
    
    def __str__(self):
        return '{0}'.format(self.title, self.date_of_post)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000, help_text='Введите комментарий', verbose_name='Комментарий')
    time_of_comment = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    class Meta:
        ordering = ['time_of_comment']
        verbose_name = 'Комментарий'

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.id)])

    def __str__(self):
        return '{0}: {1}. Time: {2}'.format(self.author.username, self.post.title, self.time_of_comment)
