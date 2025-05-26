import matplotlib.pyplot as plt

# Tiempos obtenidos después de ejecutar ambos códigos
tiempo_original = 15.23  # Reemplazar por tu valor real
tiempo_optimizado = 1.78  # Reemplazar por tu valor real

# Comparativa
plt.figure(figsize=(8, 4))
plt.bar(['Original', 'Optimizado'], [tiempo_original, tiempo_optimizado], color=['red', 'green'])
plt.ylabel('Tiempo (segundos)')
plt.title('Comparativa de Tiempos de Ejecución')
plt.grid(True)
plt.savefig('comparativa_tiempos.png')
plt.show()

# Distribución (ejemplo)
labels = ['Función es_primo', 'Bucle principal', 'Otros']
sizes = [60, 30, 10]
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.1, 0, 0)

plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribución de Tiempo (Ejemplo)')
plt.savefig('distribucion_tiempo.png')
plt.show()