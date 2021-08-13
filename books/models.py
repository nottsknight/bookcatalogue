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

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Author):
            return False

        return ((self.last_name, self.first_name, self.middle_names) ==
                (o.last_name, o.first_name, o.middle_names)
                )

    def __lt__(self, o):
        if not isinstance(o, Author):
            return False

        return ((self.last_name, self.first_name, self.middle_names) <
                (o.last_name, o.first_name, o.middle_names)
                )


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
