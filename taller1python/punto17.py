"""
Entradas
presupuesto anual-->float-->presupuesto
Salidas
presupuesto Ginecologia-->(presupuesto*0.40)
presupuesto Traumatología-->(presupuesto*0.30)
presupuesto Pediatría-->(presupuesto*0.30)
"""
presupuesto= float(input("Ingresa el presupuesto anual: "))
print("El area de Ginecologia le corresponde: $", presupuesto*0.40)
print("El area de Traumatología le corresponde: $", presupuesto*0.30)
print("El area de Pediatría le corresponde: $", presupuesto*0.30)
