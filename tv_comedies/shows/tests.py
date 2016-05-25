from django.test import TestCase
from shows.models import Show, Actor, Writer
from shows.utils import create_writer

class ShowTestCase(TestCase):
    def setUp(self):
        Show.objects.create(title='TestShow')
        Show.objects.create(country='FR')
        Show.objects.create(tv_rating='TV-14')

    def testShowFeilds(self):
        showOne = Show.objects.get(title='TestShow')
        showTwo = Show.objects.get(country='FR')
        showThree = Show.objects.get(tv_rating='TV-14')
        self.assertEquals('TestShow', showOne.title)
        self.assertEquals('FR', showTwo.country)
        self.assertEquals('TV-14', showThree.tv_rating)

    def testIsKidFriendly(self):
        showOne = Show.objects.get(tv_rating='TV-14')
        self.assertEquals(False, showOne.is_kid_friendly())

    def testShowManager(self):
        self.assertEquals(3, Show.objects.show_count())

class ActorTestCase(TestCase):
    def setUp(self):
        Actor.objects.create(birth_day='1977-08-04')

    def testAge(self):
        actorOne = Actor.objects.get(id=1)
        self.assertEquals(38, actorOne.age.years)

class testUtils(TestCase):
    def testCreateWriter(self):
        create_writer('Bob Smith', 'Has written many things that are funny')
        writer = Writer.objects.get(id=1)
        self.assertEqual('Bob Smith', writer.name)
