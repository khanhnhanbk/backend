from django.urls import include, path

# BASE_URL / api /  + ...
urlpatterns = [
    path("auth/", include("authentication.urls")),
]
