from django import forms


class FormCadastrar(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Nome",
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "E-mail",
            }
        ),
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Senha",
            }
        )
    )
    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "CPF",
                "maxlength": "11",
            }
        ),
    )
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "type": "date",
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Data Nascimento",
            }
        )
    )
    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Telefone",
            }
        )
    )
