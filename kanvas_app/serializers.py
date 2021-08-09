from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(required=False)

class SimpleUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    users = SimpleUserSerializer(many=True, required=False)

class UserListSerializer(serializers.Serializer):
    user_ids = serializers.ListField()

class SubmissionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    grade = serializers.IntegerField(allow_null=True)
    repo = serializers.CharField()
    user_id = serializers.IntegerField()
    activity_id = serializers.IntegerField()

class EstudentSubmissionSerializer(serializers.Serializer):
    grade = serializers.IntegerField(allow_null=True)
    repo = serializers.CharField()

class ActivitiesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    points = serializers.IntegerField()
    submissions = SubmissionsSerializer(many=True, required=False)