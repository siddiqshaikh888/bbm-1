from django import forms
from .models import BlogModel
class CommentForm(forms.Form):
    your_name =forms.CharField(max_length=20)
    comment_text =forms.CharField(widget=forms.Textarea)
 
    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"
 
class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogModel #,'post_date'
        fields = ('blog_title','blog','header_image','author','Category_name')#,'blog_views')
        widgets = {
            'blog_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title Here'}),
            'blog': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            #'post_date': forms.Date(attrs={'class':'form-control'}),
            'Category_name': forms.Select(attrs={'class':'form-control'}),
        }
#class UpdateBlogPostForm(forms.ModelForm):
#    class Meta:
#        model = BlogModel
#        fiels = ['blog_title','blog','header_image','Category_name']
    
#    def save(self, commit=True):
#         blog_post = self.instance
#         blog_post.blog_title = self.cleaned_data['blog_title']
#         blog_post.blog = self.cleaned_data['blog']
#         blog_post.Category_name = self.cleaned_data['category_name']

#         if self.cleaned_data['header_image']:
#             blog_post.header_image = self.cleaned_data['header_image']
#         if commit:
#            blog_post.save()
#         return blog_post