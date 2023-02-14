from django import forms
from .models import WordsLearningSubtest

class WordsLearningSubtestForm(forms.ModelForm):
    stone1 = forms.BooleanField(required=False)
    ear1 = forms.BooleanField(required=False)
    neck1 = forms.BooleanField(required=False)
    cloud1 = forms.BooleanField(required=False)
    foot1 = forms.BooleanField(required=False)
    seed1 = forms.BooleanField(required=False)
    tongue1 = forms.BooleanField(required=False)
    sand1 = forms.BooleanField(required=False)
    fire1 = forms.BooleanField(required=False)
    nose1 = forms.BooleanField(required=False)
    tree1 = forms.BooleanField(required=False)
    hand1 = forms.BooleanField(required=False)
    wind1 = forms.BooleanField(required=False)
    knee1 = forms.BooleanField(required=False)

    class Meta:
        model = WordsLearningSubtest
        fields = [
            'stone1',
            'ear1',
            'neck1',
            'cloud1',
            'foot1',
            'seed1',
            'tongue1',
            'sand1',
            'fire1',
            'nose1',
            'tree1',
            'hand1',
            'wind1',
            'knee1',
        ]

class WordsLearningSubtestTrial2Form(forms.ModelForm):
    class Meta:
        model = WordsLearningSubtest
        fields = [
            'stone2',
            'ear2',
            'neck2',
            'cloud2',
            'foot2',
            'seed2',
            'tongue2',
            'sand2',
            'fire2',
            'nose2',
            'tree2',
            'hand2',
            'wind2',
            'knee2',
        ]
        
class WordsLearningSubtestTrial3Form(forms.ModelForm):
    class Meta:
        model = WordsLearningSubtest
        fields = [
            'stone3',
            'ear3',
            'neck3',
            'cloud3',
            'foot3',
            'seed3',
            'tongue3',
            'sand3',
            'fire3',
            'nose3',
            'tree3',
            'hand3',
            'wind3',
            'knee3',
        ]
