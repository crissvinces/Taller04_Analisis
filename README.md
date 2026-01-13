# Taller04_Analisis
Identificar y describir cómo se aplicaría cada una de las siguientes estrategias al problema de la
mochila 0/1, Incluir pseudocódigo en lenguaje natural usando sus propias palabras y un diagrama de flujo básico.
Luego, justificar por qué cada estrategia es o no es adecuada para el problema.

• Fuerza bruta

Verificar todas las combinaciones una por una y conseguir la que cumpla el máximo cargable de la maleta y además tenga mejor beneficio en costo unitario; la complejidad es de 2^n.

• Dividir y conquistar

• Programación dinámica

Se mide el mejor caso posible para un peso determinado y luego se chequea si añadir un objeto mejorará la situación o será mejor no añadirlo; y a partir de ahí se continua

Código Programacion dinamica
n=len (objetos)
for i to n:
    P[1,0]=0
for we to W_max: 
    P[0, w]=0
for i = 1 to n:
  for w= 1 to W_max:
    if peso[i] <= w: # Elemento i cabe en la capacidad w actual 
        if b[i] + P[i-1, w peso[i]]> P[i-1, w]:
            else:
                P[i, w] = b[i] + P[i-1, w peso[i]]
                P[i, w] P[i-1, w]
            else: # No puedo agregar objeto por su peso
                P[i, w] = p[i-1, w]
    
        
• Algoritmo voraz
