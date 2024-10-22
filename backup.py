import shutil

def backupSavefile(loc: str) -> None:
    shutil.copyfile(loc, 'Temp/backup.dat')

def exportSavefile(loc: str) -> None:
    shutil.copyfile('Temp/savefile.dat', f'{loc}/CCLocalLevels.dat')