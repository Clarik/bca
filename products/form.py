from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    Title = forms.CharField(
                label='Title'
                , widget=forms.TextInput(
                        attrs={
                            'placeholder': 'Input your title here'
                        }
                    )
                )
    Email = forms.EmailField()
    Description = forms.CharField(
                            required=False
                            , widget=forms.Textarea(
                                    attrs={
                                        'class': 'new-class-name two'
                                        , 'id' :  'my-id-for-textarea'
                                        , 'rows' : 20
                                        , 'columns' : 40
                                    }
                                )   
                            )
    Price       = forms.DecimalField(initial=1.99)
    class Meta:
        model = Product
        fields = [
            'Title'
            , 'Description'
            , 'Price'
        ]
    def clean_Title(self, *args, **kwargs):
        Title = self.cleaned_data.get("Title")
        if "RIK" not in Title:
            return Title
        else:
            raise forms.ValidationError("This is not valid title")

    def clean_Email(self, *args, **kwargs):
        Email = self.cleaned_data.get("Email")
        if not Email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return Email


class RawProductForm(forms.Form):
    Title       = forms.CharField(
                            label='Title'
                            , widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Input your title here'
                                    }
                                )
                            )
    Description = forms.CharField(
                            required=False
                            , widget=forms.Textarea(
                                    attrs={
                                        'class': 'new-class-name two'
                                        , 'id' :  'my-id-for-textarea'
                                        , 'rows' : 20
                                        , 'columns' : 40
                                    }
                                )   
                            )
    Price       = forms.DecimalField(initial=1.99)