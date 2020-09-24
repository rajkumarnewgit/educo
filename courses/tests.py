from django.test import TestCase
from .models import Course ,Subject
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.
class CourseModelTest(TestCase):

    def SetUp(self):

        self.u1 = User.objects.create(username = 'user1')
        self.sub1 = Subject.objects.create(title = 'demo',slug='demo')
        self.course1 = Course.objects.create(owner = self.u1,subject = self.sub1,
                                             title = self.'course1',slug = self.'course1',
                                             overview = self.'demo')
        self.u2 = User.objects.create(username = 'std')
        self.course1.students.add(self.u2)

    def test_course_content(self):

        excepted_object_name = f'{self.course.title}'
        self.asserEqual(excepted_object_name,'course1')

    def test_subject_content(self):

        excepted_object_name = f'{self.sub1.title}'
        self.asserEqual(excepted_object_name,'demo')

    def test_student_field(self):

        std = self.course1.students.values_list('username').first()[0]
        excepted_object_name = f'{std}'
        self.asserEqual(excepted_object_name,'std')

    def test_user(self):

        excepted_object_name = f'{self.u1.username}'
        self.asserEqual(excepted_object_name,'user1')

class CoursePageViewTest(TestCase):

    def SetUp(self):

        self.u1 = User.objects.create(username = 'user1')
        self.sub1 = Subject.ojects.create(title = 'demo',slug = 'demo')
        self.course1 = Course.objects.create(owner = self.u1,subject = self.sub1,title='course1',
                                            slug = 'course1',overview = 'demo' )

        self.u2 = User.objects.create(username = 'std')
        self.course1.student.add(self.u2)

    def test_view_url_exists_at_proper_location(self):

        resp = self.client.get('/')
        self.asserEqual(resp.status_code ,200)

    def test_view_uses_correct_templates(self):

        resp = self.client.get(reverse('course_list'))
        self.asserEqual(resp.status_code ,200)
        self.assertTemplateUsed(resp,'courses/course/list.html')                                                                                                        
