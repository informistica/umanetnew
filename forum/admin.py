from django.contrib import admin
from django import forms
from .models import Discussione, Post, Sezione, Classe, School
from ckeditor.widgets import CKEditorWidget
# Register your models here.

class ScuolaModelAdmin(admin.ModelAdmin):
    model = School

class ClasseModelAdmin(admin.ModelAdmin):
    model = Classe

class DiscussioneModelAdmin(admin.ModelAdmin):
    model = Discussione
    list_display = ["titolo", "sezione_appartenenza", "autore_discussione"]
    search_fields = ["titolo", "autore_discussione"]
    list_filter = ["sezione_appartenenza", "data_creazione"]

class PostModelAdmin(admin.ModelAdmin):
    contenuto = forms.CharField(widget=CKEditorWidget())
    model = Post
    list_display = ["autore_post", "discussione"]
    search_fields = ["contenuto"]
    list_filter = ["data_creazione", "autore_post"]

class SezioneModelAdmin(admin.ModelAdmin):
    contenuto = forms.CharField(widget=CKEditorWidget())
    model = Sezione
    list_display = ["nome_sezione", "descrizione"]



admin.site.register(School, ClasseModelAdmin)
admin.site.register(Classe, ClasseModelAdmin)
admin.site.register(Discussione, DiscussioneModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Sezione, SezioneModelAdmin)
