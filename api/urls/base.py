from django.urls import path, include

urlpatterns = [
    path("news/", include("api.urls.news")),
    path("posts/", include("api.urls.posts")),
    path("navbar/", include("api.urls.navbar")),
    path("interactive-map/", include("api.urls.interactive_map")),
]
