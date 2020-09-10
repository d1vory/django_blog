from django.forms import ModelForm
from .models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']
    #
    # def clean_photo(self):
    #     data = self.data['photo']
    #     return data
