import webbrowser
import time
import pyfiglet
banner = pyfiglet.figlet_format("Ez    Views")
print(banner)
MSG = input("Looks Liks You Need Views Lol Its Ok Press Enter")
Url = input("Input Your Video Url Here: ")
duration = input("Input The Time You Want Your Bot To Watch Video: ")
while True:
    webbrowser.open_new(Url)
    time.sleep(int(duration))