from rest_framework.views import APIView
from .serializer import ExerciseSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import datetime
from rest_framework import status

class ExerciseView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        exercises = user.exercise_set.all()
        exercise = exercises.filter(date=datetime.date.today())
        serializer = ExerciseSerializer(exercise, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        user = request.user
        
        exercise = data.get('exercise')
        intensity = data.get('intensity')
        duration = data.get('duration')

        exercise = user.exercise_set.create(
            exercise=exercise,
            intensity=intensity,
            duration=duration,
            date=datetime.date.today()
        )
        
        return Response({'success': 'Exercise added'}, status=status.HTTP_200_OK)
