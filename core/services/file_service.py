from core.models import File
from core.serializers.file_serializer import FileSerializer
from file_storage import exceptions
from file_storage.utils import get_object_or_raise_error


def get_host_url(request):
    return "%s://%s" % (request.scheme, request.get_host())


class FileUploadService:
    def list_files(self, request):
        return FileSerializer(
            File.objects.all(),
            many=True,
            context={"host_url": get_host_url(request)},
        ).data

    def upload_file(self, request, file):
        file_upload_serializer = FileSerializer(
            data={"file": file},
            context={"host_url": get_host_url(request)},
        )

        if not file_upload_serializer.is_valid():
            raise exceptions.Exception(file_upload_serializer.errors)

        file_upload_serializer.save()

        return file_upload_serializer.data

    def retrieve_file(self, request, slug):
        uploaded_file = get_object_or_raise_error(File, slug=slug)

        return FileSerializer(
            uploaded_file, context={"host_url": get_host_url(request)}
        ).data

    def update_file(self, request, slug, file):
        uploaded_file = get_object_or_raise_error(File, slug=slug)

        file_serializer = FileSerializer(
            uploaded_file,
            data={"file": file},
            partial=True,
            context={"host_url": get_host_url(request)},
        )

        if not file_serializer.is_valid():
            raise exceptions.Exception(file_serializer.errors)

        file_serializer.save()

        return file_serializer.data

    def delete_file(self, slug):
        file = get_object_or_raise_error(File, slug=slug)
        file.delete()

        return None
