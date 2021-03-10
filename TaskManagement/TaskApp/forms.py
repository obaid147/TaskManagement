from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Enter Your Task"}))

    class Meta:
        model = Task
        fields = "__all__"
