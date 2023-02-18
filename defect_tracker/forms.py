from django import forms
from .models import Defect


class DefectForm(forms.ModelForm):
    # define the reason_choice field as a ChoiceField
    reason_choice = forms.ChoiceField(
        choices=[], required=False, label='Choose existing defect cause')

    class Meta:
        model = Defect
        exclude = ['created_at']
        fields = ['reason_choice', 'reason', 'job_order_no', 'defect_image']
        labels = {'reason': 'Or insert a new defect cause'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # populate the reason_choice field with a list of distinct reasons from the database
        self.fields['reason_choice'].choices = [
            ('', '')] + [(reason, reason) for reason in Defect.objects.order_by().values_list('reason', flat=True).distinct()]

    def clean(self):
        cleaned_data = super().clean()
        reason = cleaned_data.get('reason')
        reason_choice = cleaned_data.get('reason_choice')
        if not reason and not reason_choice:
            raise forms.ValidationError(
                'Please enter a reason or choose one from the list.')
        elif reason and reason_choice:
            raise forms.ValidationError(
                'Please enter a reason OR choose one from the list, not both.')
        elif not reason:
            cleaned_data['reason'] = reason_choice
        return cleaned_data
