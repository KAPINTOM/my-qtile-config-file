# 🧠 Vertical-First Qtile Configuration

A minimalist, intentional, and productivity-focused Qtile configuration built around a **vertical-first interface philosophy**.

This setup rethinks traditional desktop layouts by **eliminating horizontal bars** and instead using **dual vertical sidebars** to preserve vertical space, reduce clutter, and improve focus.

---

# 📐 Design Philosophy

## Core Principle

> Preserve vertical space for content. Use horizontal space for system UI.

Modern applications—especially browsers, editors, and terminals—are inherently **vertical in structure**. However, most desktop environments waste this valuable vertical space with stacked horizontal bars.

This configuration solves that by:

* Removing top bars entirely
* Moving UI elements to the left and right edges
* Keeping the center area clean and dedicated to content

---

## Layout Model

```
[ CONTROL ] [        CONTENT        ] [ STATUS ]
```

* **Left Bar → Control**

  * Window management
  * Layout indicator
  * Task navigation

* **Center → Content**

  * Fullscreen-focused workspace
  * No visual interference

* **Right Bar → Status**

  * System information (CPU, RAM, battery, time)
  * Quick actions (power, launchers, etc.)

---

## Workflow Modes

### 🟢 Focus Mode (Default)

* Layout: `Max`
* One window at a time
* No distractions
* Ideal for:

  * coding
  * reading
  * browsing
  * gaming

---

### 🔵 Work Mode

* Layout: `Columns`
* Multi-window tiling
* Ideal for:

  * multitasking
  * comparisons
  * development workflows

Switch between modes instantly via keybinding or UI.

---

# ✨ Features

## 🧩 Dual Vertical Bars

* Left and right bars instead of a top bar
* Better use of widescreen displays
* Zero vertical space wasted

---

## 🧠 Intentional Minimalism

* Only essential widgets
* No redundant UI elements
* Clean and consistent layout

---

## 🎯 TaskList as Tab System

* Acts like a tab bar for windows
* Perfect complement to `Max` layout

---

## ⚡ Efficient Keybindings

* Vim-like directional navigation
* Logical grouping:

  * Move → `mod + shift`
  * Resize → `mod + control`
* Media and brightness keys included

---

## 🔄 Layout Switching

* Fast toggle between:

  * Fullscreen (`Max`)
  * Tiling (`Columns`)

---

## 🚀 Autostart Support

* Executes a custom script at startup
* Handles executable and non-executable scripts gracefully

---

## 🎨 Consistent Theming

* Centralized color system
* Semantic color naming
* Easy to customize

---

## 🧱 Structured Configuration

* Cleanly organized sections:

  * Keys
  * Layouts
  * Widgets
  * Screens
  * Mouse
  * Floating rules

---

# 🖥️ Bar Overview

## Left Bar (Control)

* Current layout indicator
* Task list (window navigation)

---

## Right Bar (Status)

* Application launcher (Rofi)
* Window actions (kill, minimize)
* System tray
* CPU usage
* RAM usage
* Battery status
* Vertical clock

---

# 🧰 Dependencies

Make sure you have the following installed:

### Required

* `qtile`
* `python`

### Recommended tools

* `rofi` (app launcher)
* `kitty` (terminal)
* `maim` (screenshots)
* `brightnessctl` (brightness control)
* `amixer` (audio control)
* `playerctl` (media control)

---

# ⌨️ Keybindings (Highlights)

| Action            | Key              |
| ----------------- | ---------------- |
| Launch terminal   | `Mod + Enter`    |
| App launcher      | `Mod + E`        |
| Window switcher   | `Mod + W`        |
| Kill window       | `Mod + Q`        |
| Toggle fullscreen | `Mod + F`        |
| Toggle floating   | `Mod + T`        |
| Next layout       | `Mod + Tab`      |
| Reload config     | `Mod + Ctrl + R` |
| Shutdown Qtile    | `Mod + Ctrl + Q` |

---

# 📸 Screenshots

*(Add screenshots here if desired)*

---

# 🔧 Customization

## Colors

Edit the `colors` dictionary to quickly change the theme.

## Terminal

Change:

```python
terminal = "kitty"
```

## Autostart Script

Located at:

```
~/.config/qtile/scripts/autostart.sh
```

---

# 🧠 Why This Setup?

Traditional desktop environments:

* stack UI elements vertically
* reduce usable content space
* mix system UI with application UI

This configuration:

* separates concerns (control / content / status)
* maximizes usable space
* reduces cognitive load
* creates a stable, predictable interface

---

# 🚀 Future Ideas

* Auto-switch layouts based on window count
* Dynamic sidebar behavior
* Scratchpads (dropdown apps)
* Context-aware widgets

---

# 🏁 Final Thoughts

This is not just a Qtile config—it’s a **different way of thinking about desktop interfaces**.

Instead of adapting to traditional layouts, it redefines how space is used:

> The center is for work. The sides are for everything else.

---

# 👤 Author

Kenneth Andrey Pinto Medina
GitHub: https://github.com/KAPINTOM
