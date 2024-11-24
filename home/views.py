# views.py

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos, ArtigosRecommends, Category, Tag
from .forms import ArtigoForm
from django.db.models import Q

# Dicionário para mapear o tipo de artigo para o modelo correspondente
ARTICLE_MODELS = {
    'principal': ArtigoPrincipal,
    'secundario': ArtigoSecundario,
    'terceario': ArtigoTerceiro,
    'generico': ArtigosGenericos,
    'recommends': ArtigosRecommends,
}

def initial(request):
    return render(request, 'home/init.html')

def HomeView(request):
    artigoP = ArtigoPrincipal.objects.latest('create_at')
    artigoS = ArtigoSecundario.objects.latest('create_at')
    artigoT = ArtigoTerceiro.objects.latest('create_at')
    artigoGe = ArtigosGenericos.objects.order_by('-create_at').all()
    artigoRe = ArtigosRecommends.objects.order_by('-create_at').all()
    return render(request, 'home/homeview.html', {
        'artigoS': artigoS,
        'artigoP': artigoP,
        'artigoT': artigoT,
        'artigoGe': artigoGe,
        'artigoRe': artigoRe
    })

def Index(request):
    return render(request, 'home/index.html')

def lista_artigos(request):
    artigos_principais = ArtigoPrincipal.objects.all()
    artigos_secundarios = ArtigoSecundario.objects.all()
    artigos_terceiros = ArtigoTerceiro.objects.all()
    return render(request, 'home/lista_artigos.html', {
        'artigos_principais': artigos_principais,
        'artigos_secundarios': artigos_secundarios,
        'artigos_terceiros': artigos_terceiros
    })

def detalhe_artigo(request, id, article_type):
    model = ARTICLE_MODELS.get(article_type)
    if not model:
        return HttpResponse("Tipo de artigo inválido", status=400)
    
    artigo = get_object_or_404(model, id=id)
    return render(request, 'home/detalhe_artigo.html', {
        'artigo': artigo,
        'categories': artigo.categories.all(),
        'tags': artigo.tags.all()
    })


def detalhe_artigo2(request, id):
    artigo_secundario = get_object_or_404(ArtigoSecundario, id=id)
    return render(request, 'home/detalhe_artigo2.html', {'artigo_secundario': artigo_secundario})

def detalhe_artigo3(request, id):
    artigo_terceario = get_object_or_404(ArtigoTerceiro, id=id)
    return render(request, 'home/detalhe_artigo3.html', {'artigo_terceario': artigo_terceario})

def detalhe_artigoGe(request, id):
    artigo_generico = get_object_or_404(ArtigosGenericos, id=id)
    return render(request, 'home/detalhe_artigoGe.html', {'artigo_generico': artigo_generico})

def detalhe_artigoRe(request, id):
    artigo_recommends = get_object_or_404(ArtigosRecommends, id=id)
    return render(request, 'home/detalhe_artigorecommends.html', {'artigo_recommends': artigo_recommends})

def add_content(request, article_type):
    model = ARTICLE_MODELS.get(article_type)
    if not model:
        return HttpResponse("Tipo de artigo inválido", status=400)

    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=model())
        if form.is_valid():
            form.save()
            return redirect('homeview')
    else:
        form = ArtigoForm(instance=model())
    return render(request, 'home/add_content.html', {'form': form, 'article_type': article_type})

def edit_content(request, id, article_type):
    model = ARTICLE_MODELS.get(article_type)
    if not model:
        return HttpResponse("Tipo de artigo inválido", status=400)

    artigo = get_object_or_404(model, id=id)
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('detalhe_artigo', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'home/edit_content.html', {'form': form})



def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        for model in ARTICLE_MODELS.values():
            results += model.objects.filter(
                Q(titulo__icontains=query) | Q(texto__icontains=query)
            )

    return render(request, 'home/search_results.html', {
        'query': query,
        'results': results
    })


def filter_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    results = []
    for model in ARTICLE_MODELS.values():
        results += model.objects.filter(categories=category)
    return render(request, 'home/filter_results.html', {'results': results, 'filter': category.name})

def filter_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    results = ArtigoPrincipal.objects.filter(tags=tag)
    return render(request, 'home/filter_results.html', {'results': results, 'filter': tag.name})
