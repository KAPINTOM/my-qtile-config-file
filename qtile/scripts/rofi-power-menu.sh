#!/bin/bash

# Opciones del menú
options="Apagar pantalla\nCerrar sesión\nReiniciar\nSuspender\nApagar\nHibernar\nBloquear"

# Mostrar menú con rofi
chosen=$(echo -e "$options" | rofi -dmenu -p "⚡ Energía" -theme-str 'window {width: 15%;} listview {lines: 6;}')

# Ejecutar acción según la opción seleccionada
case "$chosen" in
    "Apagar pantalla")
        xset dpms force standby ;;
    "Cerrar sesión")
        qtile cmd-obj -o cmd -f shutdown ;;
    "Reiniciar")
        systemctl reboot ;;
    "Suspender")
        systemctl suspend ;;
    "Apagar")
        systemctl poweroff ;;
    "Hibernar")
        systemctl hibernate ;;
    "Bloquear")
        dm-tool lock ;;
esac
