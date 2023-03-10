"""trunkjunk2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from trunkjunk2api.views import register_user, check_user
from trunkjunk2api.views import UserView, CollectionView, BandanaCollectionView, BandanaView, BandanaColorView, BandanaConditionView, BandanaMarkingView, BandanaPatternView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'collections', CollectionView, 'collection')
router.register(r'bandana_collections', BandanaCollectionView, 'bandana_collection')
router.register(r'bandana_colors', BandanaColorView, 'bandana_color')
router.register(r'bandana_conditions', BandanaConditionView, 'bandana_condition')
router.register(r'bandana_markings', BandanaMarkingView, 'bandana_marking')
router.register(r'bandana_patterns', BandanaPatternView, 'bandana_pattern')
router.register(r'bandanas', BandanaView, 'bandana')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('checkuser', check_user),
    path('', include(router.urls)),
]
