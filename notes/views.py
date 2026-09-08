from django.shortcuts import render, redirect

# Create your views here.
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title=title, content=content)
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
        note.save()
        return redirect('index')

    return render(request, 'notes/edit.html', {'note': note})
