# =============================================
# IMPORTS Y CONFIGURACIONES BÁSICAS
# =============================================

import psutil
import os
import subprocess
import libqtile
from psutil import *
from libqtile.widget import *
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from libqtile.backend.wayland import InputConfig


if qtile.core.name == "x11":
    term = "kitty"  # For X11
elif qtile.core.name == "wayland":
    term = "kitty"   # For Wayland (or use 'alacritty', 'kitty')

    
# =============================================
# CONFIGURACIÓN DE TECLAS MODIFICADORAS
# =============================================

mod = "mod4"  # Tecla Super/Windows
terminal = "kitty"  # Terminal por defecto del sistema

# Definición de teclas especiales para funciones del sistema

brightup = "XF86MonBrightnessUp"
brightdown = "XF86MonBrightnessDown"
volup = "XF86AudioRaiseVolume"
voldown = "XF86AudioLowerVolume"
volmute = "XF86AudioMute"

# =============================================
# PALETA DE COLORES MEJORADA
# =============================================

colors = {
    "background": "#1a1a1a",
    "foreground": "#ffffff",
    "primary": "#5294e2",
    "secondary": "#b16286",
    "warning": "#d79921",
    "error": "#cc241d",
    "success": "#98971a",
    "gray": "#3c3836"
}

# =============================================
# HOOK DE INICIO AUTOMÁTICO
# =============================================

@hook.subscribe.startup
def autostart():
    """Ejecuta script de autostart al iniciar Qtile"""
    home = os.path.expanduser("/home/kapm/.config/qtile/scripts/autostart.sh")
    subprocess.call(home)

# =============================================
# CONFIGURACIÓN DE TECLADO (KEYBINDINGS)
# =============================================

keys = [
    # ========== NAVEGACIÓN ENTRE VENTANAS ==========

    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # ========== MOVIMIENTO DE VENTANAS ==========

    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # ========== REDIMENSIONAMIENTO DE VENTANAS ==========

    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # ========== DISPOSICIÓN DE VENTANAS ==========

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # ========== MENÚ PERSONALIZADO DE ENERGÍA ==========

    Key([mod], "p", lazy.spawn("bash /home/kapm/.config/qtile/scripts/rofi-power-menu.sh"), desc="Abrir menú de energía"),
    
    # ========== GESTIÓN GENERAL ==========

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # ========== KEYBINDINGS PERSONALIZADOS KAPM1001 ==========

    Key([mod], "e", lazy.spawn("rofi -i -show drun -modi drun -show-icons"), desc="Lanzador rofi"),
    Key([mod], "w", lazy.spawn("rofi -i -show window -modi drun -show-icons"), desc="Lanzador rofi ventanas"),
    Key([], brightup, lazy.spawn("brightnessctl set 10%+"), desc="Subir brillo"),
    Key([], brightdown, lazy.spawn("brightnessctl set 10%-"), desc="Bajar brillo"),
    Key([], volup, lazy.spawn("amixer -D 'default' sset Master 10%+"), desc="Subir volumen"),
    Key([], voldown, lazy.spawn("amixer -D 'default' sset Master 10%-"), desc="Bajar volumen"),
    Key([], volmute, lazy.spawn("amixer -D 'default' sset Master toggle"), desc="Mute"),
]

# =============================================
# CONFIGURACIÓN DE VIRTUAL TERMINALS (WAYLAND)
# =============================================

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# =============================================
# CONFIGURACIÓN DE GRUPOS DE TRABAJO
# =============================================

groups = [Group(i) for i in "123456789"]

# Keybindings para cambiar entre grupos

for i in groups:
    keys.extend(
        [
            # mod + número de grupo = cambiar al grupo
            
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
            
            # mod + shift + número = cambiar y mover ventana al grupo
            
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}"),
        ]
    )

# =============================================
# CONFIGURACIÓN DE DISPOSICIONES (LAYOUTS)
# =============================================

layouts = [
    layout.Columns(border_focus=["#00a2ff"], border_normal=["#000000"], border_width=3, margin=0),
    layout.Max(border_focus=["#00a2ff"], border_width=0, margin=0),

    # Layouts adicionales disponibles
    
    layout.Matrix(border_focus=["#00a2ff"], border_normal=["#000000"], border_width=3, margin=0),
]

# =============================================
# CONFIGURACIÓN DE WIDGETS Y BARRA
# =============================================

# Configuración por defecto para widgets

widget_defaults = dict(
    font="Cascadia Code NF Bold Italic",
    fontsize=15,
    padding=6,
    background=colors["background"],
    foreground=colors["foreground"],
)
extension_defaults = widget_defaults.copy()

# Configuración de la barra principal

screens = [
    Screen(
        bottom=bar.Bar(
            [

                # Widget de layout actual

                widget.CurrentLayout(foreground=colors["primary"], padding=10),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"], background=colors["background"]),
                
                # Widget de grupos de trabajo

                widget.GroupBox(
                    highlight_method="line",
                    highlight_color=[colors["primary"], colors["gray"]],
                    this_current_screen_border=colors["primary"],
                    this_screen_border=colors["gray"],
                    other_current_screen_border=colors["gray"],
                    other_screen_border=colors["gray"],
                    urgent_border=colors["error"],
                    urgent_text=colors["error"],
                    rounded=False,
                    margin_x=0,
                    margin_y=2,
                    padding_x=8,
                    padding_y=4,
                ),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"], background=colors["background"]),
                
                # Widget de nombre de ventana

                widget.WindowName(foreground=colors["primary"], max_chars=60, padding=10),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"], background=colors["background"]),
                
                # ========== WIDGETS DEL SISTEMA ==========

                # CPU

                widget.TextBox(text="CPU →", foreground=colors["success"], padding=0),
                widget.CPU(format="{load_percent:.0f}%", update_interval=2, foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Memoria RAM

                widget.TextBox(text="RAM →", foreground=colors["warning"], padding=0),
                widget.Memory(format="{MemPercent:.0f}%", measure_mem="G", update_interval=2, foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Red

                widget.TextBox(text="NET →", foreground=colors["secondary"], padding=0),
                widget.Net(format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}", foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Volumen

                widget.TextBox(text="VOL →", foreground=colors["primary"], padding=0),
                widget.Volume(foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Batería

                widget.TextBox(text="BAT →", foreground=colors["success"], padding=0),
                widget.Battery(format="{percent:.0%}", foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Systray (área de notificaciones)

                widget.Systray(icon_size=16, padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Reloj

                widget.TextBox(text="TIME →", foreground=colors["warning"], padding=0),
                widget.Clock(format="%d/%m/%y %H:%M", timezone="America/Bogota", foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
                
                # Botón de salida rápida
                #widget.QuickExit(foreground=colors["error"], padding=10),
            ],
            18,  # Altura de la barra
            background=colors["background"],
            margin=[0, 0, 0, 0],  # Sin márgenes
            opacity=0.95,
        ),
    ),
]

# =============================================
# CONFIGURACIÓN DEL RATÓN
# =============================================

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# =============================================
# CONFIGURACIONES AVANZADAS
# =============================================

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

# Configuración de ventanas flotantes

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Otras configuraciones

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# Configuración para Wayland

wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

# Identificación del WM para compatibilidad con aplicaciones Java

version = subprocess.run(['qtile', '--version'], capture_output=True, text=True).stdout.strip()
wmname = f"Qtile {version}"
