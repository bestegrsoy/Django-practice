from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()

    author=models.ForeignKey(Author, on_delete=models.CASCADE) # on_Delete=Cascade Author silindiğinde Post'unda silinmesini sağlar 
    tag=models.ManyToManyField(Tag, blank=True) # blank=true boş bırakılabilir demek 

    def __str__(self):
        return self.title # sorgu sırasında title'ın gelmesine sebep olur.