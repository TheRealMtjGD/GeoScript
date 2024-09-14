import os
import tkinter
import pygit2
import shutil
import admin
import webbrowser

class GSInstaller:
    def install_message(self) -> None:
        window = tkinter.Tk()
        window.title('Installed GeoScript')
        window.geometry('200x100')
        
        tkinter.Label(window, text='Sucsessfuly installed GeoScript').place(anchor='center', relx=0.5, rely=0.5)
        
        window.mainloop()
    
    def install_geoscript(self) -> None:
        os.mkdir(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript')
        os.mkdir(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN')
        
        pygit2.clone_repository('https://github.com/TheRealMtjGD/GeoScript.git', f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN')
        shutil.copytree(f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript/GeoScriptMAIN/interface', f'C:/Users/{os.getlogin()}/AppData/Local/Programs/GeoScript', dirs_exist_ok=True)
        self.install_message()
        exit(0)
    
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('GeoScript Installer')
        self.window.geometry('300x400')
        
        self.draw()
        
        self.window.mainloop()
    
    def draw(self):
        tkinter.Label(self.window, text='GeoScript Installer', font=1).place(anchor='center', relx=0.5, rely=0.1)
        tkinter.Label(self.window, text='GeoScript copywrite (c) MIT License').place(anchor='center', relx=0.5, rely=0.15)
        
        tkinter.Label(self.window, text='Downloading version 1.0.0').place(anchor='center', relx=0.5, rely=0.3)
        tkinter.Label(self.window, text='https://github.com/TheRealMtjGD/GeoScript.git').place(anchor='center', relx=0.5, rely=0.35)
        
        tkinter.Label(self.window, text='By installing you agree to the License and Security').place(anchor='center', relx=0.5, rely=0.5)
        tkinter.Button(self.window, text='Install', font=1, width=10, height=1, command=self.install_geoscript).place(anchor='center', relx=0.5, rely=0.6)
        
        tkinter.Button(self.window, text='License', command=lambda: webbrowser.open('https://github.com/TheRealMtjGD/GeoScript/blob/main/license.md')).place(anchor='center', relx=0.2, rely=0.9)
        tkinter.Button(self.window, text='Changelog', command=lambda: webbrowser.open('https://github.com/TheRealMtjGD/GeoScript/blob/main/changelog.md')).place(anchor='center', relx=0.5, rely=0.9)
        tkinter.Button(self.window, text='Security', command=lambda: webbrowser.open('https://github.com/TheRealMtjGD/GeoScript/blob/main/security.md')).place(anchor='center', relx=0.8, rely=0.9)

if __name__ == '__main__':
    if admin.isUserAdmin() == False:
        admin.runAsAdmin()
        GSInstaller()