###########################################################################################
## ARQUIVO PARA GERAR UM EXECUTÁVEL WIN UTILIZANDO CX_FREEZE
import sys
from cx_Freeze import setup, Executable
######################

##### Caso deseje que não apareça o console / Comente a linha se quiser aquele cmd no fundo
base = None
if sys.platform == "win32":
    base = "Win32GUI"
############################################################################################
executables = [
        Executable("main.py", base=base) ## nome do arquivo principal / base=none se quiser que o cmd apareça
]

buildOptions = dict(
        packages = [], ## pacotes tipo TKinter etc...
        includes = ["pygame"],
        include_files = ['data/icone.png','data/do5.wav',
                         'data/re5.wav',
                         'data/mi5.wav',
                         'data/fa5.wav',
                         'data/sol5.wav',
                         'data/la5.wav',
                         'data/si5.wav',
                         'data/do6.wav',
                         'data/re6.wav',
                         'data/mi6.wav',
                         'data/fa6.wav'],
        excludes = []
)

setup(
    name = "XILOFONE_MAESTRO",
    version = "1.0",
    description = "Jogo desenvolvido por RobsonMaestro como suporte as aulas de música do Colégio SESC - Unidade Araxá",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
