from boa import Boa
from huron import Huron




# Parametros de la Boa
name_boa = "super_python"
weight_boa = 400
age_boa = 5550
pais_origen_boa = "Colombia"
impuesto_boa = 20

boa_1 = Boa(name_boa, weight_boa, age_boa, pais_origen_boa, impuesto_boa)

boa_1.hacer_ruido()
boa_1.comer_raton(3)
boa_1.comer_raton(5)
boa_1.comer_raton(5)
boa_1.comer_raton(5)
boa_1.contar_ratones_comidos()
boa_1.calcular_flete()


# Parametros de la Uron
name_uron = "super_python"
weight_uron = 400
age_uron = 5550
pais_origen_uron = "Venezuela"
impuesto_uron = 0.00000000020333222544

uron_1 = Huron(name_uron, weight_uron, age_uron, pais_origen_uron, impuesto_uron)

# uron_1.hacer_ruido()



