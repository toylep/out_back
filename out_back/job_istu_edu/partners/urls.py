from django.urls import path
from partners.views import (
    PracticeView,
    PracticeSingleView,
    PartnerView,
    PartnerSingleView,
    DocLinkView,
    DocLinkSingleView
)

urlpatterns = [
    path('practice/', PracticeView.as_view()),
    path('', PartnerView.as_view()),
    path('docs/', DocLinkView.as_view()),
    path('practice/<int:pk>', PracticeSingleView.as_view()),
    path('<int:pk>', PartnerSingleView.as_view()),
    path('docs/<int:pk>', DocLinkSingleView.as_view()),
]