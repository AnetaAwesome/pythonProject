from django import forms


class BlogPostForm(forms.Form):
    required_css_class = 'required'

    title = forms.CharField(max_length=30, label="Tytuł",
                            widget=forms.TextInput(attrs={'placeholder': "Tytuł posta"}))
    content = forms.CharField(widget=forms.Textarea, label="Treść")

