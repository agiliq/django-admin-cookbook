How to add nested inlines in Django admin?
==========================================


You have yor models defined like this::

    class Category(models.Model):
        ...

    class Hero(models.Model):
        category = models.ForeignKey(Catgeory)
        ...

    class HeroAcquaintance(models.Model):
        hero = models.OneToOneField(Hero, on_delete=models.CASCADE)
        ...

You want to have one admin page to create :code:`Category`, :code:`Hero` and :code:`HeroAcquaintance` objects. However, Django doesn't support nested inline with Foreign Keys or One To One relations which span more than one levels. You have a few options,


You can change the :code:`HeroAcquaintance` model, so that it has a direct FK to :code:`Category`, something like this::

    class HeroAcquaintance(models.Model):
        hero = models.OneToOneField(Hero, on_delete=models.CASCADE)
        category = models.ForeignKey(Category)

        def save(self, *args, **kwargs):
            self.category = self.hero.category
            super().save(*args, **kwargs)


Then you can attach :code:`HeroAcquaintanceInline` to :code:`CategoryAdmin`, and get a kind of nested inline.

Alternatively, there are a few third party Django apps which allow nested inline. A quick Github or DjangoPackages search will find one which suits your needs and tastes.

