from cx_Freeze import setup, Executable

base = None    

executables = [Executable("recycle.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "RCT",
    options = options,
    version = "1.0.0",
    description = 'learn to recycle!',
    executables = executables
)