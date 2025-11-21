# 🔗 Hotkey Shortcut Launcher

This project allows you to **bind custom keyboard shortcuts** to launch applications or open websites. It uses a simple JSON configuration file to define hotkeys and their associated commands/paths.

---

## 📌 Features
- Bind any keyboard shortcut to:
  - Launch local applications
  - Open websites in your default browser
- Configuration stored in a JSON file (`shortcuts.json`)
- Lightweight and easy to customize

---

## 📂 Project Structure
```
.
├── shortcuts.json   # Configuration file with hotkeys and paths
├── launcher.py      # Main script
```

---

## ⚙️ Requirements
- Python 3.x
- Required libraries:
  ```bash
  pip install keyboard
  ```

---

## 🛠️ Usage

### 1. Clone or download the repository
```bash
git clone https://github.com/your-username/hotkey-launcher.git
cd hotkey-launcher
```

### 2. Create/Edit `shortcuts.json`
Define your shortcuts in the following format:
```json
{
  "shortcuts": [
    {
      "hotkey": "ctrl+alt+c",
      "path": "calc.exe"
    },
    {
      "hotkey": "ctrl+alt+w",
      "path": "https://www.google.com"
    }
  ]
}
```

- `hotkey`: The keyboard combination (e.g., `ctrl+alt+c`)
- `path`: Either:
  - Application name/path (e.g., `calc.exe`, `/usr/bin/firefox`)
  - Website URL (e.g., `https://www.google.com`)

### 3. Run the script
```bash
python launcher.py
```

The script will:
- Load all shortcuts from `shortcuts.json`
- Bind them to your keyboard
- Wait for you to press the hotkeys

---

## 🚀 Example
- Press `Ctrl + Alt + C` → Opens Calculator  
- Press `Ctrl + Alt + W` → Opens Google in your browser  

---

## ⚠️ Notes
- Running this script may require **administrator/root privileges** depending on your OS.
- The `keyboard` library may not work in all environments (e.g., some Linux desktops without root).
- Be careful when binding global hotkeys to avoid conflicts with system shortcuts.

---

## 📜 License
This project is open-source. Feel free to modify and use it in your own workflows.

---
