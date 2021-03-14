#!/bin/bash
declare -i x y z
echo -n "Podaj  liczbe  calkowita: "
read x
s2.sh $x &
y=x*x
wait $!
y=y+$?
echo -n "Wynik: "
exit 0 