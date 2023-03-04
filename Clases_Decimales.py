import pandas as pd
import math
from colorama import init, Fore, Back, Style

# Inicializar colorama
init()

# Imprimir texto en diferentes colores y estilos
print(Fore.LIGHTGREEN_EX)  # + "Texto en azul"
print(Back.BLACK)  # + "Fondo negro"
print(Style.BRIGHT)  # + "Texto brillante"
# print(Fore.YELLOW + Back.BLUE + "Texto amarillo sobre fondo azul")
# print(Style.RESET_ALL + "Restaurar estilo por defecto")


# from collections import Counter (Para ocurrencia)

# Lista de elementos con punto decimal
elementos = [24.2, 29.9, 23.4, 23.0, 25.5, 22.0, 33.9, 20.4, 26.6, 24.0, 28.9, 22.5, 18.7, 32.6, 26.1, 26.2, 26.7, 20.4,
             22.2, 24.7, 18.6, 18.5, 19.6, 24.4, 24.8, 27.8, 27.6, 27.2, 20.8, 22.1, 19.7, 25.3, 28.2, 34.2, 32.5, 30.8,
             26.8, 20.6, 21.2, 20.7, 25.2, 25.7, 32.2, 28.8, 24.7, 18.7, 20.5, 25.5, 19.1, 25.5, 22.1, 27.5, 25.8, 25.2,
             25.6, 25.2, 25.2, 27.9, 18.9, 37.3, 29.9, 23.2, 19.8, 20.8, 29.5, 27.6, 21.2, 38.7, 21.3, 24.8, 32.3, 20.1,
             26.8, 25.4, 26.3, 21.2, 19.5, 22.8, 21.7, 25.3, 32.3, 28.1, 27.5, 25.3, 19.3, 27.4, 26.4, 20.9, 34.5, 25.9,
             31.4, 27.4, 27.3, 20.6, 31.8, 25.8, 25.2, 21.9, 26.8, 26.5]

# ////////////////////////////////////////////////////////////////

# Calcular Tallo y Hoja

# Ordenamos los datos de la lista
elementos.sort()

# Encontramos el número más grande en la lista
max_num = max(elementos)

# Encontramos la longitud del número más grande
max_len = len(str(max_num))

# Inicializamos un diccionario para almacenar los tallos y hojas
stem_leaf = {}

# Recorremos cada número en la lista
for num in elementos:
    # Convertimos el número en una cadena de texto
    num_str = str(num)

    # Obtenemos el tallo del número
    stem = float(num_str[:-1])

    # Obtenemos la hoja del número
    leaf = int(num_str[-1])

    # Agregamos el tallo y la hoja al diccionario
    if stem in stem_leaf:
        stem_leaf[stem].append(leaf)
    else:
        stem_leaf[stem] = [leaf]

# Imprimimos los tallos y hojas en orden
print("TALLO Y HOJA")
for stem in sorted(stem_leaf.keys()):
    leaves = ' '.join(map(str, sorted(stem_leaf[stem])))
    print(f'{stem:>{max_len}} | {leaves}')

print(" ")
# ////////////////////////////////////////////////////////////////

# Calcular el rango de los datos
rango = max(elementos) - min(elementos)

# ////////////////////////////////////////////////////////////////

# Calcular el número de clases usando la regla de Sturges
n = len(elementos)
num_clases = (int(1 + 3.322 * math.log10(n)))
k: float = (1 + 3.322 * math.log10(n))

# ////////////////////////////////////////////////////////////////

# Calcular la amplitud de cada clase
amplitud_clase = int((rango / k) + 1)

# ////////////////////////////////////////////////////////////////

# Calcular los límites de cada clase
limites_clase = [min(elementos) + i * amplitud_clase for i in range(num_clases + 1)]

# ////////////////////////////////////////////////////////////////

# Crear una tabla para almacenar las frecuencias de cada clase
tabla_frecuencias = pd.DataFrame(index=range(num_clases), columns=["L-i", "L-s", "F"])

# ////////////////////////////////////////////////////////////////

# Imprimir intervalo de clase
print("Numero de clases: ", num_clases)
print("Max: ", max(elementos), " Min: ", min(elementos))

print("Intervalo de clase: ", amplitud_clase, '\n')

# ////////////////////////////////////////////////////////////////

# Calcular la frecuencia de cada clase
total_frecuencias = 0
for i in range(num_clases):
    tabla_frecuencias.iloc[i]["L-i"] = round(limites_clase[i], 2)
    tabla_frecuencias.iloc[i]["L-s"] = round(limites_clase[i + 1], 2)
    frecuencia = len([x for x in elementos if round(limites_clase[i], 1) <= x < round(limites_clase[i + 1], 1)])
    # frecuencia = [25,14,35,13,8,3,2]
    tabla_frecuencias.iloc[i]["F"] = frecuencia
    total_frecuencias += frecuencia

# Imprimiendo ocurrencias (prueba)
# ocurrencia = Counter(elementos)
# print(ocurrencia)

# ////////////////////////////////////////////////////////////////

# Calcular el punto medio de cada clase
tabla_frecuencias["P-m"] = (tabla_frecuencias["L-i"] + tabla_frecuencias["L-s"]) / 2

# ////////////////////////////////////////////////////////////////

# Calcular la frecuencia acumulada
tabla_frecuencias["F-a"] = tabla_frecuencias["F"].cumsum()

# ////////////////////////////////////////////////////////////////

# Calcular la frecuencia relativa
tabla_frecuencias["F-r"] = tabla_frecuencias["F"] / total_frecuencias

# ////////////////////////////////////////////////////////////////

# Calcular la frecuencia relativa porcentual
tabla_frecuencias["F-r%"] = (tabla_frecuencias["F"] / total_frecuencias) * 100

# ////////////////////////////////////////////////////////////////

# Calcular la frecuencia por punto medio
tabla_frecuencias["Pm*F"] = tabla_frecuencias["P-m"] * tabla_frecuencias["F"]

# ////////////////////////////////////////////////////////////////

# Calculo de la media aritmetica
total_pmf = sum(tabla_frecuencias["Pm*F"])
media = total_pmf / total_frecuencias

# ////////////////////////////////////////////////////////////////

# Calcular el punto medio - media aritmetica
tabla_frecuencias["Pm-MA"] = tabla_frecuencias["P-m"] - media

# ////////////////////////////////////////////////////////////////

# Calcular el punto medio - media aritmetica elevados a 2
tabla_frecuencias["Pm-MA2"] = pow(tabla_frecuencias["P-m"] - media, 2)

# ////////////////////////////////////////////////////////////////

# Calcular el punto medio - media aritmetica elevados a 2 por la frecuencia
tabla_frecuencias["Pm-MA2*F"] = pow(tabla_frecuencias["P-m"] - media, 2) * tabla_frecuencias["F"]

# ////////////////////////////////////////////////////////////////

# Calculo de la mediana
lim = int(total_frecuencias / 2)

# ////////////////////////////////////////////////////////////////

# Calculo de la suma de la frecuencia relativa porcentual
total_frp = sum(tabla_frecuencias["F-r%"])

# ////////////////////////////////////////////////////////////////

# Mostrar la tabla con ayuda de la librería Pandas
print(tabla_frecuencias[["L-i", "L-s", "F", "P-m", "Pm*F", "F-a", "F-r", "F-r%", "Pm-MA", "Pm-MA2", "Pm-MA2*F"]])

# ////////////////////////////////////////////////////////////////

# Encontrar la frecuencia acumulada mediana
fa_mediana = total_frecuencias / 2
fa_anterior = 0
fm = 0
li = 0
for i in range(num_clases):
    if fa_anterior < fa_mediana <= tabla_frecuencias.iloc[i]["F-a"]:
        fm = tabla_frecuencias.iloc[i]["F"]
        li = tabla_frecuencias.iloc[i]["L-i"]
        break
    else:
        fa_anterior = tabla_frecuencias.iloc[i]["F-a"]

# ////////////////////////////////////////////////////////////////

print("\nSuma total de las frecuencias: ", total_frecuencias)
print("\nSuma total del Pm*F: ", total_pmf)
print("\nSuma total del %F: ", total_frp)
print("\nMedia aritmética: ", media)
print("\nValor de N/2: ", lim)
print("fa_anterior: ", fa_anterior)

# Calcular la mediana
mediana = li + ((fa_mediana - fa_anterior) / fm) * amplitud_clase

# ////////////////////////////////////////////////////////////////

# Sumatoria de Pm-MA2*F
suma_MA2 = sum(tabla_frecuencias["Pm-MA2*F"])

# ////////////////////////////////////////////////////////////////

# Calculo de la moda (Método 1-Inspección)

# Obtiene el índice de la fila con la frecuencia mayor
tabla_frecuencias["F"] = tabla_frecuencias["F"].astype(int)
# Obtener la frecuencia mayor
frec_mayor = tabla_frecuencias["F"].max()

# Filtrar la tabla para obtener la fila con la frecuencia mayor
fila_frec_mayor = tabla_frecuencias.loc[tabla_frecuencias["F"] == frec_mayor]

# Obtener los límites de clase de la frecuencia mayor
limite_inferior = fila_frec_mayor["L-i"].values[0]
limite_superior = fila_frec_mayor["L-s"].values[0]

# Calcula la moda como el promedio de los límites de clase de la frecuencia mayor
moda1 = (limite_inferior + limite_superior) / 2

# ////////////////////////////////////////////////////////////////

# Calculo de la moda (Método 2-Pearson)
moda2 = (3 * mediana - 2 * media)

# ////////////////////////////////////////////////////////////////

# Calculo de la moda (Método 3-Diferencia)

# Obtiene el índice de la fila con la frecuencia mayor
tabla_frecuencias["F"] = tabla_frecuencias["F"].astype(int)
# Obtener la frecuencia mayor
frec_mayor = tabla_frecuencias["F"].max()

# Filtrar la tabla para obtener la fila con la frecuencia mayor
fila_frec_mayor = tabla_frecuencias.loc[tabla_frecuencias["F"] == frec_mayor]

# Obtener los límites de clase de la frecuencia mayor
limite_inferior = fila_frec_mayor["L-i"].values[0]
limite_superior = fila_frec_mayor["L-s"].values[0]

# Obtener la frecuencia anterior a la mayor
frec_anterior = tabla_frecuencias.iloc[fila_frec_mayor.index[0] - 1]["F"] if fila_frec_mayor.index[0] > 0 else 0

# Obtener la frecuencia posterior a la mayor
frec_posterior = tabla_frecuencias.iloc[fila_frec_mayor.index[0] + 1]["F"] if fila_frec_mayor.index[0] < \
                                                                              len(tabla_frecuencias) - 1 else 0

# Diferencias
dif_frec_mayor_posterior = frec_mayor - frec_posterior
dif_frec_mayor_anterior = frec_mayor - frec_anterior

moda3 = limite_inferior + amplitud_clase * (dif_frec_mayor_anterior /
                                            (dif_frec_mayor_anterior + dif_frec_mayor_posterior))

print("\nFrecuencia Mayor: ", frec_mayor)
print("Posterior a la mayor: ", frec_posterior)
print("Anterior a la mayor: ", frec_anterior)

# ////////////////////////////////////////////////////////////////

# Calculo de la varianza
varianza = suma_MA2 / (total_frecuencias - 1)

# ////////////////////////////////////////////////////////////////

# Calculo de la desviacion standar
desviacion = math.sqrt(varianza)

# ////////////////////////////////////////////////////////////////

# Calculo del coeficiente de variacion
coeficiente = (desviacion / media) * 100

# ////////////////////////////////////////////////////////////////

print("\nMediana: ", mediana)
# print("fm: ", fm)
print("\nLa moda (Método 1-Inspección): ", moda1)
print("La moda (Método 2-Pearson): ", moda2)
print("La moda (Método 3-Diferencia): ", moda3)
print("\nSuma de Pm-MA2*F: ", suma_MA2)
print("\nVarianza: ", varianza)
print("\nDesviacion Standar: ", desviacion)
print("\nCoeficiente de Variacion: ", round(coeficiente, 2), "%")

# ////////////////////////////////////////////////////////////////

# Calculo de la Representatividad

# Verificar si el coeficiente está entre 0 y 10
if 0 <= coeficiente <= 10:
    print("\nEs Altamente Representativa La Media Aritmetica")
elif 10 <= coeficiente <= 20:
    print("\nEs Bastante Representativa La Media Aritmetica")
elif 20 <= coeficiente <= 30:
    print("\nEs Poca Representativa La Media Aritmetica")
elif 30 <= coeficiente <= 40:
    print("\nEs Dudosamente Representativa La Media Aritmetica")
elif 40 <= coeficiente > 40:
    print("\nNo Tiene Representatividad La Media Aritmetica")

# ////////////////////////////////////////////////////////////////
