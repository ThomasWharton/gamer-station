from django.forms.widgets import ClearableFileInput, RadioSelect
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'


class StarRadioSelect(RadioSelect):

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
        option['label'] = mark_safe(f'<i class="fas fa-star"></i>')
        return option
