from django.urls import reverse
from django.test import TestCase
from .models import Task
from .factories import TaskFactory


class TaskViewTests(TestCase):

    def setUp(self):
        self.task = TaskFactory()

    def test_task_list_view(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')
        self.assertContains(response, self.task.title)
        self.assertEqual(len(response.context['tasks']), 1)

    def test_task_detail_view(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_detail.html')
        self.assertContains(response, self.task.title)

    def test_task_create_view(self):
        response = self.client.post(reverse('task-create'), {
            'title': 'Новая задача',
            'description': 'Описание задачи'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)
        new_task = Task.objects.last()
        self.assertEqual(new_task.title, 'Новая задача')

    def test_task_update_view(self):
        response = self.client.post(reverse('task-update', args=[self.task.id]), {
            'title': 'Обновленная задача',
            'description': 'Обновленное описание',
            'completed': True
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Обновленная задача')
        self.assertTrue(self.task.completed)

    def test_task_delete_view(self):
        url = reverse('task-delete', args=[self.task.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
