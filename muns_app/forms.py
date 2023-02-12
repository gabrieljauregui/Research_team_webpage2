from django import forms
from .models import words_memory_subtest

class words_memory_subtest(forms.ModelForm):
    class Meta:
        model = words_memory_subtest
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
