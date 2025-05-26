import numpy as np
import time

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos(rango):
    return np.array([x for x in range(rango + 1) if es_primo(x)])

if __name__ == "__main__":
    inicio = time.time()
    primos = encontrar_primos(100000)
    fin = time.time()
    print(f"Tiempo de ejecución (optimizado): {fin - inicio:.4f} segundos")
    # Descomentar si quieres ver los primeros primos
    # print(primos[:10])