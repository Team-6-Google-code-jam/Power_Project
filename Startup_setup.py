import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup(file_path="",file=__file__):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(file))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(f'python "" "{file_path}\{file}"')

if __name__ == "__main__":
    add_to_startup(file='power_predictor.py')