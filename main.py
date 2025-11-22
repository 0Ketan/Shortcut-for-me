import keyboard
import subprocess
import json
import webbrowser

import subprocess

def notify(title, message):
    script = f"""
    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
    $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
    $toastText = $template.GetElementsByTagName("text")
    $toastText.Item(0).AppendChild($template.CreateTextNode("{title}")) > $null
    $toastText.Item(1).AppendChild($template.CreateTextNode("{message}")) > $null
    $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
    $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("ShortcutForMe")
    $notifier.Show($toast)
    """

    subprocess.Popen(["powershell", "-Command", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

CONFIG_PATH = "C:\\Users\\LENOVO\\OneDrive\\Desktop\\My Projects\\Shortcut-for-me\\shortcuts.json"

current_mode = "apps"  # apps OR websites

# ---------- Run Functions ---------- #

def run_app(command):
    subprocess.Popen(command, shell=True)

def run_web(command):
    webbrowser.open(command)

# ---------- Load JSON ---------- #

with open(CONFIG_PATH, "r") as f:
    data = json.load(f)

apps = {item["hotkey"]: item["path"] for item in data["apps"]}
websites = {item["hotkey"]: item["path"] for item in data["websites"]}

all_hotkeys = set(apps.keys()) | set(websites.keys())

# ---------- Handler for all hotkeys ---------- #

def run_action(hotkey):
    global current_mode

    if current_mode == "apps" and hotkey in apps:
        run_app(apps[hotkey])

    elif current_mode == "websites" and hotkey in websites:
        run_web(websites[hotkey])

    else:
        print(f"No command in {current_mode} mode for {hotkey}")

# ---------- Bind All Hotkeys Once ---------- #

for hotkey in all_hotkeys:
    keyboard.add_hotkey(hotkey, lambda h=hotkey: run_action(h))

# ---------- Mode Switch Hotkey ---------- #

def mode_switch():
    global current_mode

    if current_mode == "apps":
        current_mode = "websites"
        notify("Mode Changed", "Switched to WEBSITE Mode")
        print("Switched to WEBSITE Mode")

    else:
        current_mode = "apps"
        notify("Mode Changed", "Switched to APPS Mode")
        print("Switched to APPS Mode")


keyboard.add_hotkey("ctrl+alt+space", mode_switch)

# ---------- Wait Forever ---------- #

keyboard.wait()
