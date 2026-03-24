# My Simple Qtile Config File
# Made by Kenneth Andrey Pinto Medina
# https://github.com/KAPINTOM

# This configuration is designed to be simple, efficient, and visually appealing, with a focus on usability and aesthetics. It includes a clean bar with essential widgets, a consistent color scheme, and intuitive keybindings for managing windows and launching applications. The autostart function ensures that necessary applications and services are launched when Qtile starts, providing a seamless user experience from the moment you log in.

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
        border_width=0,
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
    padding=5,
    background=colors["background"],
    foreground=colors["foreground"],
)

# Using the same widget defaults for extension defaults to maintain a consistent look and feel across all widgets, ensuring that any new widgets added in the future will automatically inherit these settings for a cohesive appearance.
extension_defaults = widget_defaults.copy()

# =============================================
# BAR / SCREEN
# =============================================

# Using the same value for gaps and bar margin to create a consistent look
gaps_value = margins

# The bar is designed with consistent spacing and margins, using Gap widgets to create uniform gaps around the bar and between widgets, ensuring a cohesive and visually appealing layout.
screens = [
    Screen(

        # Using Gap widgets to create consistent spacing around the bar, ensuring a cohesive design with the defined margins
        left=Gap(gaps_value),
        right=Gap(gaps_value),
        top=Gap(gaps_value),

        # Bar configuration with consistent margins and spacing between widgets, using the defined colors and widget settings for a cohesive appearance
        bottom=bar.Bar(
            [
                # Separators with zero linewidth and consistent padding to create uniform spacing between widgets
                widget.Sep(linewidth=0, padding=15),

                #widget.TextBox(text="TIME →", foreground=colors["warning"], padding=0),
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

                widget.Sep(linewidth=0, padding=15),
            ],

            # Size of the bar is set to
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
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# =============================================
# FLOATING
# =============================================

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# =============================================
# OTHER SETTINGS
# =============================================

dgroups_key_binder = None
dgroups_app_rules = []

# Mouse focus settings
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

# Focus on newly opened windows
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False

wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
