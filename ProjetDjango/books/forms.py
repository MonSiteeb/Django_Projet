from cProfile import label
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,ReadOnlyPasswordHashField

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """
    The default 

    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]   
    
class DocumentForm(forms.Form):
    matiere = forms.CharField(
        max_length=30,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type' : 'text'
            }
        )
    )
    classe = forms.CharField(
        max_length=30,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type' : 'text'
            }
        )
    )
    
    professeur = forms.CharField(
        max_length=40,
        required=True,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type' : 'text'
            }
        )
    )
    
    type = forms.ChoiceField(
        required=True,
        choices=[('epreuve', 'Epreuve'), ('correction', 'Correction')],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )
    
    fichier = forms.FileField(
        required=True,
        # widget=forms.Select(
        #     attrs={
        #         'type':'upload'
        #     }
        # )
    )

class Subscribe(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type':'email'
            }
        )
    )

class UserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        required=True
    )
    password1 = forms.CharField(
        label= 'Mot de passe',
        help_text= "<ul><li>Votre mot de passe ne doit pas être similaire à vos infos personnelles</li><li>Votre mot de passe doit contenir 8 caractères au minimum.</li><li>Votre mot de passe ne doit pas être commun.</li><li>Votre mot de passe ne peut pas être entièrement numérique.</li>",
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'type' : 'password'
            }
        )
    )
    password2 = forms.CharField(
        label= 'Confirmer le mot de passe',
        help_text= "Entrez le même mot de passe",
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'type' : 'password'
            }
        )
    )
    is_from_esmt = forms.BooleanField(
        label= "Êtes-vous de l'ESMT ?",
        required=False
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'password1','password2', 'is_from_esmt')