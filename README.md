---

# 📘 Shortcut-For-Me

A lightweight global-hotkey launcher with **dual modes** (Apps / Websites), plus **native Windows 11 toast notifications**.
Built with Python and works perfectly with **Python 3.14**.

---

## 🚀 Features

### ✅ Dual-Mode System

Easily toggle between two modes:

* **App Mode** → Hotkeys launch installed applications
* **Website Mode** → Same hotkeys open websites
* Mode is switched instantly using
  **`CTRL + ALT + SPACE`**

### 🔥 Single Hotkey for Multiple Actions

The **same hotkey** can launch:

* Chrome.exe (App mode)
* youtube.com (Website mode)

Depending on which mode is active.

### 🔔 Windows 11 Notifications

Uses native **PowerShell-based toast notifications**, fully compatible with Python 3.14 (win10toast/winotify don’t work).

You receive a popup when:

* Mode switches to **APPS**
* Mode switches to **WEBSITES**

### ⚡ Fast & Optimized for Startup

* Lightweight
* Runs silently in background
* One-time hotkey binding
* Reads a simple JSON shortcut list

---

## 📁 Project Structure

```
Shortcut-for-me/
│
├── main.py               # Main Python script
├── shortcuts.json        # App & website shortcuts
└── README.md             # This file
```

---

## 🛠 Requirements

### Windows:

* Windows 10 or 11
* PowerShell enabled (default)

### Python:

* Python **3.14**
* Required packages:

  * `keyboard`

Install:

```
pip install keyboard
```

---

## 📄 JSON Format (shortcuts.json)

Your JSON must contain two lists:

```json
{
  "apps": [
    {
      "hotkey": "ctrl+alt+c",
      "path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
      "desc": "Chrome"
    }
  ],

  "websites": [
    {
      "hotkey": "ctrl+alt+c",
      "path": "https://www.youtube.com",
      "desc": "YouTube"
    }
  ]
}
```

Hotkeys **can be the same** for apps and websites.

---

## ⚙ How the Program Works

### 1️⃣ Load Shortcuts

All app & website shortcuts are loaded from `shortcuts.json`.

### 2️⃣ Bind Hotkeys

Every hotkey is bound **once**.

When triggered, it calls:

```py
run_action(hotkey)
```

### 3️⃣ Mode Switching

Press:

```
CTRL + ALT + SPACE
```

to toggle between:

```
apps  <→>  websites
```

### 4️⃣ Execute Action

If in app mode → run EXE
If in website mode → open URL

---

## 🔔 Notifications

A small toast shows:

```
Mode Changed
Switched to WEBSITE Mode
```

or

```
Mode Changed
Switched to APPS Mode
```

This uses native PowerShell toast API (works on Python 3.14).

---

## ▶ Running the Script

Simply execute:

```
python main.py
```

To run it **every startup**, place a shortcut to `main.py` in:

```
shell:startup
```

---

## 💡 Future Improvements (optional)

* UI for managing shortcuts (Tkinter)
* Import/export profiles
* Add sound notifications
* Auto-reload JSON without restarting app
* Tray icon with menu

---