from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=spiderman, type='Running', duration=30, date='2023-01-01')
        Workout.objects.create(name='Cardio', description='Cardio workout')
        Leaderboard.objects.create(user=spiderman, score=100)

    def test_user_team(self):
        user = User.objects.get(email='spiderman@marvel.com')
        self.assertEqual(user.team.name, 'Marvel')

    def test_leaderboard(self):
        entry = Leaderboard.objects.get(user__email='spiderman@marvel.com')
        self.assertEqual(entry.score, 100)
