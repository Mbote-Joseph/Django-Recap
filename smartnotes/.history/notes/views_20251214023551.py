from django.shortcuts import get_object_or_404, render
from django.db import models
from django.template.context_processors import request
from django.http import Http404, HttpResponseRedirect
from django.apps import apps
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Notes
# Create your views here.

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = "/login"
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gt = 3)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/note_detail.html'
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    fields = '__all__'
    template_name = 'notes/note_form.html' # Create this template in your templates folder
    success_url = '/notes' # Change to your success URL name
    # Optional: Override http_method_names if you only want 'get' and 'post'
    http_method_names = ['get', 'post', 'head', 'options']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class NoteUpdateView(UpdateView):
    model = Notes
    fields = '__all__'
    template_name = 'notes/note_form.html' 
    success_url = '/notes'
    http_method_names = ['get', 'post', 'head', 'options']
    
class NoteDeleteView(DeleteView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/note_confirm_delete.html' 
    success_url = '/notes'
    
    
def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse('note.details', args=[pk]))
    raise Http404
        
def change_visibility_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse('note.details', args=[pk]))
    raise Http404

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

# def note_details(request, pk):
#     try:
#         note_detail = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note Doesn't exist")
#     return render(request, 'notes/note_detail.html', {'note_detail': note_detail})