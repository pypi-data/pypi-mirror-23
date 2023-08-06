Usage:

```python
from django.db import models
from django_joining import JoiningKey


class ModelA(models.Model):

    foo = models.IntegerField()
    bar = models.IntegerField()
    baz = models.TextField()

    model_b = JoiningKey('ModelB',
        from_fields=['foo', 'bar'],
        to_fields=['qux', 'quux'],
        related_name='model_a_set'
        )


class ModelB(models.Model):

    qux = models.IntegerField()
    quux = models.IntegerField()
    quuux = models.TextField()



ModelA.objects.filter(model_b__quuux='test').select_related('model_b')

...

ModelB.objects.prefetch_related('model_a_set')

...

```


