from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexController.as_view(), name='index'),
    url(r'^books_list/$', views.BookListView.as_view(), name='books'),
    url(r'^books_list/search/$', views.SearchListView.as_view(), name='search_list_view'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
    url(r'^sorry/', views.NotALinkYet.as_view(), name='sorry'),
]
