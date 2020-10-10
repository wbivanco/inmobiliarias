from django.contrib.auth import get_user_model


def crear_usuario(username):
    usuario, _ = get_user_model().objects.get_or_create(
        username=username,
        defaults={
            'first_name': 'Usuario',
            'last_name': 'Prueba',
            'email': 'usuario@test.com'
        }
    )

    return usuario
