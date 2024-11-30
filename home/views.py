from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Artigo, Category, Tag
from .forms import ArtigoForm
from django.db.models import Max
from django.db.models import Q


def initial(request):
    return render(request, 'home/init.html')


def HomeView(request):
    artigoP = Artigo.objects.filter(tipo='principal').order_by('-create_at').first()
    artigoS = Artigo.objects.filter(tipo='secundario').order_by('-create_at').first()
    artigoT = Artigo.objects.filter(tipo='terciario').order_by('-create_at').first()
    artigoGe = Artigo.objects.filter(tipo='generico').order_by('-create_at')
    artigoRe = Artigo.objects.filter(tipo='recomendado').order_by('-create_at')

    context = {
        'artigoP': artigoP,
        'artigoS': artigoS,
        'artigoT': artigoT,
        'artigoGe': artigoGe,
        'artigoRe': artigoRe,
    }
    return render(request, 'home/homeview.html', context)


def Index(request):
    return render(request, 'home/index.html')


def lista_artigos(request):
    # Recuperar todos os artigos, organizados por tipo
    artigos = Artigo.objects.all().order_by('-create_at')
    return render(request, 'home/lista_artigos.html', {'artigos': artigos})


def detalhe_artigo(request, id):
    # Recuperar o artigo pelo ID
    artigo = get_object_or_404(Artigo, id=id)
    return render(request, 'home/detalhe_artigo.html', {
        'artigo': artigo,
        'categories': artigo.categories.all(),
        'tags': artigo.tags.all()
    })


def add_content(request):
    # Adicionar um novo artigo
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homeview')
    else:
        form = ArtigoForm()
    return render(request, 'home/add_content.html', {'form': form})


def edit_content(request, id):
    # Editar um artigo existente
    artigo = get_object_or_404(Artigo, id=id)
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('detalhe_artigo', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'home/edit_content.html', {'form': form})


def search_results(request):
    # Implementar busca por título ou texto
    query = request.GET.get('q')
    results = []
    if query:
        results = Artigo.objects.filter(
            Q(titulo__icontains=query) | Q(texto__icontains=query)
        )
    return render(request, 'home/search_results.html', {
        'query': query,
        'results': results
    })


def filter_by_category(request, category_id):
    # Filtrar artigos por categoria
    category = get_object_or_404(Category, id=category_id)
    results = Artigo.objects.filter(categories=category)
    return render(request, 'home/filter_results.html', {'results': results, 'filter': category.name})


def filter_by_tag(request, tag_id):
    # Filtrar artigos por tag
    tag = get_object_or_404(Tag, id=tag_id)
    results = Artigo.objects.filter(tags=tag)
    return render(request, 'home/filter_results.html', {'results': results, 'filter': tag.name})
