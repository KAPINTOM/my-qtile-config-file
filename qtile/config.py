# My Simple Qtile Config File
# Made by Kenneth Andrey Pinto Medina
# https://github.com/KAPINTOM

import os
import subprocess
import psutil

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# =============================================
# MODIFIER AND TERMINAL
# =============================================
# 'mod' is the modifier key used in your keybindings. "mod4" is the Super /
# Windows key on most keyboards. You can change it to "mod1" for Alt.
mod = "mod4"

# Default terminal used by keybindings which spawn a terminal.
# We use "kitty" here; change it to your preferred terminal (alacritty, rxvt,
# urxvt, xterm, etc.). If you leave it blank, gui apps that use the guess
# utility may fall back to a default.
terminal = "kitty"

# Special multimedia keys. Keep these strings as-is — they are the X11/evdev
# key names for brightness and audio keys and Qtile will map them for you.
brightup = "XF86MonBrightnessUp"
brightdown = "XF86MonBrightnessDown"
volup = "XF86AudioRaiseVolume"
voldown = "XF86AudioLowerVolume"
volmute = "XF86AudioMute"

# =============================================
# COLOURS
# =============================================
# Colors are stored as hex strings in a dictionary for easy reuse across the
# config. This centralises theme changes and prevents accidental typos when
# passing colors to widgets/layouts.
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
# AUTOSTART HOOK
# =============================================
# The @hook.subscribe.startup function runs when Qtile is starting. It's a
# common place to launch background services (compositor, clipboard manager,
# notification daemon, etc.).
#
# Robustness notes:
# - We check that the script exists before running it.
# - If the script isn't executable, we run it via /bin/bash. This prevents a
#   non-executable file from failing silently.
# - Avoid spawning blocking commands here (long-running interactive processes).

@hook.subscribe.startup
def autostart():
    """Run autostart script if present.

    Expected script path: ~/.config/qtile/scripts/autostart.sh
    (You can change the path below if you keep your autostart somewhere else.)
    """
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    if os.path.exists(script) and os.access(script, os.X_OK):
        # If executable, run directly so it can use its shebang.
        try:
            subprocess.call([script])
        except Exception:
            # If direct execution fails for any reason, fall back to running
            # the script with bash to avoid hard startup crashes.
            subprocess.call(["/bin/bash", script])
    elif os.path.exists(script):
        # Script exists but isn't executable: run with bash.
        subprocess.call(["/bin/bash", script])

# =============================================
# KEYS / KEYBINDINGS
# =============================================
# Keys are configured using libqtile.config.Key objects. Each Key takes:
#  - a list of modifier keys (e.g. [mod, "shift"]) or [] for none
#  - a key name (e.g. "Return", "space", "F1" or multimedia names above)
#  - an action, usually one of the lazy.* commands
#
# Notes & common pitfalls:
# - Use exact key names (case-sensitive). Function keys are "F1", "F2", ...
# - Avoid calling lazy.* methods when storing them (don't add parentheses).
# - Keep Key definitions readable so future edits are easier.

keys = [
    # Movement between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows around
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize windows (behavior depends on layout)
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Launch terminal / run commands
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Example of running a small script — change the path to your user/script
    Key([mod], "p", lazy.spawn("bash /home/kapm/.config/qtile/scripts/rofi-power-menu.sh"), desc="Abrir menú de energía"),

    # General actions
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Personal shortcuts / rofi
    Key([mod], "e", lazy.spawn("rofi -i -show drun -modi drun -show-icons"), desc="Lanzador rofi"),
    Key([mod], "w", lazy.spawn("rofi -i -show window -modi drun -show-icons"), desc="Lanzador rofi ventanas"),

    # Brightness
    Key([], brightup, lazy.spawn("brightnessctl set 10%+"), desc="Subir brillo"),
    Key([], brightdown, lazy.spawn("brightnessctl set 10%-"), desc="Bajar brillo"),

    # Volume control — device and mixer might need adjusting for your system
    Key([], volup, lazy.spawn("amixer -D 'default:2' sset Headphone 5%+"), desc="Subir volumen"),
    Key([], voldown, lazy.spawn("amixer -D 'default:2' sset Headphone 5%-"), desc="Bajar volumen"),
    Key([], volmute, lazy.spawn("amixer -D 'default:2' sset Headphone toggle"), desc="Mute"),
]

# =============================================
# VIRTUAL TERMINALS (Wayland-only)
# =============================================
# Some systems expose virtual terminals (VT1..VT7) and you may want to
# switch to them via keys. Changing virtual terminals is a concept tied to
# tty devices and on Wayland you can call change_vt. Attempting to add these
# keys on a system without the proper support can raise exceptions - so we
# check the runtime core name first.
try:
    core_name = getattr(qtile.core, "name", "")
except Exception:
    core_name = ""

if core_name == "wayland":
    # Only add these on Wayland sessions. Use "F1".."F7" (case sensitive).
    for vt in range(1, 8):
        keys.append(
            Key(["control", "mod1"], f"F{vt}", lazy.core.change_vt(vt), desc=f"Switch to VT{vt}")
        )

# =============================================
# GROUPS / WORKSPACES
# =============================================
# Groups are like virtual desktops. This simple setup creates groups named
# '1'..'9' and binds Mod+<number> to switch to the group and Mod+Shift+<number>
# to move the focused window to that group.

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

# =============================================
# LAYOUTS
# =============================================
# Layouts control how windows are placed. Make sure color arguments are
# strings (not lists) and that the layout you pick is available in your
# Qtile version.

layouts = [
    layout.Columns(border_focus="#00a2ff", border_normal="#000000", border_width=3, margin=0),
    layout.Max(border_focus="#00a2ff", border_width=0, margin=0),
    layout.Matrix(border_focus="#00a2ff", border_normal="#000000", border_width=3, margin=0),
]

# =============================================
# WIDGETS / BAR / SCREENS
# =============================================
# Widget defaults centralise font/padding and background colors. If a widget
# fails to import or crashes on startup, remove it and try again (common for
# custom widgets or distro-specific ones).

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font Bold",
    fontsize=15,
    padding=6,
    background=colors["background"],
    foreground=colors["foreground"],
)
extension_defaults = widget_defaults.copy()

# A single-screen example. For multiple screens, replicate this Screen block
# with different Bar configurations (or the same if you prefer symmetry).
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(foreground=colors["primary"], padding=10),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"], background=colors["background"]),

                widget.GroupBox(
                    disable_drag=True,
                    highlight_method="block",
                    active=colors["foreground"],
                    inactive=colors["gray"],
                    this_current_screen_border=colors["primary"],
                    other_current_screen_border=colors["gray"],
                    rounded=False,
                    margin_x=6,
                    margin_y=3,  # centered vertically
                    padding_x=6,
                    padding_y=6,  # increased for vertical centering
                    borderwidth=0,
                ),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"], background=colors["background"]),

                widget.WindowName(foreground=colors["primary"], padding=10),
                widget.Sep(linewidth=0, padding=10, foreground=colors["gray"], background=colors["background"]),

                # System stats
                widget.TextBox(text="CPU →", foreground=colors["success"], padding=0),
                widget.CPU(format="{load_percent:.0f}%", update_interval=2, foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),

                widget.TextBox(text="RAM →", foreground=colors["warning"], padding=0),
                widget.Memory(format="{MemPercent:.0f}%", measure_mem="G", update_interval=2, foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),

                widget.TextBox(text="NET →", foreground=colors["secondary"], padding=0),
                widget.Net(format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}", foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),

                widget.TextBox(text="VOL →", foreground=colors["primary"], padding=0),
                # Volume widget device/channel may need adjusting for your system.
                widget.Volume(foreground=colors["foreground"], padding=5, device='default:2', channel='Headphone'),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),

                widget.TextBox(text="BAT →", foreground=colors["success"], padding=0),
                widget.Battery(format="{percent:.0%}", foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),

                widget.Systray(icon_size=16, padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),

                widget.QuickExit(),

                widget.TextBox(text="TIME →", foreground=colors["warning"], padding=0),
                # Clock uses the user's timezone specified in the developer message
                widget.Clock(format="%d/%m/%y %H:%M", timezone="America/Bogota", foreground=colors["foreground"], padding=5),
                widget.Sep(linewidth=0, padding=5, foreground=colors["gray"], background=colors["background"]),
            ],
            20,  # bar height in pixels
            background=colors["background"],
            margin=[0, 0, 0, 0],
            opacity=1,
        ),
    ),
]

# =============================================
# MOUSE
# =============================================
# Drag/Click map floating window mouse actions. Important: when referencing
# lazy.* methods for the 'start' argument, do NOT call them (no parentheses).
# Passing the callable itself is required by Qtile.

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# =============================================
# OTHER QTILE SETTINGS
# =============================================
# These are common boolean flags and options. Keep them if you like default
# Qtile behavior; tweak as you become more comfortable.

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

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

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# Wayland-specific fallbacks (set to None to use defaults)
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

# wmname: sometimes set to help Java GUI apps that check for known window
# managers. We attempt to include the qtile version if available but fall
# back to a safe string to avoid exceptions during startup.
try:
    version = subprocess.run(['qtile', '--version'], capture_output=True, text=True, check=False).stdout.strip()
    wmname = f"Qtile {version}" if version else "Qtile"
except Exception:
    wmname = "Qtile"

# End of documented config
# ------------------------
# Notes for further customization:
# - If a widget causes Qtile to crash at startup, comment it out and try
#   launching qtile again. Check `~/.local/share/xorg/` logs or `journalctl -b`
#   for tracebacks.
# - For multi-monitor setups, define multiple Screen() entries in the
#   'screens' list above — one per monitor.
# - If you want me to add scratchpads, drop-down terminals, or a minimal
#   debug config (very small bar, few widgets), tell me which features you
#   want and I will modify this file accordingly.
