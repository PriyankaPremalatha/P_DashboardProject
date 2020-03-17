from django.urls import path
from supportteamapp import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns=[

	path("sregister/",views.sregister,name="sregister"),
	path("slogin/",views.slogin,name="slogin"),
	path("",views.sindex,name="sindex"),
	path("onsite/",views.onsite,name="onsite"),

]