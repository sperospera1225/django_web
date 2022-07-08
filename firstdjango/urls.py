"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path


from first import views
urlpatterns = [
    path('first/', include('first.urls')), # view 파일의 index 메소드에 연결
    path('second/', include('second.urls')),
    path('third/', include('third.urls')),
    path('admin/', admin.site.urls),
    ]
'''
하나의 프로젝트 내에 여러 앱이 존재할 수 있기 때문에 각 앱에 base path를 지정하고
유지보수를 용이하게 하기 위해 각 웹앱에 urls 라우팅 파일을 정의하고 그 파일을 base path에 맵핑
'''
