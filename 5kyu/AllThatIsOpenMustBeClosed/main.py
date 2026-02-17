import re

source = "(Sensei [says) no!]"
caps = "()[]"
rules = {caps[i]: caps[i+1] for i in range(0, len(caps), 2)}
stack = []

for char in source:
    if char in rules:
        stack.append(char)

    elif char in rules.values():
        if not stack:
            print("Error de fechamento")
            break

        topo = stack.pop()
        if rules[topo] != char:
            print("Error de fechamento")
            break
    else:
        if not stack:
            print("Tudo balanceado")
        else:
            print("Error de fechamento")

# se eu to percorrendo uma string e um parêntese abre e
# abre um colchetes, precisa ser fechado o colchetes e
# os parenteses, nessa ordem.
