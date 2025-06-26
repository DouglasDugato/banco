# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:

if (" " in email or 
    not "@" in email or 
    email.startswith("@") or 
    email.endswith("@")):
    print("Email Invalido")
else:
    print('Email valido!')