from django.db import models


class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=255)
    class_number = models.CharField(max_length=10)
    class_id = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + str(self.class_number) + '-' + str(self.class_id)


class Book(models.Model):
    book_id = models.IntegerField()
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name + str(self.number) + self.author


class Journal(models.Model):
    id1 = models.ForeignKey(Student, on_delete=models.PROTECT)
    id2 = models.ForeignKey(Book, on_delete=models.PROTECT)
    date_take = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id1) + ' ' + str(self.id2)
