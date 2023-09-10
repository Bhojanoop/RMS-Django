from django.urls import path
from micro_branch_service.controller.branchmainController import BranchMainController

urlpatterns = [
    path('main',BranchMainController.as_view())
]
