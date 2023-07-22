import speedtest
import time
from colorama import init, Fore
from colorama import Back
from colorama import Style
from prettytable import PrettyTable

print(Fore.BLACK + Back.LIGHTGREEN_EX + '''
░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░░
░░░░░░░░░░░▄▄████████████▄▄░░░░░░░░░░░
░░░░░░░░░▄██████████████████▄░░░░░░░░░
░░▄███████████████████▀▀▀▀▀▀▀▀▀▀▀▀█▄░░
░████████████████████░░░░░░░░░░░░░░▀█░
████░░██░░██░░█░░███░░░░███▀▀▀░░██░░▀█
████▄░▀░░░▀░░██░░███░░░░███▄▄▄░░██░░░█
█████░░░▄░░░░██░░███░░░░███▀▀▀░░██░░░█
█████▄░░██░░███░░███░░░░███░░░░░██░░▄█
░██████████████████░░░░░░░░░░░░░░░░▄█░
░░▀▀██████████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀░░
░░░░░░░░░▀██████████████████▀░░░░░░░░░
░░░░░░░░░░░░▀████████████▀░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▀▀▀▀▀▀░░░░░░░░░░░░░░░░

''')
def start():
    word = input('Enter "s" to start >>> ')
    if word.lower() == 's':
        print('Please, wait...')
        start1 = time.time()
        test = speedtest.Speedtest()
        test.get_best_server()
        ping = test.results.ping
        download = test.download()
        upload = test.upload()
        mytable = PrettyTable()
        mytable.field_names = ["DOWNLOAD (Mbit/s)", "UPLOAD (Mbit/s)", "PING (ms)"]
        mytable.add_rows(
            [
                [download / 1000000, upload / 1000000, ping],
            ]
        )
        print(mytable)
        end = time.time()
        print(f'Function execution time {round(end - start1)}s')
        start()
    else:
        start()


start()

