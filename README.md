# Qtile Window Manager Configuration

![Qtile](https://img.shields.io/badge/Qtile-Python%20WM-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A sophisticated and highly optimized configuration for Qtile, a tiling window manager written in Python. This setup is designed for power users who value efficiency, information density, and keyboard-driven workflows.

## Features

### **Window Management**
- **Multiple Layouts**: Columns, Max, and Matrix layouts
- **Intelligent Tiling**: Automatic window arrangement with manual controls
- **Floating Windows**: Support for dialog boxes and temporary windows
- **Workspace Management**: 9 virtual desktops for organized workflow

### **System Integration**
- **Real-time Monitoring**: Comprehensive system status in status bar
- **Multimedia Controls**: Hardware key support for brightness and volume
- **Network Management**: Built-in network applet integration
- **Power Management**: Battery monitoring and power controls

### **Customization & UX**
- **Rofi Integration**: Application and window launchers
- **Visual Feedback**: Color-coded status information
- **Keyboard-Centric**: Extensive keybindings for all operations
- **Auto-start Services**: Seamless desktop environment initialization

## File Structure

```
~/.config/qtile/
├── config.py          # Main Qtile configuration
└── autostart.sh       # Startup applications script
```

## Installation & Setup

### Prerequisites

**Essential Packages:**
```bash
# Qtile and core dependencies
sudo pacman -S qtile python-psutil

# System components
sudo pacman -S rofi nitrogen network-manager-applet
```

**Optional Dependencies:**
```bash
# Audio control
sudo pacman -S alsa-utils volumeicon

# Compositor (optional)
sudo pacman -S picom

# System monitoring tools
sudo pacman -S lm_sensors acpi
```

### Installation Steps

1. **Clone or download these configuration files:**
   ```bash
   cp config.py ~/.config/qtile/
   cp autostart.sh ~/.config/qtile/
   chmod +x ~/.config/qtile/autostart.sh
   ```

2. **Ensure Qtile is set as your window manager:**
   - Add `exec qtile` to your `~/.xinitrc` if using startx
   - Configure your display manager to launch Qtile

3. **Restart Qtile or your session to apply changes**

## Keybindings Reference

### **Window Navigation**
| Key Combination | Action |
|----------------|---------|
| `Super + Arrow Keys` | Move focus between windows |
| `Super + Shift + Arrow Keys` | Move windows between positions |
| `Super + Control + Arrow Keys` | Resize windows |
| `Super + Space` | Cycle window focus |
| `Super + n` | Reset window sizes |

### **Application Launchers**
| Key Combination | Action |
|----------------|---------|
| `Super + Return` | Launch terminal |
| `Super + e` | Rofi application launcher |
| `Super + w` | Rofi window switcher |
| `Super + r` | Command prompt (commented) |

### **System Controls**
| Key Combination | Action |
|----------------|---------|
| `Super + Tab` | Switch between layouts |
| `Super + f` | Toggle fullscreen |
| `Super + t` | Toggle floating window |
| `Super + q` | Close focused window |
| `Super + Control + r` | Reload Qtile config |
| `Super + Control + q` | Shutdown Qtile |

### **Workspace Management**
| Key Combination | Action |
|----------------|---------|
| `Super + 1-9` | Switch to workspace |
| `Super + Shift + 1-9` | Move window to workspace |

### **Hardware Controls**
| Key | Action |
|-----|---------|
| `Brightness Up/Down` | Adjust display brightness |
| `Volume Up/Down` | Adjust audio volume |
| `Volume Mute` | Toggle audio mute |

## Status Bar Configuration

The status bar provides comprehensive system monitoring:

### **Left Section**
- **Layout Indicator**: Current window layout
- **Workspace Switcher**: Visual group selection with line highlighting
- **Window Name**: Currently focused application

### **System Monitoring Center**
- **Network**: Real-time upload/download speeds
  - *Color: Deep Blue (#002980)*
- **CPU**: Processor usage percentage
  - *Color: Orange-Red (#802900)*
- **Temperature**: CPU thermal monitoring
  - *Color: Dark Red (#800002)*
- **Memory**: RAM usage percentage and absolute values
  - *Color: Green (#008033)*
- **Battery**: Power status and percentage
  - *Color: Purple (#6a369e)*

### **Right Section**
- **System Tray**: Background applications and notifications
- **Volume Control**: Audio level indicator
- **Clock**: Date and time (Bogotá timezone)
- **Quick Exit**: Fast session logout

## Layouts Available

### **1. Columns Layout**
- **Features**: Master and stack areas, resizable columns
- **Visual**: Red focus borders (#ff0000), 3px border width
- **Usage**: Primary layout for most workflows

### **2. Max Layout**
- **Features**: Fullscreen window focus
- **Visual**: No borders, no margins
- **Usage**: Maximized applications, presentations

### **3. Matrix Layout**
- **Features**: Grid-based window arrangement
- **Visual**: Red focus borders, 5px border width
- **Usage**: Organizing multiple windows in grid pattern

## Autostart Services

The `autostart.sh` script initializes essential desktop services:

### **Active Services**
- **Nitrogen**: Wallpaper restoration and management
- **Network Manager Applet**: System tray network controls

### **Commented Services (Available for Enablement)**
- **Picom**: Compositor for visual effects (transparency, shadows)
- **Volumeicon**: Audio volume system tray control

To enable any commented service, remove the `#` and ensure the package is installed.

## Customization Guide

### **Adding New Keybindings**
```python
Key([mod], "p", lazy.spawn("your-application"), desc="Launch Your Application")
```

### **Creating New Workspace Rules**
```python
groups = [
    Group("1", label="", layout="columns"),
    Group("2", label="", layout="max", matches=[Match(wm_class="firefox")]),
]
```

### **Custom Widgets**
Add new widgets to the status bar by inserting them in the `screens` section:
```python
widget.YourWidget(background="#your_color", **widget_defaults)
```

### **Theme Modification**
Change color scheme by updating the color values throughout `config.py`:
```python
border_focus=["#your_color"]  # Window focus color
background="#your_color"      # Widget background
```

## Advanced Features

### **Floating Window Rules**
Automatically float specific application types:
- Password dialogs (pinentry)
- System confirmation dialogs
- SSH key prompts
- Git interface windows

### **Multi-Monitor Support**
Ready for multi-monitor setups with screen-specific configurations.

### **Java Application Support**
WM name emulation ensures compatibility with Java-based applications.

## Troubleshooting

### **Common Issues**

1. **Missing dependencies**
   ```bash
   # Check for missing Python packages
   pip install psutil
   ```

2. **Audio controls not working**
   ```bash
   # Ensure ALSA is configured
   amixer sset Master unmute
   ```

3. **Brightness controls not working**
   ```bash
   # Check brightnessctl permissions
   sudo chmod +s /usr/bin/brightnessctl
   ```

4. **Widgets not displaying**
   - Verify all required system monitoring tools are installed
   - Check sensor names match your hardware

### **Debugging**
- Check Qtile logs: `tail -f ~/.local/share/qtile/qtile.log`
- Reload config: `Super + Control + r`
- Test individual widgets by enabling them one at a time

## Contributing

Feel free to fork this configuration and adapt it to your needs. Some areas for improvement:

- Add weather or email notifications
- Implement workspace-specific applications
- Add screenshot functionality
- Create theme variants

## License

This configuration is released under the MIT License, same as Qtile itself.

## Credits

- **Qtile Developers**: For creating an amazing window manager
- **Qtile Community**: For extensive documentation and examples
- **Arch Linux Community**: For excellent documentation on tiling WMs
- **DeepSeek**: For write this readme, I'm too lazy to write it myself

---

**Note**: This configuration is continuously refined. Check back periodically for updates and new features tailored for productive development workflows.
