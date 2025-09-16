from .models import Stadium
from .serializers import StadiumSerializer
from .permissions import IsOwnerCreated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from drf_spectacular.utils import extend_schema

class StadionListView(APIView):
    def get(self, request):
        stadiums = Stadium.objects.all()
        serializer = StadiumSerializer(stadiums, many=True)
        return Response(serializer.data)

@extend_schema(request=StadiumSerializer)
class StadionCreateView(APIView):
    def post(self, request):
        print(request.user.role)
        print(request.user)
        if request.user.role != "owner":
            raise ValidationError({"errors": "Faqat owner stadion qo‘shishi mumkin!"})

        serializer = StadiumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # owner avtomatik yoziladi
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(request=StadiumSerializer)
class StadionUpdateView(APIView):
    def put(self, request, id):
        try:
            stadium = Stadium.objects.get(id=id)
        except Stadium.DoesNotExist:
            raise ValidationError({"errors": "Stadion topilmadi !!!"})

        serializer = StadiumSerializer(stadium, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=StadiumSerializer)
class StadionDeleteView(APIView):
    def delete(self,request,id):
        stadium = Stadium.objects.filter(id=id)
        print(stadium)
        if stadium:
            stadium.delete()
            return Response({"success":"stadion o'chirildi!  "})
        raise ValidationError({"ERRORS":"STADION TOPILMADII!!!!!!!!!"})



# class StadionListView(ListAPIView):
#
#
# class StadionUpdateView(UpdateAPIView):
#
#
#
# class StadionDeleteView(DestroyAPIView):

