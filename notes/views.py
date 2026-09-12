from django.shortcuts import render, redirect

# Create your views here.
from .models import Note, Tag


def obter_tags(nomes):
    tags = []
    if not nomes:
        return tags

    for nome in nomes.split(','):
        nome = nome.strip()
        if nome == '':
            continue

        tag, created = Tag.objects.get_or_create(name=nome)
        tags.append(tag)

    return tags


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nomes_tags = request.POST.get('tag')

        # A nota precisa ser salva antes de associar tags (ManyToMany)
        note = Note(title=title, content=content)
        note.save()

        tags = obter_tags(nomes_tags)
        if tags:
            note.tags.add(*tags)

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
        note.save()

        tags = obter_tags(request.POST.get('tag'))
        note.tags.set(tags)
        return redirect('index')

    tags_value = ', '.join(tag.name for tag in note.tags.all())
    return render(request, 'notes/edit.html', {
        'note': note,
        'tags_value': tags_value,
    })


def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})


def tag_detail(request, id):
    # Buscando a tag no banco de dados
    tag = Tag.objects.get(id=id)
    notes = tag.note_set.all()
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes})
