print("Ingrese su sueldo bruto")
SueldoBruto = float(input("> "))

SFS = SueldoBruto * 0.0287
AFP = SueldoBruto * 0.0304
Bonificacion = SueldoBruto * 0.10
SueldoAnual = SueldoBruto * 12

if SueldoAnual <= 416220.00:
    ISR_anual = 0
elif SueldoAnual <= 624329.00:
    ISR_anual = (SueldoAnual - 416220.01) * 0.15
elif SueldoAnual <= 867123.00:
    ISR_anual = ((SueldoAnual - 624329.01) * 0.20) + 31216.00
else:
    ISR_anual = ((SueldoAnual - 867123.01) * 0.25) + 79776.00

ISR = ISR_anual / 12
SueldoNeto = SueldoBruto + Bonificacion - (ISR + AFP + SFS)

print(f"\n--- Resultados ---")
print(f"ISR mensual: RD${ISR:.2f}")
print(f"Bonificación: RD${Bonificacion:.2f}")
print(f"AFP (3.04%): RD${AFP:.2f}")
print(f"SFS (2.87%): RD${SFS:.2f}")
print(f"Sueldo Neto: RD${SueldoNeto:.2f}")