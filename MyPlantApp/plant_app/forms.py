from django import forms

from MyPlantApp.plant_app.models import PlantApp


class PlantAppForm(forms.ModelForm):
    class Meta:
        model = PlantApp
        fields = '__all__'


class DeletePlant(PlantAppForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
