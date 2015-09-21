from django.db import models
from django.conf import settings


class Page(models.Model):

    name = models.CharField(max_length=32)
    width = models.FloatField()
    height = models.FloatField()
    quantity = models.IntegerField()

    def __unicode__(self):
        return self.name


class PostItModel(models.Model):

    width = models.FloatField()
    height = models.FloatField()

    def __unicode__(self):
        return '%smm x %smm' % (self.width, self.height)

    def adjust_height(self):
        return self.height - (settings.PADDING * 2) - settings.BORDER

    def adjust_width(self):
        return self.width - (settings.PADDING * 2) - settings.BORDER


class PrintPage(models.Model):

    page = models.ForeignKey(Page)
    post_it_model = models.ForeignKey(PostItModel)


class PostIt(models.Model):

    title = models.CharField(max_length=12)
    body = models.CharField(max_length=512)
    outside_code = models.CharField(null=True, blank=True, max_length=32)
    print_page = models.ForeignKey(PrintPage, related_name='posts')

    def __unicode__(self):
        return self.title

