from rest_framework import routers
from .views import RecipeViewSet, topview

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'', topview)
