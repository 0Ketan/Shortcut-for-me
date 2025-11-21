import keyboard
import subprocess
import json
import webbrowser

CONFIG_PATH = "shortcuts.json"

def launch_application(command):
    try:
        if command.startswith(("http://", "https://")):
            webbrowser.open(command)
        else:
            subprocess.Popen(command, shell=True)
    except Exception as e:
        print(f"Failed to launch application: {e}")
def bind_hotkeys(hotkey, command):
    keyboard.add_hotkey(hotkey, lambda: launch_application(command))

with open(CONFIG_PATH, "r") as f:
    shortcuts = json.load(f)["shortcuts"]

for item in shortcuts:
    bind_hotkeys(item["hotkey"], item["path"])

keyboard.wait()
