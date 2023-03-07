from django import forms
from django import forms


class FeatureForm(forms.Form):
    Customerid = forms.CharField(label='Customer ID', max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Gender = forms.ChoiceField(label='Gender', choices=[(
        'male', 'male'), ('female', 'female')], widget=forms.Select(attrs={'class': 'form-select'}))
    # Seniorcitizen = forms.ChoiceField(label='Senior Citizen', choices=[(
    #     0, 'No'), (1, 'Yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    # Seniorcitizen = forms.IntegerField(label='Senior Citizen')
    Seniorcitizen = forms.ChoiceField(label='Senior Citizen', choices=[(
        'yes', 'yes'), ('no', 'no')], widget=forms.Select(attrs={'class': 'form-select'}))
    Partner = forms.ChoiceField(label='Partner', choices=[(
        'yes', 'yes'), ('no', 'no')], widget=forms.Select(attrs={'class': 'form-select'}))
    Dependents = forms.ChoiceField(label='Dependents', choices=[(
        'yes', 'yes'), ('no', 'no')], widget=forms.Select(attrs={'class': 'form-select'}))
    Tenure = forms.IntegerField(label='Tenure (months)', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    Phoneservice = forms.ChoiceField(label='Phone Service', choices=[(
        'yes', 'yes'), ('no', 'no')], widget=forms.Select(attrs={'class': 'form-select'}))
    Multiplelines = forms.ChoiceField(label='Multiple Lines', choices=[(
        'no_phone_service', 'no_phone_service'), ('no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Internetservice = forms.ChoiceField(label='Internet Service', choices=[(
        'dsl', 'dsl'), ('fiber_optic', 'fiber_optic'), ('no', 'no')], widget=forms.Select(attrs={'class': 'form-select'}))
    Onlinesecurity = forms.ChoiceField(label='Online Security', choices=[(
        'no_internet_service', 'no_internet_service'), ('no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Onlinebackup = forms.ChoiceField(label='Online Backup', choices=[('no_internet_service', 'no_internet_service'), (
        'no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Deviceprotection = forms.ChoiceField(label='Device Protection', choices=[(
        'no_internet_service', 'no_internet_service'), ('no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Techsupport = forms.ChoiceField(label='Tech Support', choices=[('no_internet_service', 'no_internet_service'), (
        'no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Streamingtv = forms.ChoiceField(label='Streaming TV', choices=[('no_internet_service', 'no_internet_service'), (
        'no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Streamingmovies = forms.ChoiceField(label='Streaming Movies', choices=[(
        'no_internet_service', 'no_internet_service'), ('no', 'no'), ('yes', 'yes')], widget=forms.Select(attrs={'class': 'form-select'}))
    Contract = forms.ChoiceField(label='Contract', choices=[('month-to-month', 'month-to-month'), (
        'one_year', 'one_year'), ('two_year', 'two_year')], widget=forms.Select(attrs={'class': 'form-select'}))
    Paperlessbilling = forms.ChoiceField(label='Paperless Billing', choices=[(
        'yes', 'yes'), ('no', 'no')], widget=forms.Select(attrs={'class': 'form-select'}))
    Paymentmethod = forms.ChoiceField(label='Payment Method', choices=[(
        'electronic_check', 'electronic_check'), ('mailed_check', 'mailed_check'), ('bank_transfer_(automatic)', 'bank_transfer_(automatic)'), ('credit_card', 'credit_card')], widget=forms.Select(attrs={'class': 'form-select'}))
    Monthlycharges = forms.FloatField(label='Monthlycharges', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    Totalcharges = forms.FloatField(label='Totalcharges', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))


# class FeatureForm(forms.Form):
#     Customerid = forms.CharField(max_length=255)
#     Gender = forms.CharField(max_length=50)
#     Seniorcitizen = forms.IntegerField()
#     Partner = forms.CharField(max_length=50)
#     Dependents = forms.CharField(max_length=50)
#     Tenure = forms.IntegerField()
#     Phoneservice = forms.CharField(max_length=50)
#     Multiplelines = forms.CharField(max_length=50)
#     Internetservice = forms.CharField(max_length=50)
#     Onlinesecurity = forms.CharField(max_length=50)
#     Onlinebackup = forms.CharField(max_length=50)
#     Deviceprotection = forms.CharField(max_length=50)
#     Techsupport = forms.CharField(max_length=50)
#     Streamingtv = forms.CharField(max_length=50)
#     Streamingmovies = forms.CharField(max_length=50)
#     Contract = forms.CharField(max_length=50)
#     Paperlessbilling = forms.CharField(max_length=50)
#     Paymentmethod = forms.CharField(max_length=50)
#     Monthlycharges = forms.FloatField()
#     Totalcharges = forms.FloatField()
