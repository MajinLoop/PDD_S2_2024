import shutil
import os
import platform
from enum import Enum


class OS(Enum):
    WINDOWS  = "Windows"
    UBUNTU   = "Ubuntu"


g_os_name = OS.WINDOWS.value

# Windows default format
g_TEMPLATE_OPTION_0 = '..\\templates\\arch0.txt'
g_TEMPLATE_OPTION_1 = '..\\templates\\arch1.txt'
g_TEMPLATE_STRUCTURE_OPTION_0 = '..\\templates\\structure_example_1.txt'


def recognize_os():
    global g_os_name
    current_os = os.name

    if current_os == 'posix':
        if platform.system() == "Linux" and "ubuntu" in platform.version().lower():
            g_os_name = OS.UBUNTU.value
            covert_template_paths()


def covert_template_paths():
    global g_TEMPLATE_OPTION_0, g_TEMPLATE_OPTION_1, g_TEMPLATE_STRUCTURE_OPTION_0
    if(g_os_name == OS.UBUNTU.value):
        g_TEMPLATE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_OPTION_0)
        g_TEMPLATE_OPTION_1 = windows_to_unix_path(g_TEMPLATE_OPTION_1)
        g_TEMPLATE_STRUCTURE_OPTION_0 = windows_to_unix_path(g_TEMPLATE_STRUCTURE_OPTION_0)


def covert_metadata_path(path):
    if(g_os_name == OS.WINDOWS.value):
        return windows_to_wsl_path(path)


def print_dash_line(char='-'):
    columns, _ = shutil.get_terminal_size()
    print(char * (columns - 1))


def windows_to_unix_path(windows_path):
    return windows_path.replace('\\', '/')


def windows_to_wsl_path(windows_path):
    wsl_path = windows_to_unix_path(windows_path)
    
    if wsl_path[1:3] == ':/' or wsl_path[1:2] == ':':
        drive_letter = wsl_path[0].lower()
        wsl_path = f'/mnt/{drive_letter}{wsl_path[2:]}'    
    return wsl_path