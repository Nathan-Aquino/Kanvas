from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from kanvas_app.models import Activities, Course, Submissions
from kanvas_app.permissions import OnlyInstructor, InstructorAndStaffs, OnlyStudent
from kanvas_app.serializers import ActivitiesSerializer, CourseSerializer, EstudentSubmissionSerializer, SubmissionsSerializer, UserListSerializer, UserSerializer, GradeSubmissionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
import ipdb


class AccountsView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=serializer.validated_data['username']).exists():
            return Response({'error':'user already exist!'},status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(**serializer.validated_data)

        serializer = UserSerializer(user)

        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(**serializer.validated_data)

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key})
        else:
            return Response({'Unauthorized': 'Failed to authenticate'}, status=status.HTTP_401_UNAUTHORIZED)

class CourseView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyInstructor]

    def get(self, request, course_id = ''):
        if course_id:
            # course = get_object_or_404(Course, id=course_id)
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)
        
        course = Course.objects.all()

        serializer = CourseSerializer(course, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        course = Course.objects.get_or_create(**serializer.validated_data)[0]

        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, course_id = ''):
        # course = get_object_or_404(Course, id=course_id)
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({"errors": "invalid course_id"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserListSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        users = serializer.validated_data.pop('user_ids')

        for user in users:
            try:
                student = User.objects.get(id=user)
            except User.DoesNotExist:
                return Response({"errors": "invalid user_id list"}, status=status.HTTP_400_BAD_REQUEST)

            if student.is_staff == False and student.is_superuser == False:
                continue
            else:
                return Response({ "errors": "Only students can be enrolled in the course."}, status=status.HTTP_400_BAD_REQUEST)
        
        course.users.set(users)

        serializer = CourseSerializer(course)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, course_id = ''):
        try:
            course = Course.objects.get(id=course_id)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ActivitiesView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [InstructorAndStaffs]

    def get(self, request):
        activities = Activities.objects.all()

        serializer = ActivitiesSerializer(activities, many=True)

        # ipdb.set_trace()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ActivitiesSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        activity = Activities.objects.get_or_create(**serializer.validated_data)[0]

        serializer = ActivitiesSerializer(activity)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SubmissionsView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyStudent]

    def post(self, request, activity_id = ''):
        serializer = EstudentSubmissionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        repo = serializer.validated_data.pop('repo')

        user = request.user

        activity = Activities.objects.get(id=activity_id)

        data = {
            'repo': repo,
            'user':user,
            'activity':activity
        }

        submission = Submissions.objects.create(**data)

        serializer = SubmissionsSerializer(submission)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, submission_id = ''):
        serializer = GradeSubmissionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        submission = get_object_or_404(Submissions,id=submission_id)

        user = request.user

        self.check_object_permissions(self.request, user)

        submission.grade = serializer.validated_data['grade']
        submission.save()

        serializer = SubmissionsSerializer(submission)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get(self, request):
        if request.user.is_superuser or request.user.is_staff:
            submissions = Submissions.objects.all()

            serializer = SubmissionsSerializer(submissions, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        submissions = Submissions.objects.filter(id=request.user.id).all()

        serializer = SubmissionsSerializer(submissions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

