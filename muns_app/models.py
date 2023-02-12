from django.db import models


class words_memory_subtest(models.Model):
    stone1 = models.BooleanField(default=False)
    ear1 = models.BooleanField(default=False)
    neck1 = models.BooleanField(default=False)
    cloud1 = models.BooleanField(default=False)
    foot1 = models.BooleanField(default=False)
    seed1 = models.BooleanField(default=False)
    tongue1 = models.BooleanField(default=False)
    sand1 = models.BooleanField(default=False)
    fire1 = models.BooleanField(default=False)
    nose1 = models.BooleanField(default=False)
    tree1 = models.BooleanField(default=False)
    hand1 = models.BooleanField(default=False)
    wind1 = models.BooleanField(default=False)
    knee1 = models.BooleanField(default=False)
    WL_trial1 = models.IntegerField()

    def save(self, *args, **kwargs):
        self.WL_trial1 = (1 if self.stone1 == True else 0) + (3 if self.ear1 == True else 0) + (1 if self.neck1 == True else 0) + (3 if self.cloud1 == True else 0) + (1 if self.foot1 == True else 0) + (3 if self.seed1 == True else 0) + (1 if self.tongue1 == True else 0) + (3 if self.sand1 == True else 0) + (1 if self.fire1 == True else 0) + (3 if self.nose1 == True else 0) + (1 if self.tree1 == True else 0) + (3 if self.hand1 == True else 0) + (1 if self.wind1 == True else 0) + (3 if self.knee1 == True else 0)
        super(words_memory_subtest, self).save(*args, **kwargs)

    def __str__(self):
        return f"Word List Subtest Trial 1 - Score: {self.WL_trial1}"

   
""" stone2 = models.PositiveSmallIntegerField()
    ear2 = models.PositiveSmallIntegerField()
    neck2 = models.PositiveSmallIntegerField()
    cloud2 = models.PositiveSmallIntegerField()
    foot2 = models.PositiveSmallIntegerField()
    seed2 = models.PositiveSmallIntegerField()
    tongue2 = models.PositiveSmallIntegerField()
    sand2 = models.PositiveSmallIntegerField()
    fire2 = models.PositiveSmallIntegerField()
    nose2 = models.PositiveSmallIntegerField()
    tree2 = models.PositiveSmallIntegerField()
    hand2 = models.PositiveSmallIntegerField()
    wind2 = models.PositiveSmallIntegerField()
    knee2 = models.PositiveSmallIntegerField()
    WL_trial2 = models.PositiveSmallIntegerField()
    stone3 = models.PositiveSmallIntegerField()
    ear3 = models.PositiveSmallIntegerField()
    neck3 = models.PositiveSmallIntegerField()
    cloud3 = models.PositiveSmallIntegerField()
    foot3 = models.PositiveSmallIntegerField()
    seed3 = models.PositiveSmallIntegerField()
    tongue3 = models.PositiveSmallIntegerField()
    sand3 = models.PositiveSmallIntegerField()
    fire3 = models.PositiveSmallIntegerField()
    nose3 = models.PositiveSmallIntegerField()
    tree3 = models.PositiveSmallIntegerField()
    hand3 = models.PositiveSmallIntegerField()
    wind3 = models.PositiveSmallIntegerField()
    knee3 = models.PositiveSmallIntegerField()
    WL_trial3 = models.PositiveSmallIntegerField()
    WL_all_inmediate_trials = models.PositiveSmallIntegerField()
    
""" 