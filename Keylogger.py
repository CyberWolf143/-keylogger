import keyboard
import os
from datetime import datetime

# Function to find the correct Desktop path (handles OneDrive)
def get_desktop_path():
    user_home = os.path.expanduser("~")
    # Check for OneDrive Desktop first (as seen in your screenshot)
    onedrive_path = os.path.join(user_home, "OneDrive", "Desktop")
    
    if os.path.exists(onedrive_path):
        return onedrive_path
    else:
        # Fallback to standard Desktop
        return os.path.join(user_home, "Desktop")

# Setup File Path
desktop_path = get_desktop_path()
log_file = os.path.join(desktop_path, "typing_log.txt")

print("📝 Typing Logger Started!")
print(f"💾 Saving to: {log_file}")
print("⏹️  Press F12 to stop")

# Initialize the log file with a header
try:
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(f"Typing Log Session - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n\n")
except Exception as e:
    print(f"❌ Error creating file: {e}")
    exit()

# Callback function when a key is pressed
def on_key(event):
    if event.event_type == 'down':
        # Open file in append mode ('a') to save the key
        with open(log_file, "a", encoding="utf-8") as f:
            if event.name == 'space':
                f.write(" ")
            elif event.name == 'enter':
                f.write("\n")
            elif event.name == 'backspace':
                f.write("[BACKSPACE]")
            elif len(event.name) == 1:  # Capture letters, numbers, symbols
                f.write(event.name)
        
        # Live feedback in terminal
        print(f"Typed: {event.name}", end="\r")

# Start listening to keyboard events
keyboard.hook(on_key)

print("\n✅ Recording... Everything is being saved!")

# Keep the script running until F12 is pressed
keyboard.wait('f12')

print("\n🛑 Recording stopped!")
print(f"📁 Log saved to: {log_file}")
