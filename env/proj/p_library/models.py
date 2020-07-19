from django.db import models


class Publishing(models.Model):
    name = models.CharField(max_length=20, default='')
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Friend(models.Model):
    full_name = models.CharField(max_length=25, default='', null=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    ISBN = models.CharField(db_column='ISBN', max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=5, blank=True, null=True)
    copy_count = models.SmallIntegerField(blank=True, null=True)
    publishing = models.ForeignKey(
        Publishing, on_delete=models.CASCADE, related_name='publish', null=True)
    debeter = models.ManyToManyField(
        'Friend', through='Exchange', through_fields=('book', 'friend'), blank=True)
    cover = models.ImageField(
        upload_to='covers/', blank=True)

    # Я решил сделать связь ManyToMany дабы учесть возможность выдачи одной
    # книги нескольким друзьям. В конце концов, FOreignKey мы уже обсосали со всех сторон
    # в прошлых ДЗ. Но если тебе нужен именно один-ко-многим, то раскомментируй debeter ниже.
    # debeter = models.ForeignKey(
    #     Friend, models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title


class Exchange(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(
        Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book.title} у {self.friend.full_name}'
