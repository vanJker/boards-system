from django.test import TestCase
from django.urls import reverse, resolve
from boards.models import Board
from boards.views import TopicListView

class BoardTopicsTests(TestCase):
    def setUp(self) -> None:
        Board.objects.create(name='好词', description='这是关于好词的素材版')
    
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_navigation_link(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        home_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(home_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))

