urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('register/', views.register,name="register"),
]
