import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "C:\Users\win10_1511\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\Users\win10_1511\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\tcl\tcl8.6"

base = None
include_files = [
    "./assets",
    "C:\Users\win10_1511\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\DLLs\tcl86t.dll",
    "C:\Users\win10_1511\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\DLLs\tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="KrypApp",
    version="1.4",
    description="File Encryption App",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "KrypApp.py",
            base=base,
            targetName="KrypApp.exe",
            icon="./assets/icon.ico"
        )
    ]
)
