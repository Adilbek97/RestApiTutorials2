from posts.models import Lead, Book, Teacher, Student, Subject, Questions, Result
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, BookSerializer, TeacherSerializer, StudentSerializer, SubjectSerializer, \
    QuestionsSerializer, ResultSerializers
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters


# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BookSerializer


class TeacherFilter(filters.FilterSet):
    login = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ('login', 'password')


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    # serializer_class = TeacherSerializer
    # authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated, )
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

    # filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Teacher.objects.filter()


#           Token is: c268a06f1e21a5ff327268762c898df1f2683113


class StudentFilter(filters.FilterSet):
    login = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ('login', 'password')


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer
    filterset_class = StudentFilter


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionsSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ResultSerializers
