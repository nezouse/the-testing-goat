from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    @property
    def name(self):
        return self.item_set.first().text


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering: ('id')
        order_with_respect_to = 'list'
        unique_together = ('list', 'text')
