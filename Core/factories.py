import factory
from .models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    completed = factory.Faker('boolean')

    class Meta:
        model = Task
