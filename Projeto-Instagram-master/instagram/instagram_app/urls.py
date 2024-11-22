from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views  
from .views import post_detail

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('add/', views.add_post, name='add_post'),  # URL para a página de adicionar post
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detalhes do post
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'), # rota para a exclusão
    path('edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'), # Editar comentários
]


