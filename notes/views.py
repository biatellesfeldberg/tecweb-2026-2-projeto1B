from django.shortcuts import render, redirect

# Create your views here.
from .models import Note, Tag

def obter_tag(nome):
    if not nome:
        return None

    nome = nome.strip()
    if nome == '':
        return None

    try:
        # Buscando a tag no banco de dados
        tag = Tag.objects.get(name=nome)
    except Tag.DoesNotExist:
        # Criando uma nova tag no banco de dados
        tag = Tag(name=nome)
        tag.save()

    return tag

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nome_tag = request.POST.get('tag')

        # Buscando a tag existente ou criando uma nova
        tag = obter_tag(nome_tag)

        # Criando uma anotação e vinculando à tag
        note = Note(title=title, content=content, tag=tag)
        note.save()

        return redirect('index')
    
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('index')

def edit(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        nome_tag = request.POST.get('tag')

        # Buscando a tag existente ou criando uma nova
        tag = obter_tag(nome_tag)
        note.tag = tag
        note.save()
        return redirect('index')

    return render(request, 'notes/edit.html', {'note': note})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})

def tag_detail(request, id):
    # Buscando a tag no banco de dados
    tag = Tag.objects.get(id=id)
    notes = tag.note_set.all()
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})
