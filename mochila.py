import random
import time
import matplotlib.pyplot as plt

# FUERZA BRUTA
def mochila_fuerza_bruta(pesos, beneficios, capacidad):
    n = len(pesos)
    mejor_beneficio = 0
    mejor_seleccion = None

    for mascara in range(1 << n):
        peso_total = 0
        beneficio_total = 0

        for i in range(n):
            if (mascara >> i) & 1:
                peso_total += pesos[i]
                beneficio_total += beneficios[i]

                # pequeño corte si ya se pasa
                if peso_total > capacidad:
                    break

        if peso_total <= capacidad and beneficio_total > mejor_beneficio:
            mejor_beneficio = beneficio_total
            mejor_seleccion = mascara

    objetos_elegidos = []
    if mejor_seleccion is not None:
        for i in range(n):
            if (mejor_seleccion >> i) & 1:
                objetos_elegidos.append(i)

    return mejor_beneficio, objetos_elegidos

# PROGRAMACIÓN DINÁMICA
def mochila_programacion_dinamica(pesos, beneficios, capacidad):
    n = len(pesos)
    tabla = [[0] * (capacidad + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        peso_i = pesos[i - 1]
        beneficio_i = beneficios[i - 1]

        for w in range(capacidad + 1):
            tabla[i][w] = tabla[i - 1][w]  # no tomar

            if peso_i <= w:
                tabla[i][w] = max(
                    tabla[i][w],
                    beneficio_i + tabla[i - 1][w - peso_i]
                )

    # reconstruir solución
    objetos_elegidos = []
    w = capacidad
    for i in range(n, 0, -1):
        if tabla[i][w] != tabla[i - 1][w]:
            objetos_elegidos.append(i - 1)
            w -= pesos[i - 1]

    objetos_elegidos.reverse()
    return tabla[n][capacidad], objetos_elegidos


# GENERAR INSTANCIA DE PRUEBA
def generar_instancia(n, capacidad, inicial=None):
    if inicial is not None:
        random.seed(inicial)

    pesos = [random.randint(1, 20) for _ in range(n)]
    beneficios = [random.randint(1, 30) for _ in range(n)]
    return pesos, beneficios, capacidad


# MEDIR TIEMPO DE EJECUCIÓN
def medir_tiempo(funcion, pesos, beneficios, capacidad, repeticiones=3):
    mejor_tiempo = float("inf")
    resultado = None

    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = funcion(pesos, beneficios, capacidad)
        fin = time.perf_counter()
        mejor_tiempo = min(mejor_tiempo, fin - inicio)

    return mejor_tiempo, resultado

def main():
    tamanios = [10, 12, 14, 16, 18, 20, 22]
    capacidad = 60

    tiempos_bruta = []
    tiempos_dp = []

    for n in tamanios:
        pesos, beneficios, cap = generar_instancia(n, capacidad, inicial=100 + n)

        tiempo_bruta, res_bruta = medir_tiempo(
            mochila_fuerza_bruta, pesos, beneficios, cap
        )
        tiempo_dp, res_dp = medir_tiempo(
            mochila_programacion_dinamica, pesos, beneficios, cap
        )

        tiempos_bruta.append(tiempo_bruta)
        tiempos_dp.append(tiempo_dp)

        # verificación
        if res_bruta[0] != res_dp[0]:
            print("ERROR: resultados distintos en n =", n)

        print(
            f"n={n} | Fuerza bruta={tiempo_bruta:.6f}s | "
            f"DP={tiempo_dp:.6f}s | Óptimo={res_dp[0]}"
        )

    # GRÁFICA
    plt.figure()
    plt.plot(tamanios, tiempos_bruta, marker="o", label="Fuerza bruta")
    plt.plot(tamanios, tiempos_dp, marker="o", label="Programación dinámica")
    plt.xlabel("Número de objetos (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos - Problema de la Mochila 0/1")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("comparacion_mochila.png")
    print("Gráfica guardada como comparacion_mochila.png")


if __name__ == "__main__":
    main()
