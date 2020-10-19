from django.conf.urls import url

from . import views

app_name='posts'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"), #url halaman utama post, kasih liat list post
    url(r"new/$", views.CreatePost.as_view(), name="create"), #url buat post
    url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"), #url liat list post yg dibuat user tsb (pk)
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"), #url liat detail post yg dibuat user tsb (pk)
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"), #url delete post tertentu (pk)
]
