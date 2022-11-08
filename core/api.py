from file_storage.decorators import handle_errors
from file_storage.utils import BaseView
from rest_framework import status
from rest_framework.response import Response

from core.service import FileUploadService

file_upload_service = FileUploadService()


class ListCreateFileAPI(BaseView):
    @handle_errors()
    def get(self, request):
        return Response(
            file_upload_service.list_files(request), status=status.HTTP_200_OK
        )

    @handle_errors()
    def post(self, request):
        file = request.FILES.get("file")
        return Response(
            file_upload_service.upload_file(request, file),
            status=status.HTTP_201_CREATED,
        )


class GetUpdateDeleteFileAPI(BaseView):
    @handle_errors()
    def get(self, request, slug):
        return Response(
            file_upload_service.retrieve_file(request, slug), status=status.HTTP_200_OK
        )

    @handle_errors()
    def put(self, request, slug):
        file = request.FILES.get("file")
        return Response(
            file_upload_service.update_file(request, slug, file),
            status=status.HTTP_200_OK,
        )

    @handle_errors()
    def delete(self, request, slug):
        return Response(
            file_upload_service.delete_file(slug),
            status=status.HTTP_204_NO_CONTENT,
        )
