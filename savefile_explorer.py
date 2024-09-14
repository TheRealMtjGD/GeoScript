from components import decoder
from components import savefile_module
import shutil

shutil.copyfile('C:/Users/danre/AppData/Local/GeometryDash/CCLocalLevels.dat', 'temp/backupfile.dat')
decoder.DecryptCCLL('temp/backupfile.dat')

print(savefile_module.getLevelInfomation('GeoScript test'))