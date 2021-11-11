import os
import shutil

from django.http import FileResponse
from django_analyses.models.run import Run
from django_analyses.serializers.run import RunSerializer
from django_analyses.views.pagination import StandardResultsSetPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=True, methods=["get"])
    def to_zip(self, request: Request, pk: int) -> FileResponse:
        instance = Run.objects.get(id=pk)
        base_dir = root_dir = str(instance.path)
        name = str(instance.id)
        archive = shutil.make_archive(name, "zip", base_dir, root_dir)
        response = FileResponse(open(archive, "rb"), as_attachment=True)
        os.unlink(archive)
        return response
