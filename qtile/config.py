# My Simple Qtile Config File
# Made by Kenneth Andrey Pinto Medina
# https://github.com/KAPINTOM

import os
import subprocess

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.bar import Gap

# =============================================
# MODIFIER AND TERMINAL
# =============================================

mod = "mod4"
terminal = "kitty"

brightup = "XF86MonBrightnessUp"
brightdown = "XF86MonBrightnessDown"

volup = "XF86AudioRaiseVolume"
voldown = "XF86AudioLowerVolume"
volmute = "XF86AudioMute"

playpause = "XF86AudioPlay"
nexttrack = "XF86AudioNext"
prevtrack = "XF86AudioPrev"

# =============================================
# COLOURS
# =============================================

colors = {
    "background": "#1a1a1a",
    "foreground": "#ffffff",
    "primary": "#5294e2",
    "secondary": "#b16286",
    "warning": "#d79921",
    "error": "#cc241d",
    "success": "#98971a",
    "gray": "#3c3836",
}

# =============================================
# AUTOSTART
# =============================================

@hook.subscribe.startup
def autostart():
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")

    if os.path.exists(script) and os.access(script, os.X_OK):
        try:
            subprocess.call([script])
        except Exception:
            subprocess.call(["/bin/bash", script])
    elif os.path.exists(script):
        subprocess.call(["/bin/bash", script])

# =============================================
# KEYS
# =============================================

keys = [

    # Focus
    Key([mod], "left", lazy.layout.left()),
    Key([mod], "right", lazy.layout.right()),
    Key([mod], "down", lazy.layout.down()),
    Key([mod], "up", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # Move windows
    Key([mod, "shift"], "left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up()),

    # Resize
    Key([mod, "control"], "left", lazy.layout.grow_left()),
    Key([mod, "control"], "right", lazy.layout.grow_right()),
    Key([mod, "control"], "down", lazy.layout.grow_down()),
    Key([mod, "control"], "up", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Power menu – fixed to use expanduser
    Key([mod], "p", lazy.spawn(["bash", os.path.expanduser("~/.config/qtile/scripts/rofi-power-menu.sh")])),

    # Layout
    Key([mod], "Tab", lazy.next_layout()),

    # Window actions
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),

    # Qtile
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Rofi
    Key([mod], "e", lazy.spawn("rofi -i -show drun -show-icons")),
    Key([mod], "w", lazy.spawn("rofi -i -show window -show-icons")),

    # Screenshot
    Key(
        [],
        "Print",
        lazy.spawn("bash -c 'mkdir -p ~/Screenshots && maim ~/Screenshots/screenshot-$(date +%Y-%m-%d-%H%M%S).png'")
    ),

    # Brightness
    Key([], brightup, lazy.spawn("brightnessctl set 10%+")),
    Key([], brightdown, lazy.spawn("brightnessctl set 10%-")),

    # Volume
    Key([], volup, lazy.spawn("amixer sset Master 5%+")),
    Key([], voldown, lazy.spawn("amixer sset Master 5%-")),
    Key([], volmute, lazy.spawn("amixer sset Master toggle")),

    # Media
    Key([], playpause, lazy.spawn("playerctl play-pause")),
    Key([], nexttrack, lazy.spawn("playerctl next")),
    Key([], prevtrack, lazy.spawn("playerctl previous")),
]

# =============================================
# GROUPS
# =============================================

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        ]
    )

# =============================================
# LAYOUTS
# =============================================

# Using a single variable for margins to ensure consistency across layouts and bars
margins = 5

layouts = [

    layout.Columns(
        border_focus="#eb0bff",
        border_normal="#000000",
        border_width=1,
        margin=margins
    ),

    layout.Max(
        border_focus="#008cff",
        border_width=0,
        margin=0
    ),

]

# =============================================
# WIDGETS
# =============================================

widget_defaults = dict(
    font="Cascadia Code",
    fontsize=15,
    padding=6,
    background=colors["background"],
    foreground=colors["foreground"],
)

extension_defaults = widget_defaults.copy()

# =============================================
# BAR / SCREEN
# =============================================

# Using the same value for gaps and bar margin to create a consistent look
gaps_value = margins

screens = [
    Screen(

        left=Gap(gaps_value),
        right=Gap(gaps_value),
        top=Gap(gaps_value),

        bottom=bar.Bar(
            [
                widget.TextBox(text="TIME →", foreground=colors["warning"], padding=0),

                widget.Clock(
                    format="%d/%m/%y %H:%M",
                    timezone="America/Bogota",
                    padding=5
                ),

                widget.CurrentLayout(
                    foreground=colors["primary"],
                    padding=10
                ),

                widget.GroupBox(
                    disable_drag=True,
                    highlight_method="block",
                    active=colors["foreground"],
                    inactive=colors["gray"],
                    this_current_screen_border=colors["primary"],
                    other_current_screen_border=colors["gray"],
                    rounded=False,
                    margin_x=6,
                    margin_y=3,
                    padding_x=6,
                    padding_y=6,
                    borderwidth=0,
                ),

                widget.Sep(linewidth=0, padding=10),

                widget.WindowName(
                    foreground=colors["primary"],
                    padding=10
                ),

                widget.Sep(linewidth=0, padding=10),

                widget.TextBox(text="CPU →", foreground=colors["success"], padding=0),

                widget.CPU(
                    format="{load_percent:.0f}%",
                    update_interval=2,
                    padding=5
                ),

                widget.Sep(linewidth=0, padding=5),

                widget.TextBox(text="RAM →", foreground=colors["warning"], padding=0),

                widget.Memory(
                    format="{MemPercent:.0f}%",
                    update_interval=2,
                    padding=5
                ),

                widget.Sep(linewidth=0, padding=5),

                widget.TextBox(text="NET →", foreground=colors["secondary"], padding=0),

                widget.Net(
                    format="{down:6.0f}{down_suffix} ↓↑ {up:6.0f}{up_suffix}",
                    padding=5
                ),

                widget.Sep(linewidth=0, padding=5),

                widget.TextBox(text="VOL →", foreground=colors["primary"], padding=0),

                widget.Volume(
                    device='default',
                    channel='Master',
                    padding=5
                ),

                widget.Sep(linewidth=0, padding=5),

                widget.TextBox(text="BAT →", foreground=colors["success"], padding=0),

                widget.Battery(
                    format="{percent:.0%}",
                    padding=5
                ),

                widget.Sep(linewidth=0, padding=5),

                widget.Systray(icon_size=16, padding=5),

                widget.Sep(linewidth=0, padding=5),

                widget.QuickExit(default_text="[ ⏻ ]"),

            ],
            22,
            background=colors["background"],
            margin=[gaps_value,0,0,0]
        ),
    ),
]

# =============================================
# MOUSE
# =============================================

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# =============================================
# FLOATING
# =============================================

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)

# =============================================
# OTHER SETTINGS
# =============================================

dgroups_key_binder = None
dgroups_app_rules = []

follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False

wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
