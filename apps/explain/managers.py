from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.db.models.query import QuerySet
from django.db.models import Manager

class EntryManager(models.Manager):
    def get_until_create(self):
        created = False
        while not created:
            hex = ''.join(random.choice('0123456789abcdef') for i in range(6))
            entry, created = Entry.objects.get_or_create(hex=hex)
            if created:
                return entry

class VoteQuerySet(QuerySet):
    def for_model(self, model):
        ct = ContentType.objects.get_for_model(model)
        return self.filter(content_type=ct, object_pk=force_unicode(model._get_pk_val()))

    def get_up_votes(self):
        return self.filter(value=True)

    def get_down_votes(self):
        return self.filter(value=False)

class VoteManager(Manager):
    def get_query_set(self):
        return VoteQuerySet(self.model, using=self._db)

    def for_model(self, model):
        return self.get_query_set().for_model(model)

    def get_up_votes(self):
        return self.get_query_set().get_up_votes()

    def get_down_votes(self):
        return self.get_query_set().get_down_votes()
