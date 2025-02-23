# My Personal Qtile Configuration Repository 🖥️

Welcome to my **personal Qtile configuration repository**! This repository contains my custom configuration files for the **Qtile** window manager, tailored to my workflow, preferences, and aesthetic tastes. Qtile is a highly customizable tiling window manager for Linux, and this configuration reflects my personal setup, optimized for productivity, performance, and visual appeal.

## What's Inside? 📂

The repository contains two main files, located in the `~/.config/qtile/` directory:

### 1. **`autostart.sh`** 🚀
   - **Description**: This is a Bash script that runs automatically when Qtile starts. It initializes essential services and applications to ensure a smooth desktop experience.
   - **Technical Details**:
     - **Picom**: Starts the Picom compositor for window transparency, shadows, and other visual effects.
     - **Nitrogen**: Restores the desktop wallpaper using Nitrogen, a lightweight wallpaper manager.
     - **Network Manager Applet**: Launches `nm-applet`, a system tray applet for managing network connections.
     - **Volume Icon**: Kills any existing `volumeicon` processes and restarts it to manage audio volume via a system tray icon.
     - **Auto-mount**: Automatically mounts a specific drive (`/dev/sdb1`) using `udisksctl`.

   #!/bin/bash

   picom &  # Start Picom compositor
   nitrogen --restore &  # Restore wallpaper
   nm-applet &  # Launch network manager applet
   pkill -f volumeicon  # Kill existing volumeicon processes
   sleep 1  # Wait for 1 second
   volumeicon &  # Start volumeicon for audio control
   sudo udisksctl mount -b /dev/sdb1 &  # Auto-mount a specific drive

### 2. **`config.py`** 🛠️
   - **Description**: This is the main configuration file for Qtile, written in Python. It defines keybindings, layouts, widgets, and other settings to customize the window manager.
   - **Technical Details**:
     - **Keybindings**: Custom keybindings for window management, application launching, and system controls (e.g., brightness, volume).
     - **Layouts**: Multiple tiling layouts, including `Columns`, `Max`, and `Matrix`, with customizable borders and margins.
     - **Widgets**: A status bar with widgets for system monitoring (CPU, memory, network), a clock, and a system tray.
     - **Autostart**: Integrates with `autostart.sh` to launch essential services on startup.
     - **Custom Commands**: Includes commands for launching applications like `rofi` for application and window management.

   # Keybindings for window management
   keys = [
       Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
       Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
       Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
       Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
       Key([mod], "e", lazy.spawn("rofi -i -show drun -modi drun -show-icons"), desc="Launch rofi"),
       Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+"), desc="Increase brightness"),
       Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D 'default' sset Master 10%+"), desc="Increase volume"),
   ]

   # Layouts with custom borders and margins
   layouts = [
       layout.Columns(border_focus=["#ff0000"], border_normal=["#000000"], border_width=5, margin=5),
       layout.Max(border_focus=["#ff0000"], border_width=5, margin=5),
       layout.Matrix(border_focus=["#ff0000"], border_normal=["#000000"], border_width=5, margin=5),
   ]

   # Widgets for the status bar
   screens = [
       Screen(
           bottom=bar.Bar(
               [
                   widget.CurrentLayout(),
                   widget.GroupBox(highlight_method="line"),
                   widget.WindowName(background="#191919"),
                   widget.Net(format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}", background="#002980"),
                   widget.CPU(update_interval=2, background="#802900"),
                   widget.Memory(format='{MemPercent: .0f}', update_interval=2, background="#008033"),
                   widget.Clock(format="%d/%m/%y %H:%M", timezone="America/Bogota"),
                   widget.Systray(background="#2a0033"),
                   widget.QuickExit(),
               ],
               24,
           ),
       ),
   ]

## Folder Structure 📁

The configuration files are located in the `~/.config/qtile/` directory, which is the standard location for Qtile configurations. The structure is as follows:

~/.config/qtile/
├── autostart.sh
└── config.py

## How to Use These Configurations? 🛠️

1. **Clone the repository** or download the configuration files.
2. Place the `autostart.sh` and `config.py` files in the `~/.config/qtile/` directory.
3. Ensure that `autostart.sh` is executable by running:

bash

   chmod +x ~/.config/qtile/autostart.sh
   
6. Restart Qtile to apply the new configuration.

## Customization and Contributions 🤝

This configuration is highly personalized, but feel free to adapt it to your needs! If you have improvements or additional features, contributions are welcome. Just fork the repository, make your changes, and submit a pull request.

## Key Features of My Configuration 🎯

### **Keybindings** ⌨️
- **Window Management**: Move, resize, and switch between windows with ease.
- **Application Launcher**: Use `rofi` to quickly launch applications or switch between open windows.
- **System Controls**: Adjust brightness, volume, and mute audio directly from the keyboard.

### **Layouts** 🖼️
- **Columns**: A flexible tiling layout with customizable borders and margins.
- **Max**: Maximizes the focused window, ideal for full-screen applications.
- **Matrix**: A grid-based layout for organizing windows in a structured manner.

### **Widgets** 📊
- **System Monitoring**: Real-time monitoring of CPU, memory, and network usage.
- **Clock**: Displays the current date and time.
- **System Tray**: Provides quick access to system icons like volume and network.

### **Autostart** 🚀
- **Essential Services**: Automatically starts Picom, Nitrogen, and other utilities to enhance the desktop experience.
- **Drive Mounting**: Automatically mounts a specific drive on startup.

## Credits 🙏

This configuration is my personal setup, built on the foundation of the Qtile project. Special thanks to the Qtile community for their continuous development and support.

**Note**: This configuration is not officially affiliated with the Qtile project. It is a personal setup designed to enhance my workflow and desktop experience.

Enjoy exploring my Qtile configuration! 🎉
