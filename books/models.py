from django.db import models
from functools import total_ordering

# Create your models here.


@total_ordering
class Author(models.Model):
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    middle_names = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        if self.middle_names:
            return f'{self.last_name}, {self.first_name} {self.middle_names}'
        else:
            return f'{self.last_name}, {self.first_name}'

    @property
    def _sort_tuple(self):
        return (self.last_name, self.first_name, self.middle_names)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Author):
            return False

        return self._sort_tuple == o._sort_tuple

    def __lt__(self, o):
        if not isinstance(o, Author):
            return False

        return self._sort_tuple < o._sort_tuple


@total_ordering
class Classmark(models.Model):
    number = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.number} {self.name}'

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Classmark):
            return False

        return self.number == o.number

    def __lt__(self, o):
        if not isinstance(o, Classmark):
            return False

        return self.number < o.number


@total_ordering
class Book(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, null=True)
    classmark = models.ForeignKey(Classmark, on_delete=models.PROTECT)
    author1 = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='author1_set')
    author2 = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='author2_set', blank=True, null=True)
    author3 = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='author3_set', blank=True, null=True)
    author4 = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='author4_set', blank=True, null=True)
    author5 = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='author5_set', blank=True, null=True)

    @property
    def shelf_label(self):
        return f'{self.classmark.number} {self.author1.last_name[:3].upper()}'

    @property
    def _sort_tuple(self):
        return (self.shelf_label,
                self.title,
                self.author1,
                self.author2,
                self.author3,
                self.author4,
                self.author5)

    def __str__(self) -> str:
        return f'[{self.shelf_label}] {self.title}'

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Book):
            return False

        return self._sort_tuple == o._sort_tuple

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Book):
            return False

        return self._sort_tuple < o._sort_tuple
