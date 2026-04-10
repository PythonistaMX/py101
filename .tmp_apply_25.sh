#!/usr/bin/env bash
set -e

# Capitulo 15
f15="/workspaces/py101/15_funciones.ipynb"
sed -i 's/aquÍ/aquí/g' "$f15"
sed -i 's/ningun tipo de acción/ningún tipo de acción/g' "$f15"
sed -i 's/funci;on/función/g' "$f15"
sed -i 's/deifne/define/g' "$f15"
sed -i 's/la funcion ```saludo()```/la función ```saludo()```/g' "$f15"
sed -i 's/bien defindos/bien definidos/g' "$f15"
sed -i 's/El resutado será/El resultado será/g' "$f15"
sed -i 's/la cuaL regresará/la cual regresará/g' "$f15"
sed -i 's/correpsondiente/correspondiente/g' "$f15"
sed -i 's/parámetros definidos en una función pertencen/parámetros definidos en una función pertenecen/g' "$f15"
sed -i 's/```ave```no/```ave``` no/g' "$f15"
sed -i 's/```<nommbre>```/```<nombre>```/g' "$f15"
sed -i 's/despelgará/desplegará/g' "$f15"
sed -i 's/corresdponderá/corresponderá/g' "$f15"
sed -i 's/operado de asignación/operador de asignación/g' "$f15"
sed -i 's/TyepeError/TypeError/g' "$f15"
sed -i 's/dichos argumentos se deben de dejar al principio de la sucesión de parámetros./dichos argumentos se deben dejar al final de la sucesión de parámetros./g' "$f15"

# Capitulo 22
f22="/workspaces/py101/22_bases_de_programacion_funcional.ipynb"
sed -i 's/A partir de concepto de cerradura,/A partir del concepto de cerradura (closure),/g' "$f22"
sed -i 's/a si misma/a sí misma/g' "$f22"
sed -i 's/argumento to/argumento texto/g' "$f22"
sed -i 's/del resutado de invocar/del resultado de invocar/g' "$f22"
sed -i 's/un recursos/un recurso/g' "$f22"
sed -i 's/del la expresión/de la expresión/g' "$f22"
sed -i 's/Python permite definir funciones en una sola línea/*Python* permite definir funciones en una sola línea/g' "$f22"
sed -i 's/número non\./número impar./g' "$f22"
