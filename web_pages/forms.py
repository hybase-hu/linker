from django.forms import  ModelForm

from web_pages.models import WebPage


class WebPageForm(ModelForm):
    class Meta:
        model = WebPage
        fields = ["href_to",]

    def __init__(self, *args, **kwargs):
        super(WebPageForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control bg-primary text-light'