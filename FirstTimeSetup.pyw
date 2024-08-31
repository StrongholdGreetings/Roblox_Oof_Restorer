import shutil,os,time,sys,platform,tkinter,tkinter.ttk,tkinter.messagebox,requests,json,datetime,time
appdir=os.getcwd()
DataInFirstTime=['This file determines if the program has been run for the first time or not. Do not modifiy, move or delete this file or the program will rerun setup (which requires Internet).\n','IsFirstTime=False']

if not os.path.isdir(appdir+'/Data'):
	os.makedirs(appdir+"/Data")
if not os.path.isdir(appdir+'/Data/TXT'):
	os.makedirs(appdir+"/Data/TXT")
if not os.path.isdir(appdir+'/Data/Media'):
	os.makedirs(appdir+"/Data/Media")
	
def Run():
	global bar
	def on_closing():
		if tkinter.messagebox.askyesno("Roblox OOF Restorer!",'Are you sure you want to quit Setup? You will have to redownload every file manually!'):
			try:
				with open('Data/TXT/IsFirstTime.txt','w') as f:
					for lines in DataInFirstTime:
						f.writelines(lines)
				progress.destroy()
				tkinter.messagebox.showinfo("Setup","Setup closed! Please download your file manually or reopen Setup again in Settings!")
			except Exception:
				progress.destroy()
	#Progress Bar
	progress=tkinter.Tk()
	progress.title("Roblox OOF Restorer - Setup")
	progress.aspect(1,1,1,1)
	progress.configure(bg='gray90')
	progress.geometry("350x350")
	#Title
	label=tkinter.Label(progress)
	label.configure(text="Welcome to Instant Setup.",font=('Arial',15,'bold'),bg='gray90')
	label.place(relx=0.5,rely=0.05,anchor=tkinter.CENTER)
	label1=tkinter.Label(progress)
	label1.configure(text="Download things you need with just a click!",font=('Times New Roman',9,'bold'),bg='gray90')
	label1.place(relx=0.5,rely=0.12,anchor=tkinter.CENTER)
	dash=tkinter.Label(progress)
	dash.configure(text=">------------------------------------------------------<",font=('Times New Roman',9),bg='gray90')
	dash.place(relx=0.5,rely=0.18,anchor=tkinter.CENTER)
	label2=tkinter.Label(progress)
	label2.configure(text="Press Download to download necessary files!",font=('Times New Roman',9),bg='gray90')
	label2.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)
	label3=tkinter.Label(progress)
	label3.configure(text="Press Skip to skip the setup!",font=('Times New Roman',9),bg='gray90')
	label3.place(relx=0.5,rely=0.31,anchor=tkinter.CENTER)
	label4=tkinter.Label(progress)
	label4.configure(text="Don't trust me? Press Info for my source code",font=('Times New Roman',9),bg='gray90')
	label4.place(relx=0.5,rely=0.37,anchor=tkinter.CENTER)
	label5=tkinter.Label(progress)
	label5.configure(text="This program is open source. I do not collect any of your user data!",font=('Times New Roman',9),bg='gray90')
	label5.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)

	bar=tkinter.ttk.Progressbar(progress, orient=tkinter.HORIZONTAL, length=280,mode='determinate')

	def CancelAction():
		rep=tkinter.messagebox.askyesno('Instant Setup','Do you really want to skip the setup? You will have to manually download files in Settings!')
		if rep:
			with open('Data/TXT/IsFirstTime.txt','w') as f:
				for lines in DataInFirstTime:
					f.writelines(lines)
			progress.destroy()
	def MoreInfo():
		os.system('start "" "https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/blob/main/Roblox_Oof_Restorer.py"')
	def Begin():
		if tkinter.messagebox.askyesno("Instant Setup","Do you want to continue?"):
			try:
				if not os.path.isdir(appdir+'/Data'):
					os.makedirs(appdir+"/Data")
				response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/icon.ico")
				with open('Data/Media/icon.ico',"wb") as a:
					a.write(response.content)
				bar['value']+=70
				progress.update_idletasks()
				response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch.ogg")
				with open('Data/Media/ouch.ogg',"wb") as a:
					a.write(response.content)
				bar['value']+=70
				progress.update_idletasks()
				response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch%20(NEW).ogg")
				with open('Data/Media/NewOuch.ogg','wb') as f:
					f.write(response.content)
				bar['value']+=70
				progress.update_idletasks()
				with open('Data/TXT/IsFirstTime.txt','w') as f:
					for lines in DataInFirstTime:
						f.writelines(lines)
				bar['value']+=70
				progress.update_idletasks()
				if bar['value']==280:
					tkinter.messagebox.showinfo("Instant Setup","Setup completed! You can now use the app normally!")
				progress.destroy()
			except requests.exceptions.RequestException:
				tkinter.messagebox.showerror('Instant Setup', "An internet connection is required to download all necessary elements for the app to run. Please connect to the Internet and try again!")
	bar.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
	tkinter.Button(progress,text='Download',width=9,height=1,command=Begin).pack(anchor=tkinter.SE,side=tkinter.RIGHT)
	tkinter.Button(progress,text='Skip',width=7,height=1,command=CancelAction).pack(anchor=tkinter.SE,side=tkinter.RIGHT)
	tkinter.Button(progress,text='Info',width=6,height=1,command=MoreInfo).pack(anchor=tkinter.SE,side=tkinter.RIGHT)
	progress.protocol("WM_DELETE_WINDOW", on_closing)
	progress.mainloop()
if __name__=="__main__":
	Run()