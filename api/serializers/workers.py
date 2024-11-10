from rest_framework import serializers

import basic_app.models as models


class AdministratorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrator
        fields = ("id", "f_name", "image", "phone", "position", "email", "admission_days")


class AdministratorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrator
        fields = "__all__"
