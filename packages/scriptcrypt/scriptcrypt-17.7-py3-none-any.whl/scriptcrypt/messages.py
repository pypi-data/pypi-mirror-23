footerMenu = """ADD:n|SELECT:s|DESELECT:d|INFO:SPACE|\
INSTALL:i|UNINSTALL:u|REMOVE:0|EXIT:q"""
footerEdit = """EDIT:SPACE|SAVE:s|VIEW:v|EXIT:q"""
scriptMessage = """# Preset variable $TMPDIR (temporary directory) is available
# Use --manage-envars option add additional variable"""
populateMessage = """database is empty
to populate database with default entries
use --populate-db option"""
removeEntries = """Remove entries?(y/n)"""
returnCode = """Following scripts have \
returned with non-zero exit code"""
emptySel = """Selection is empty. Please, select some entries first"""
runIns = """Running install script for """
runUnIns = """Running uninstall script for """


class bcolors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
