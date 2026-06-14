# calculo e nomina
identificacion_empleado = input("Digite identificación del empleado: ")
nombre_empleado = input("Digite nombre del empleado: ")

print("Bienvenido", nombre_empleado)

salario_base_mensual = 1750905

horas_trabajadas = int(input("Digite horas trabajadas: "))
valor_hora = salario_base_mensual / 240

print("Valor hora:", round(valor_hora, 2))

ingresos_adicionales = float(input("Digite ingresos adicionales: "))
auxilio_transporte = float(input("Digite auxilio transporte: "))

# Descuentos trabajador
salud = salario_base_mensual * 0.04
pension = salario_base_mensual * 0.04

# Aportes empresa
arl = salario_base_mensual * 0.00522
sena = salario_base_mensual * 0.02
icbf = salario_base_mensual * 0.03
caja_de_compensacion = salario_base_mensual * 0.04

# Prestaciones sociales
primas = salario_base_mensual * 0.0833
cesantias = salario_base_mensual * 0.0833
intereses_cesantias = salario_base_mensual * 0.01
vacaciones = salario_base_mensual * 0.0417

total_ingresos = (
    salario_base_mensual +
    ingresos_adicionales +
    auxilio_transporte
)

total_de_descuentos = salud + pension

total_prestaciones = (
    primas +
    cesantias +
    intereses_cesantias +
    vacaciones
)

salario_neto = total_ingresos - total_de_descuentos

print("\nREPORTE DE NÓMINA")
print("-" * 50)

print("Empleado:", nombre_empleado)
print("Identificación:", identificacion_empleado)

print(f"Total ingresos: ${total_ingresos:,.0f}")
print(f"Salud: ${salud:,.0f}")
print(f"Pensión: ${pension:,.0f}")
print(f"Total descuentos: ${total_de_descuentos:,.0f}")
print(f"Prestaciones: ${total_prestaciones:,.0f}")
print(f"Salario neto: ${salario_neto:,.0f}")

print("\nREPORTE DE NÓMINA")
print("-" * 60)
# ESTRUCTURA  A LA NOMINA 
print("{:<20} {:>20}".format("CONCEPTO", "VALOR"))
print("-" * 60)

print("{:<20} {:>20,.0f}".format("Salario Base", salario_base_mensual))
print("{:<20} {:>20,.0f}".format("Ingresos Adic.", ingresos_adicionales))
print("{:<20} {:>20,.0f}".format("Auxilio Transporte", auxilio_transporte))

print("-" * 60)

print("{:<20} {:>20,.0f}".format("Salud (4%)", salud))
print("{:<20} {:>20,.0f}".format("Pensión (4%)", pension))
print("{:<20} {:>20,.0f}".format("Total Descuentos", total_de_descuentos))

print("-" * 60)

print("{:<20} {:>20,.0f}".format("Salario Neto", salario_neto))
