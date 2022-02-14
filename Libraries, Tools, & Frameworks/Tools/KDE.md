# Basics
* ALT + F1 is a global keyboard shortcut for the Super/Meta/Windows key.
* Lock Screen is different from the Login Screen
* Remove 'Default' widget
 1. Right click -> Configure Desktop -> Tweaks
 2. Uncheck 'Show the desktop toolbox'

# Global Themes

Sometimes they persist when you uninstall them. To remove them from
the global themes menu, delete them from `~/.local/share/plasma/look-and-feel`

# Widgets

## Active Window Control
* Control Window Titlebar


# Packages

## Latte Dock (install)
* Dock for KDE

### Getting the Global ALT + F1 to work with Latte Dock

#### Option 1
1. Add this to `~/.config/kwinrc`
```
[ModifierOnlyShortcuts]
Meta=org.kde.lattedock,/Latte,org.kde.LatteDock,activateLauncherMenu
```
2. Reload KWin with `qdbus org.kde.KWin /KWin reconfigure`

#### Option 2
1. Run
```
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.lattedock,/Latte,org.kde.LatteDock,activateLauncherMenu"
qdbus org.kde.KWin /KWin reconfigure

```

## ms-office-online (remove)
* Microsoft Office Online shortcuts

## libre-office-fresh (install)
* LibreOffice Suite
