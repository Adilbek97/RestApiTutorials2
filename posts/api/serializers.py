from rest_framework import serializers
from posts.models import Lead, Book, Teacher, Student, Subject, Questions, Result


# Lead Serializers
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=True)
    results = ResultSerializers(many=True)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'questions', 'results')


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True, write_only=False)

    # results = ResultSerializers(many=True)

    class Meta:
        model = Teacher
        fields = ('id', 'firstName', 'lastName', 'login', 'password', 'subjects')


class StudentSerializer(serializers.ModelSerializer):
    results = ResultSerializers(many=True, read_only=True, write_only=False)

    class Meta:
        model = Student
        fields = ('id', 'firstName', 'lastName', 'login', 'password', 'results')
