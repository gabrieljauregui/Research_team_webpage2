from django.db import models


class WordsLearningSubtest(models.Model):
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
    WL_trial1_score = models.IntegerField(default=0)

    stone2 = models.BooleanField(default=False)
    ear2 = models.BooleanField(default=False)
    neck2 = models.BooleanField(default=False)
    cloud2 = models.BooleanField(default=False)
    foot2 = models.BooleanField(default=False)
    seed2 = models.BooleanField(default=False)
    tongue2 = models.BooleanField(default=False)
    sand2 = models.BooleanField(default=False)
    fire2 = models.BooleanField(default=False)
    nose2 = models.BooleanField(default=False)
    tree2 = models.BooleanField(default=False)
    hand2 = models.BooleanField(default=False)
    wind2 = models.BooleanField(default=False)
    knee2 = models.BooleanField(default=False)
    WL_trial2_score = models.IntegerField(default=0)

    stone3 = models.BooleanField(default=False)
    ear3 = models.BooleanField(default=False)
    neck3 = models.BooleanField(default=False)
    cloud3 = models.BooleanField(default=False)
    foot3 = models.BooleanField(default=False)
    seed3 = models.BooleanField(default=False)
    tongue3 = models.BooleanField(default=False)
    sand3 = models.BooleanField(default=False)
    fire3 = models.BooleanField(default=False)
    nose3 = models.BooleanField(default=False)
    tree3 = models.BooleanField(default=False)
    hand3 = models.BooleanField(default=False)
    wind3 = models.BooleanField(default=False)
    knee3 = models.BooleanField(default=False)
    WL_trial3_score = models.IntegerField(default=0)

    total_score = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.WL_trial1_score = (
            (1 if self.stone1 == True else 0)
            + (3 if self.ear1 == True else 0)
            + (1 if self.neck1 == True else 0)
            + (3 if self.cloud1 == True else 0)
            + (1 if self.foot1 == True else 0)
            + (3 if self.seed1 == True else 0)
            + (1 if self.tongue1 == True else 0)
            + (3 if self.sand1 == True else 0)
            + (1 if self.fire1 == True else 0)
            + (3 if self.nose1 == True else 0)
            + (1 if self.tree1 == True else 0)
            + (3 if self.hand1 == True else 0)
            + (1 if self.wind1 == True else 0)
            + (3 if self.knee1 == True else 0)
        )
        self.WL_trial2_score = (
            (1 if self.stone2 == True else 0)
            + (3 if self.ear2 == True else 0)
            + (1 if self.neck2 == True else 0)
            + (3 if self.cloud2 == True else 0)
            + (1 if self.foot2 == True else 0)
            + (3 if self.seed2 == True else 0)
            + (1 if self.tongue2 == True else 0)
            + (3 if self.sand2 == True else 0)
            + (1 if self.fire2 == True else 0)
            + (3 if self.nose2 == True else 0)
            + (1 if self.tree2 == True else 0)
            + (3 if self.hand2 == True else 0)
            + (1 if self.wind2 == True else 0)
            + (3 if self.knee2 == True else 0)
        )
        self.WL_trial3_score = (
            (1 if self.stone3 == True else 0)
            + (3 if self.ear3 == True else 0)
            + (1 if self.neck3 == True else 0)
            + (3 if self.cloud3 == True else 0)
            + (1 if self.foot3 == True else 0)
            + (3 if self.seed3 == True else 0)
            + (1 if self.tongue3 == True else 0)
            + (3 if self.sand3 == True else 0)
            + (1 if self.fire3 == True else 0)
            + (3 if self.nose3 == True else 0)
            + (1 if self.tree3 == True else 0)
            + (3 if self.hand3 == True else 0)
            + (1 if self.wind3 == True else 0)
            + (3 if self.knee3 == True else 0)
        )
        super(WordsLearningSubtest, self).save(*args, **kwargs)
        self.total_score = (
            self.WL_trial1_score + self.WL_trial2_score + self.WL_trial3_score
        )

    def __str__(self):
        return f"Word Learning Subtest - Total Score: {self.total_score}"


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
