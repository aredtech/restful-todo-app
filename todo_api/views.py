from . import serializers
from todo.models import Todo
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
class TodosViewset(viewsets.ViewSet):
    def list(self, request):
        todo = Todo.objects.all()
        serializer = serializers.TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            todo = Todo.objects.get(id=id)
            serializer = serializers.TodoSerializer(todo)
            return Response(serializer.data)

    def create(self, request):
        serializer = serializers.TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Todo Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = serializers.TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request,pk):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = serializers.TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Updated Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        todo = Todo.objects.get(pk=id)
        todo.delete()
        return Response({"msg":"Todo Deleted"})