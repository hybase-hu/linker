import uuid

from django.db import models


# Create your models here.
class WebPage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    browser_session = models.CharField(max_length=100)
    href_to = models.CharField(max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)


class WebRequest(models.Model):

    web_page = models.ForeignKey(WebPage, on_delete=models.CASCADE, related_name="web_requests")
    created_at = models.DateTimeField(auto_now_add=True)
    header = models.TextField()
    ip = models.CharField(max_length=60)
    country = models.CharField(blank=True,null=True,max_length=100)
    city = models.CharField(blank=True,null=True,max_length=100)
    isp = models.CharField(blank=True,null=True,max_length=100)
    region_name = models.CharField(blank=True,null=True,max_length=100)
    location = models.CharField(max_length=200, blank=True, null=True)
