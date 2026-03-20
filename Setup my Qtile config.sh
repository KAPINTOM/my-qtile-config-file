#!/usr/bin/env bash
#
# Automated setup script for Qtile (Arch Linux)
# Fetches configs from https://github.com/KAPINTOM/my-qtile-config-file
# and installs all dependencies.

set -e  # Exit on any error

# ---- Helper functions ----
error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
    exit 1
}

info() {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

success() {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

# Check if we are on Arch Linux
if ! grep -qi "arch" /etc/os-release; then
    error "This script is intended for Arch Linux only."
fi

# Check for sudo privileges
if ! sudo -v; then
    error "You need sudo privileges to install packages."
fi

# ---- Package installation ----
info "Updating system packages..."
sudo pacman -Syu --noconfirm || error "Failed to update packages"

info "Installing required packages..."
PACKAGES=(
    qtile                # Window manager
    kitty                # Terminal
    rofi                 # Application launcher
    brightnessctl        # Brightness control
    alsa-utils           # amixer for volume control
    playerctl            # Media player control
    picom                # Compositor
    nitrogen             # Wallpaper setter
    network-manager-applet # NetworkManager tray icon
    dunst                # Notification daemon
    maim                 # Screenshot utility
    xorg-server          # X server
    xorg-xinit           # startx
    xorg-xrandr          # Screen resolution control
    xorg-xsetroot        # Root window properties
    git                  # To clone the repository
    ttf-dejavu           # Fallback font (optional)
)

sudo pacman -S --needed --noconfirm "${PACKAGES[@]}" || error "Failed to install packages"

# ---- Optional font (Cascadia Code) ----
# The config uses "Cascadia Code". Install it from AUR if you have an AUR helper.
if command -v yay &> /dev/null; then
    info "Installing Cascadia Code font via yay..."
    yay -S --needed --noconfirm ttf-cascadia-code || info "Cascadia Code installation skipped"
else
    info "Cascadia Code font not installed (no AUR helper). You can install it manually if desired."
fi

# ---- Fetch configuration files ----
TEMP_DIR=$(mktemp -d)
info "Cloning configuration repository into $TEMP_DIR..."
git clone --depth 1 https://github.com/KAPINTOM/my-qtile-config-file.git "$TEMP_DIR" || error "Failed to clone repository"

# Create config directories if they don't exist
mkdir -p ~/.config

# Copy Qtile config
if [[ -d "$TEMP_DIR/qtile" ]]; then
    info "Copying Qtile configuration..."
    cp -r "$TEMP_DIR/qtile" ~/.config/
    # Ensure scripts are executable
    chmod -R +x ~/.config/qtile/scripts/*.sh 2>/dev/null || true
else
    error "Qtile folder not found in repository"
fi

# Copy Picom config
if [[ -d "$TEMP_DIR/picom" ]]; then
    info "Copying Picom configuration..."
    cp -r "$TEMP_DIR/picom" ~/.config/
else
    info "Picom folder not found, skipping..."
fi

# ---- Create Qtile desktop entry (for display managers) ----
info "Creating Qtile desktop entry..."
sudo tee /usr/share/xsessions/qtile.desktop > /dev/null << EOF
[Desktop Entry]
Name=Qtile
Comment=Qtile Window Manager
Exec=qtile start
Type=Application
EOF

# ---- Cleanup ----
rm -rf "$TEMP_DIR"
success "Setup completed successfully!"
info "You can now log out and select 'Qtile' from your display manager, or run 'startx' after configuring ~/.xinitrc."