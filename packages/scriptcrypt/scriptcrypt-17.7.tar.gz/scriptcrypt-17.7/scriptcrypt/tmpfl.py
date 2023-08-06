from tempfile import mkdtemp
from shutil import rmtree
from subprocess import run


class External(object):
    def __init__(self, extention=".sh"):
        self.extention = extention

    def __enter__(self, file=None):
        self.tempdir = mkdtemp()
        if not file:
            file = self.tempdir + "/script" + self.extention
        self.file = open(file, 'a+')

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        rmtree(self.tempdir)

    def loadText(self, text):
        self.file.seek(0)
        self.file.truncate()
        self.file.write(text)
        self.file.flush()

    def pager(self, pager):
        run([pager, self.file.name])

    def editor(self, editor):
        run([editor, self.file.name])
        self.file.seek(0)
        return self.file.read()

    def script(self, shell):
        ans = run([shell, self.file.name])
        return ans.returncode
