from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    memo = models.TextField()
    
    def __str__(self):
        return f"ID: {self.id},title: {self.title}, memo: {self.memo}"
    
class Variation(models.Model):
    kind = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"ID: {self.id},kind: {self.kind}, book_id: {self.book_id}"