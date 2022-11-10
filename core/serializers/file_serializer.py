from rest_framework import serializers

from core.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    def to_representation(self, instance):
        instance = super().to_representation(instance)

        # update file to have `host_url`
        instance["file"] = (
            "%s%s" % (self.context["host_url"], instance["file"])
            if self.context.get("host_url")
            else instance["file"]
        )

        return instance
