import scriptcrypt.jsonhandlers as s
import scriptcrypt.populate
from os import devnull
import os.path
import subprocess


def checkdir(dir):
    return True if os.path.isdir(dir) else False


def checkfile(path):
    return True if checkdir(os.path.dirname(path)) else False


def checkexec(exe):
    with open(devnull, 'w') as FNULL:
        ans = subprocess.run(["which", exe], stdout=FNULL)
    return True if ans.returncode == 0 else False


def checkall(argdict):
    Settings = s.Settigns()
    settings = Settings.getData()
    if argdict["--db"] is not None and checkfile(argdict["--db"]):
        settings["db"] = os.path.abspath(argdict["--db"])
    if argdict["--editor"] is not None and checkexec(argdict["--editor"]):
        settings["editor"] = argdict["--editor"]
    if argdict["--viewer"] is not None and checkexec(argdict["--viewer"]):
        settings["viewer"] = argdict["--viewer"]
    if argdict["--shell"] is not None and checkexec(argdict["--shell"]):
        settings["shell"] = argdict["--shell"]
    Settings.writeData(settings)
    if argdict["--populate-all"]:
        scriptcrypt.populate.copyDB(settings["db"])
        scriptcrypt.populate.copyBash()
        scriptcrypt.populate.copyZsh()
    else:
        if argdict["--populate-db"]:
            scriptcrypt.populate.copyDB(settings["db"])
        if argdict["--populate-bash"]:
            scriptcrypt.populate.copyBash()
        if argdict["--populate-zsh"]:
            scriptcrypt.populate.copyZsh()
    return settings
