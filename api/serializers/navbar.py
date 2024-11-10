from rest_framework import serializers

import basic_app.models as models


class NavbarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Navbar
        fields = ("id", "name", "parent", "slug", "url", "children")
