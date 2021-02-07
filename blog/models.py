from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural ='Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=60, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})
         
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural ='Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Tags')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural ='Статьи'
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments', verbose_name='Статья')
    name = models.CharField(max_length=80, verbose_name='Автор')
    email = models.EmailField()
    body = models.TextField(verbose_name='Комментарий')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    active = models.BooleanField(default=False, verbose_name='Выводить на сайт?')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Коментарий'
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

