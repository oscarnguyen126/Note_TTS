from django.shortcuts import render,get_object_or_404,redirect
from .models import Note,Folder
from .serializers import NoteSerializer,FolderSerializer

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html',context={'notes': notes})

def note_detail(request,slug):
    notes = get_object_or_404(Note, slug=slug)
    return render(request,template_name='note_detail.html',context={'notes': notes})

def note_create(request):
    return redirect('note_list.html')

def note_update(request,slug):
    return redirect('note_list.html')

def note_delete(request,slug):
    return redirect('note_list.html')

def folder_list(request):
    folders = Folder.objects.all()
    return render(request, template_name='folder_list.html',context={'folders':folders})

def folder_detail(request,slug):
    folders = get_object_or_404(Folder,slug)
    return render(request,template_name='folder_detail',context={'folders':folders})

def folder_create(request):
    return render(request,template_name='folder_list.html',context={'folders':folders})

def folder_update(request,slug):
    return redirect('folder_list')

def folder_delete(request,slug):
    return redirect('folder_list.html')





