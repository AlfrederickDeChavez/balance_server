from rest_framework.views import APIView
from .serializer import FoodSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import datetime
from rest_framework import status

class FoodView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        foods = user.food_set.all()
        intake = foods.filter(date_consumed=datetime.date.today())
        serializer = FoodSerializer(intake, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        user = request.user
        category = data['Category']
        name = data['Name']
        quantity = data['Quantity']
        calories = data['Calories']
        protein = data['Protein']
        dietary_fiber = data['DietaryFiber']
        vitamin_A = data['Vitamin_A']
        vitamin_D = data['Vitamin_D']
        vitamin_E = data['Vitamin_E']
        vitamin_K = data['Vitamin_K']
        thiamin = data['Thiamin']
        riboflavin = data['Riboflavin']
        niacin = data['Niacin']
        vitamin_B6 = data['Vitamin_B6']
        vitamin_B12 = data['Vitamin_B12']
        folate = data['Folate']
        vitamin_C = data['Vitamin_C']
        iron = data['Iron']
        zinc = data['Zinc']
        selenium = data['Selenium']
        iodine = data['Iodine']
        calcium = data['Calcium']
        magnesium = data['Magnesium']
        phosphorus = data['Phosphorus']
        flouride = data['Flouride'] 
        sodium = data['Sodium']
        chloride = data['Chloride']
        potassium = data['Potassium']

        food = user.food_set.create(
            name=name,
            category=category,
            quantity=quantity,
            calories=calories,
            protein=protein,
            dietary_fiber=dietary_fiber, 
            vitamin_A=vitamin_A,
            vitamin_D=vitamin_D,
            vitamin_E=vitamin_E,
            vitamin_K=vitamin_K,
            thiamin=thiamin,
            riboflavin=riboflavin,
            niacin=niacin,
            vitamin_B6=vitamin_B6,
            vitamin_B12=vitamin_B12,
            folate=folate,
            vitamin_C=vitamin_C,
            iron=iron,
            zinc=zinc,
            selenium=selenium,
            iodine=iodine,
            calcium=calcium,
            magnesium=magnesium,
            phosphorus=phosphorus,
            flouride=flouride,
            sodium=sodium,
            chloride=chloride,
            potassium=potassium,
            date_consumed=datetime.date.today()
        )
        
        return Response({'success': 'Food Added Successfully'}, status=status.HTTP_200_OK)
