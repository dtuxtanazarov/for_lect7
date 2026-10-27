import itertools
import string
from unrar import rarfile

# Bu klondan amalga oshirilgan o`zgarish
def brute_force_rar(rar_path, max_length=4):
    characters = string.ascii_lowercase

    try:
        # RAR faylni ochish
        rf = rarfile.RarFile(rar_path)

        for length in range(1, max_length + 1):
            for guess in itertools.product(characters, repeat=length):
                password = "".join(guess)

                try:
                    # Parolni tekshirib ko'rish
                    # extractall funksiyasi orqali parolni sinab ko'ramiz
                    rf.extractall(pwd=password)

                    print(f"[+] Parol topildi: {password}")
                    return password

                except Exception:
                    # Parol xato bo'lsa, xatolikni yutib yuboramiz
                    print(f"[-] Noto'g'ri: {password}")

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

    print("Parol topilmadi.")
    return None


# Foydalanish
brute_force_rar("file.rar")