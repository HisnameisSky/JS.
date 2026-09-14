import random


def generate_password(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))


password = generate_password(12)

print(f"Generated password: {password}")