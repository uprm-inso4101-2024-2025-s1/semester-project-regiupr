from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "packages": ["tkinter", "os"],
    "include_files": [("resources/CatalogoCursos.csv", "CatalogoCursos.csv")]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CourseEnrollment",
    version="0.1",
    description="A simple course enrollment search tool",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
