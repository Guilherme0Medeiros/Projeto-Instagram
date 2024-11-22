from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all()  # Pega todos os posts
    comment_form = CommentForm()  # Cria um formulário vazio para os comentários

    if request.method == 'POST':
        post_id = request.POST.get('post_id')  # Pega o ID do post
        post = get_object_or_404(Post, id=post_id)  # Pega o post correspondente
        form = CommentForm(request.POST)  # Cria o formulário de comentário

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associa o comentário ao post
            comment.user = request.user  # Associa o comentário ao usuário logado
            comment.save()  # Salva o comentário no banco de dados

            return redirect('index')  # Redireciona para a página inicial com o novo comentário

    return render(request, 'instagram_app/index.html', {
        'posts': posts,
        'comment_form': comment_form,
    })

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Recebe os dados do formulário e arquivos
        if form.is_valid():
            form.save()  # Salva o post no banco de dados
            return redirect('index')  # Redireciona para a página de feed após salvar o post
    else:
        form = PostForm()  # Se não for um POST, exibe o formulário vazio
    
    return render(request, 'instagram_app/add_post.html', {'form': form})

# Sistema de Comentários

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Pega o post com o ID fornecido
    comments = post.comments.all()  # Obtém todos os comentários do post
    form = CommentForm()  # Cria o formulário de comentário

    # Se o método for POST, significa que alguém está tentando enviar um comentário
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associa o comentário ao post
            comment.user = request.user  # Associa o comentário ao usuário logado
            comment.save()  # Salva o comentário no banco de dados
            return redirect('post_detail', post_id=post.id)  # Redireciona para a página de detalhes do post

    # Contexto para passar para o template
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'instagram_app/post_detail.html', context)  # Passa para o template

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Verifica se o usuário é o autor do comentário
    if comment.user == request.user:
        comment.delete()  # Exclui o comentário
        return redirect('index')  # Redireciona para a página principal
    else:
        return redirect('index')  # Redireciona caso o usuário não seja autorizado


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Verifica se o usuário é o autor do comentário
    if comment.user != request.user:
        return redirect('index')  # Redireciona se o usuário não for o autor

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # Preenche o form com o comentário existente
        if form.is_valid():
            form.save()  # Salva as mudanças
            return redirect('index')  # Redireciona para o feed
    else:
        form = CommentForm(instance=comment)  # Preenche o form com os dados atuais do comentário

    return render(request, 'instagram_app/edit_comment.html', {'form': form, 'comment': comment})
