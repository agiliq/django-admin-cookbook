Models used in this book
===========================


App entities
++++++++++++++

The models are::


    class Category(models.Model):
        name = models.CharField(max_length=100)

        class Meta:
            verbose_name_plural = "Categories"

        def __str__(self):
            return self.name


    class Origin(models.Model):
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name


    class Entity(models.Model):
        GENDER_MALE = "Male"
        GENDER_FEMALE = "Female"
        GENDER_OTHERS = "Others/Unknown"

        name = models.CharField(max_length=100)
        alternative_name = models.CharField(
            max_length=100, null=True, blank=True
        )


        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
        gender = models.CharField(
            max_length=100,
            choices=(
                (GENDER_MALE, GENDER_MALE),
                (GENDER_FEMALE, GENDER_FEMALE),
                (GENDER_OTHERS, GENDER_OTHERS),
            )
        )
        description = models.TextField()

        def __str__(self):
            return self.name

        class Meta:
            abstract = True


    class Hero(Entity):

        class Meta:
            verbose_name_plural = "Heroes"

        is_immortal = models.BooleanField(default=True)

        benevolence_factor = models.PositiveSmallIntegerField(
            help_text="How benevolent this hero is?"
        )
        arbitrariness_factor = models.PositiveSmallIntegerField(
            help_text="How arbitrary this hero is?"
        )
        # relationships
        father = models.ForeignKey(
            "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
        )
        mother = models.ForeignKey(
            "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
        )
        spouse = models.ForeignKey(
            "self", related_name="+", null=True, blank=True, on_delete=models.SET_NULL
        )


    class Villain(Entity):
        is_immortal = models.BooleanField(default=False)

        malevolence_factor = models.PositiveSmallIntegerField(
            help_text="How malevolent this villain is?"
        )
        power_factor = models.PositiveSmallIntegerField(
            help_text="How powerful this villain is?"
        )
        is_unique = models.BooleanField(default=True)
        count = models.PositiveSmallIntegerField(default=1)


App events
+++++++++++

The models are::



    class Epic(models.Model):
        name = models.CharField(max_length=255)
        participating_heroes = models.ManyToManyField(Hero)
        participating_villains = models.ManyToManyField(Villain)


    class Event(models.Model):
        epic = models.ForeignKey(Epic, on_delete=models.CASCADE)
        details = models.TextField()
        years_ago = models.PositiveIntegerField()


    class EventHero(models.Model):
        event = models.ForeignKey(Event, on_delete=models.CASCADE)
        hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
        is_primary = models.BooleanField()


    class EventVillain(models.Model):
        event = models.ForeignKey(Event, on_delete=models.CASCADE)
        hero = models.ForeignKey(Villain, on_delete=models.CASCADE)
        is_primary = models.BooleanField()
