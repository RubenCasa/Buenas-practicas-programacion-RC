def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(rango):
    primos = []
    for numero in range(rango + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

if __name__ == "__main__":
    import time
    inicio = time.time()
    primos = encontrar_primos(100000)
    fin = time.time()
    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
    # Descomentar si quieres ver los primeros primos
    # print(primos[:10])