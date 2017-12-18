import os
from django.db import models


def get_path(inst, filename):
    """
    :param inst: Child object
    :param filename: myPhoto.jpg
    :return: 'photo/2/myPhoto.jpg
    """
    result = os.path.join('photo', inst.id, filename)
    return result


class Child(models.Model):
    GENDER = (
        ('B', 'BOY'),
        ('G', 'GIRL')
    )

    CLASSROOMS = (
        ('CLASS_1', 'Class one'),
        ('CLASS_2', 'Class two'),
        ('CLASS_3', 'Class three'),
    )

    photo = models.ImageField(
        upload_to=get_path,
        verbose_name='Child photo',
        null=True
    )
    name = models.CharField(
        max_length=128,
        verbose_name='Child name'
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default='G',
        verbose_name='Child gender'
    )
    birthday = models.DateField(
        verbose_name='Child birthday'
    )
    classroom = models.CharField(
        max_length=7,
        choices=CLASSROOMS,
        default='CLASS_1',
        verbose_name='Child class'
    )
    learn = models.BooleanField(
        default=False,
        verbose_name='Learn'
    )


class Parents(models.Model):
    child = models.OneToOneField(
        Child,
        related_name='parents',
        verbose_name='Parents'
    )
    mother = models.CharField(max_length=128, verbose_name='Mother name')
    father = models.CharField(max_length=128, verbose_name='Father name')

    def __str__(self):
        return f'{self.mother}, {self.father}'


class Journal(models.Model):
    child = models.ForeignKey(
        Child,
        related_name='journal',
        verbose_name='Child'
    )
    bring_time = models.DateTimeField(
        verbose_name='Time when bring child to childhood'
    )
    pick_up_time = models.DateTimeField(
        verbose_name='Time when pick up child from childhood',
        blank=True,
        null=True
    )
    date = models.DateTimeField(auto_now_add=True)

    @property
    def parents(self):
        return self.child.parents

    class Meta:
        ordering = ['date']
