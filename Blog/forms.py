from django import forms
from .models import Comment,Post, Image


class Posting(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtítulo'}), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe el contenido aquí...'}),
        }



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostSearchForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    username = forms.CharField(required=False, max_length=100)