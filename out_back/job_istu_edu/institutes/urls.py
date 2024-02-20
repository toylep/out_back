from django.urls import path
from institutes.views import (
    SpecialityView,
    SpecialitySingleView,
    InstituteView,
    InstituteSingleView,
)


urlpatterns = [
    path('speciality/', SpecialityView.as_view()),
    path('', InstituteView.as_view()),
    path('<int:pk>', InstituteSingleView.as_view()),
    path('speciality/<int:pk>', SpecialitySingleView.as_view())
]