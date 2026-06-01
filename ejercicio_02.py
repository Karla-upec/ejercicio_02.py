# Mi programa para operadora logística
# Karla Castillo - Fundamentos de Programación

# Inicializo variables
total_peso = 0.0          # Acumulador
cont_50 = 0               # Contador de envíos > 50 kg
hay_prioritario = False   # Bandera (True si hay algún paquete > 100 kg)

# Bucle para 5 paquetes
for i in range(1, 6):
    # Entrada del peso
    peso = float(input(f"Ingrese el peso del paquete {i} (kg): "))
    
    # Acumulador
    total_peso = total_peso + peso
    
    # Contador para >50 kg
    if peso > 50:
        cont_50 = cont_50 + 1
    
    # Bandera para prioritario (>100 kg)
    if peso > 100:
        hay_prioritario = True

# Salida del resumen final
print("\n--- RESUMEN LOGÍSTICO ---")
print("Peso total:", total_peso, "kg")
print("Cantidad de paquetes mayores a 50 kg:", cont_50)

if hay_prioritario:
    print("Sí existió al menos un envío prioritario (peso > 100 kg).")
else:
    print("No existió ningún envío prioritario.")