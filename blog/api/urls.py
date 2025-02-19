from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from blog.api.views import PostViewSet, UserDetail, TagViewSet


router = DefaultRouter()
router.register("tags", TagViewSet)
router.register(
    "posts", PostViewSet
)  # u can add basename  arg to the register if u want to change the name

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url="http://127.0.0.1:8000/api/v1/",
    public=True,
)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
    # path("token-auth/", views.obtain_auth_token),
    path('jwt/',TokenObtainPairView.as_view(), name = 'jwt_obtain_pair'),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),

    # re_path(
    #     r"^swagger(?P<format>\.json|\.yaml)$",
    #     schema_view.without_ui(cache_timeout=0),
    #     name="schema-json",
    # ),
    # path(
    #     "swagger/",
    #     schema_view.with_ui("swagger", cache_timeout=0),
    #     name="schema-swagger-ui",
    # ),
    path(
        "posts/by-time/<str:period_name>/",
        PostViewSet.as_view({"get": "list"}),
        name="posts-by-time",
    ),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
