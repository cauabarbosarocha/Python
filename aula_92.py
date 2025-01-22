# Introdução às Generator functions em Python
# generator = (n for n in range(100))

def generator(n=0, maximum=20):
    while True:
        yield n # Pausa
        n += 1
        
        if n > maximum:
            return
        
gen = generator(maximum=100000)
for n in gen:
    print(n)