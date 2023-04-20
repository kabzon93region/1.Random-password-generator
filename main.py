import random as rnd


def rnd_smbl(x, y):
    return chr(rnd.randint(ord(x), ord(y)))


def rnd_password(length_password):
    ppl: int = 0
    ppn: int = 0
    pps: int = 0
    password: str = ""
    while pps < 1 or ppl < 1 or ppn < 1:
        ppl = 0
        ppn = 0
        pps = 0
        password = ""
        for i in range(length_password):
            symtype = rnd.randint(0, 2)

            if symtype == 0:
                lat = rnd.randint(0, 1)
                if lat == 1:
                    rl = rnd_smbl('A', 'Z')
                    ppl += 1
                else:
                    rl = rnd_smbl('a', 'z')
                password = password + rl

            elif symtype == 1:
                rn = rnd_smbl('0', '9')
                ppn += 1
                password = password + rn

            elif symtype == 2:
                rs = rnd_smbl('!', '.')
                pps += 1
                password = password + rs
    return password


lenpas: int = 0
qpas: int = 0

while True:
    try:
        lenpas = int(input("Введите длину пароля для генерации (не менее 3): "))
        qpas = int(input("Введите количество генерируемых паролей (не менее 1): "))
        break
    except ValueError:
        print("!ОШИБКА! : введено не число!", "Программа завершена с ошибкой.", "Повторный запуск...", " ", sep="\n")

if lenpas < 3: lenpas = 3
if qpas < 1: qpas = 1

file_password = open("pass.txt", "w")
for i in range(qpas):
    file_password.write(rnd_password(lenpas) + "\n") if i < qpas - 1 else file_password.write(rnd_password(lenpas))
file_password.close()

print("Программа завершена успешно.")
