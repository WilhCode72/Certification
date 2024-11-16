from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Prénom",
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Classe CSS pour les champs
            'placeholder': 'Entrez votre prénom'  # Texte d'exemple
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nom",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Entrez votre nom'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'exemple@mail.com'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        }),
        label="Mot de passe"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmez votre mot de passe'
        }),
        label="Confirmer le mot de passe"
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

        help_texts = {
            'username': '',
            'email': '',
            'password': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Supprimer les messages 'required' pour éviter d'afficher "requis"
        for field in self.fields.values():
            field.required = True  # Laisser le champ requis mais sans message par défaut
            field.error_messages = {'required': ''}  # Supprime le message 'required'
            field.help_text = ''  # Enlève les aides contextuelles, si présentes

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur ou Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nom d\'utilisateur ou Email'
        })
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '••••••••'
        })
    )
