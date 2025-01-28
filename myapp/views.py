from .serializers import ApiResponseSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import AiResponse
from rest_framework.decorators import api_view,permission_classes
from .task import get_ai_response
from celery.result import AsyncResult
from rest_framework.permissions import IsAuthenticated

class AllResponses(generics.ListAPIView):
    queryset = AiResponse.objects.all()
    serializer_class = ApiResponseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        prompt = request.POST.get('input_text')
        task = get_ai_response.apply_async(args=[prompt])
        task_result = AsyncResult(task.id)
        task_result.wait()

        if task_result.ready():
            result = task_result.result

            if result["status"] == "success":
                for i in result.keys():
                    print("keys", i)

                data = AiResponse.objects.create(
                    prompt=prompt,
                    response_text=result["data"]["response"],
                    model_used="gemini-2.0-flash-exp",
                    status="success",
                    processing_time=result["data"]["time_taken"]
                )
                data.save()
                return Response(result, status=status.HTTP_200_OK)

        return Response({"message": result}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SingleResponses(request, pk):
    try:
        response_data = AiResponse.objects.get(pk=pk)
    except AiResponse.DoesNotExist:
        return Response({'error': 'There is no data found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ApiResponseSerializer(instance=response_data)
    return Response(serializer.data, status=status.HTTP_200_OK)
        