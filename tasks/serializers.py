from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        title = value.strip()

        if not title:
            raise serializers.ValidationError(
                "O título da tarefa não pode ficar vazio."
            )

        return title

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "completed",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]