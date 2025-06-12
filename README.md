# Qtile Configuration

A highly customized Qtile window manager configuration with system monitoring, custom keybindings, and autostart applications.

## Dependencies

Install these packages using your distribution's package manager:

### Core Dependencies
```bash
# Window Manager
qtile                  # The window manager itself
python-psutil         # For system monitoring widgets
picom                 # Compositor for transparency effects
nitrogen             # Wallpaper manager
network-manager-applet # Network management tray icon (nm-applet)
volumeicon           # Volume control tray icon
brightnessctl       # Brightness control utility
rofi                # Application launcher

# Audio Control
alsa-utils          # For amixer volume control

# Optional but recommended
acpi                # For battery monitoring
python-dbus        # For various system integrations
```

## Features

### Window Management

#### Basic Controls
- **Super + Arrow Keys**: Navigate between windows
- **Super + Space**: Cycle through windows
- **Super + Shift + Arrow Keys**: Move windows within layout
- **Super + Control + Arrow Keys**: Resize windows
- **Super + N**: Reset window sizes to default

#### Layout Controls
- **Super + Tab**: Cycle through layouts
- **Super + Shift + Return**: Toggle split/unsplit in stack layout
- **Super + F**: Toggle fullscreen
- **Super + T**: Toggle floating mode

#### Window Actions
- **Super + Q**: Close focused window
- **Super + Control + R**: Reload Qtile config
- **Super + Control + Q**: Shutdown Qtile

### Workspaces
- **Super + [1-9]**: Switch to workspace 1-9
- **Super + Shift + [1-9]**: Move window to workspace 1-9

### Applications
- **Super + Return**: Launch terminal
- **Super + E**: Launch Rofi application menu
- **Super + W**: Launch Rofi window switcher

### System Controls
- **XF86AudioRaiseVolume**: Volume up
- **XF86AudioLowerVolume**: Volume down
- **XF86AudioMute**: Toggle mute
- **XF86MonBrightnessUp**: Brightness up
- **XF86MonBrightnessDown**: Brightness down

## Layouts
1. **Columns**: Main layout with red borders (#ff0000) and black normal borders
2. **Max**: Maximized layout with red borders
3. **Matrix**: Grid-based layout with similar border configuration

## Status Bar

The bottom bar includes:
- Current layout indicator
- Workspace indicators with line highlighting
- Window name (dark gray background)
- Network usage monitor (blue background)
- CPU usage monitor (orange background)
- CPU temperature sensor
- Memory usage percentage (green background)
- Memory usage in MB (green background)
- System tray (purple background)
- Volume widget (purple background)
- Clock (Bogota timezone)
- Quick exit button

## Autostart Applications

The following applications start automatically:
```bash
picom               # Compositor
nitrogen           # Wallpaper restoration
nm-applet          # Network manager applet
volumeicon         # Volume control icon
```

## Configuration Files

### Main Configuration
- **Location**: `~/.config/qtile/config.py`
- **Contents**: All window manager settings, keybindings, and layouts

### Autostart Script
- **Location**: `~/.config/qtile/autostart.sh`
- **Permissions**: Make sure it's executable (`chmod +x autostart.sh`)

## Additional Settings

### Mouse Behavior
- Focus follows mouse
- Floating windows stay above
- Cursor warping disabled
- Click to focus without raising window

### Floating Window Rules
Predefined rules for:
- Dialog windows
- Git GUI tools
- SSH password prompts
- GPG password entry

### Display Settings
- Auto fullscreen enabled
- Smart focus on window activation
- Automatic screen reconfiguration
- X11 cursor size: 24px

## Java Application Compatibility
The window manager identifies itself as "LG3D" for compatibility with Java applications.