#!/bin/bash

# Update system and install packages
echo "Updating system and installing packages..."
sudo pacman -Syu --noconfirm
sudo pacman -S --noconfirm thunar thunar-archive-plugin thunar-volman udisks2 gvfs dunst gedit gedit-plugins

# Enable necessary services for current session
echo "Enabling DBus service..."
systemctl --user enable --now dunst

# Check for Qtile autostart and provide instructions if not found
echo "Configuring autostart for Qtile..."
QTILE_AUTOSTART="$HOME/.config/qtile/autostart.sh"

if [ ! -f "$QTILE_AUTOSTART" ]; then
    echo "Qtile autostart.sh not found. Creating a sample one..."
    cat > "$QTILE_AUTOSTART" << 'EOF'
#!/bin/bash
# Start Dunst notification daemon
dunst &

# Start other applications if needed
# thunar --daemon &
EOF
    chmod +x "$QTILE_AUTOSTART"
    echo "Sample autostart.sh created at $QTILE_AUTOSTART"
else
    echo "Qtile autostart.sh found. Please ensure it includes 'dunst &'."
fi

# Provide post-installation notes
echo ""
echo "✅ Installation complete!"
echo ""
echo "📋 Manual Configuration Notes:"
echo "   - For Thunar USB auto-mount: Ensure no USB devices are defined in /etc/fstab"
echo "   - Thunar archive support: The 'Create Archive...' and 'Extract Here' options will appear in the right-click menu"
echo "   - Dunst configuration: Copy the default config if desired:"
echo "     cp /etc/dunst/dunstrc ~/.config/dunst/dunstrc"
echo "   - Restart your Qtile session or run the autostart script for changes to take effect."
