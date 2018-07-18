# blog/urls.py를 복사했음.
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='index'),
    #사용자가 장고서버에 데이터를 요청하면
    # 블로그 가장 상위의 url인 blog/urls.py를 참고한다.
    # 그래서 feed.urls를 접근하게 된다. 왜냐하면 blog/urls.py의 처음에
    # url(r'^', include('feed.urls')),로 정의해놨기때문에.
    # 그리고 feed.urls에 넘겨진 값이 아무것도 없으면 index를 표기해주고
    # localhost:8000/1과 같은 페이지에 접근하고자 한다면 view detail안에 있는
    # 데이터를 꺼내서 보여주겠다. 라는 것이다.
    # Including other URLconfs 참고
    # url(r'^$', views.about, name='index'),
]

# 정규식 시작 ^
# 정규식 끝 $
