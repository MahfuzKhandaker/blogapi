from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True,unique=True)

    objects=models.Manager()

    def __str__(self): 
        return self.name
    

class Post(models.Model):
    main_image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    number_of_views = models.IntegerField(default=0, null=True, blank=True) 
    number_of_likes = models.IntegerField(default=0, null=True, blank=True) 

    objects = models.Manager()

    class Meta: 
        ordering = ['-publish_date']
 
    def __str__(self): 
        return self.title 

class Comment(models.Model):
    comment_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete= models.CASCADE)

    objects = models.Manager()

    class Meta: 
        # unique_together = ('post', 'comment_by')
        ordering = ['-created_on']

    def __str__(self): 
        return self.comment_text

class Reply(models.Model):
    reply_by = models.ForeignKey(User, related_name='replies', on_delete=models.CASCADE)
    reply_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta: 
       ordering = ['-created_on']

    def __str__(self): 
        return self.reply_text

    

