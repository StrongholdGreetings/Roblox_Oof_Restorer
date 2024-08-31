#Import required library
LaunchBySettings=False
import shutil,os,time,sys,platform,tkinter,tkinter.messagebox,requests,json,datetime,time
import FirstTimeSetup,AppFunction,Preference
defaultcolor={"Text":"Black","Button":"White","Theme":"Light"}
defaultupdate={"NoAskUpdate":"Off","CheckWhenStarts":"On","CheckRobloxWhenStarts": "Off"}
DataInFirstTime=['This file determines if the program has been run for the first time or not. Do not modifiy, move or delete this file or the program will rerun setup (which requires Internet).\n','IsFirstTime=False']
debugmode=True

appdir=os.getcwd()

try:
	with open("Data/TXT/IsFirstTime.txt","r") as f:
		IsFirst=list(f.readlines())
	if IsFirst!=DataInFirstTime:
		FirstTimeSetup.Run()
except FileNotFoundError:
	FirstTimeSetup.Run()
	
version='v1.3'
oggfile=f'{appdir}/Data/Media/ouch.ogg'
icofile=f'{appdir}/Data/Media/icon.ico'
colordatafile=f'{appdir}/Data/ColorData.json'

try:
	with open('Data/TXT/DownloadLog.txt','r') as f:
		currenttime=f.read()
except FileNotFoundError:
	currenttime='Never'


if platform.system()=='Windows':
	widthcheckbutton=7
	widthbutton=9
else:
	widthcheckbutton=5
	widthbutton=7

xleft=0.09

savedmode='Light'

AppFunction.FileTest(0)
AppFunction.FileTest(1)
def RunMainFunc():
	AppFunction.mainfunc(0)

def main():
	global window
	def gui(): 
		global window,label4
		window=tkinter.Tk()

		try:
			with open("Data/ColorData.json",'r') as f:
				colordata=json.load(f)
		except FileNotFoundError:
			AppFunction.FileRestore(0)
			with open("Data/ColorData.json",'r') as f:
				colordata=json.load(f)
		try:
			with open('Data/TXT/UpdateAvailable.temp','r') as f:
				updatebool=f.read()
		except FileNotFoundError:
			updatebool='False'
		with open('Data/TXT/UpdateAvailable.temp','w') as f:
			updatebool=f.write(updatebool)
		ThemeData=AppFunction.ApplySettings()
		if AppFunction.OSRecognition()=='Android':
			window.geometry('350x420')
		else:
			window.geometry('350x400')
		window.configure(bg=ThemeData["bgcolor"])
		

		#Title on window
		label=tkinter.Label(window)
		label.configure(text="Roblox OOF Restorer!",font=('Arial',15,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		label.pack()

	#Define function for buttons
		def RestartApp():
			window.destroy()
			gui()
		
		#Credit
		label1=tkinter.Label(window)
		label1.configure(text="Made by StrongholdGreetings",fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		label1.pack()

		#Version number
		label3=tkinter.Label(window)
		label3.configure(text="Version 1.3",font=('Arial',8),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		label3.pack()

		label4=tkinter.Label(window)
		label4.configure(text="No Icon Mode! Restore icon in Settings!",font=('Arial',8),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		
		label5=tkinter.Label(window)
		label5.configure(text="A new update is available!",font=('Arial',7),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		if updatebool=='True':
			label5.pack()

		#Button to restore OOF
		button=tkinter.Button(
			window, text="Restore OOF!",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=RunMainFunc
		)
		button1=tkinter.Button(
			window, text="About UWP support...",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=AppFunction.NoUWP
		)

		button2=tkinter.Button(
			window, text="Settings",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=Preference.run
		)

		#Button to quit app
		button3=tkinter.Button(
			window, text="Restart App",
			font=('Arial',9,'bold'),
			width=14,
			height=2,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=RestartApp
		)

		button4=tkinter.Button(
			window, text="Quit",
			font=('Arial',9,'bold'),
			width=14,
			height=2,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=AppFunction.ExitApp
		)

		#Button placement
		button.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)
		button1.place(relx=0.5,rely=0.47,anchor=tkinter.CENTER)
		button2.place(relx=0.5,rely=0.64,anchor=tkinter.CENTER)
		button3.place(relx=0.18,rely=0.81,anchor=tkinter.W)
		button4.place(relx=0.81,rely=0.81,anchor=tkinter.E)

		#Window title
		window.title("Roblox OOF Restorer!")

		#Show icon on Title bar
		try:
			window.iconbitmap(icofile)
		except tkinter.TclError:
			if platform.system()=='Windows':
				label4.place(relx=0.5,rely=1,anchor=tkinter.S)

		window.protocol("WM_DELETE_WINDOW", AppFunction.ExitApp)

	#Keep window running
		window.mainloop()
		
	#---------------------------------------------------------------------------------------------------------------------------------------------------
	
	#Main software


	#Display Window
	gui()

try:
	AppFunction.UpdateOnStart()
	AppFunction.CheckRobloxUpdates()
	main()
except tkinter.TclError:
	window.destroy()
	rep=tkinter.messagebox.showerror("Error Occured!","Seems like there is an illegal value in the JSON file. Do you want to restore all value to default?",type='yesno')
	if rep=='yes':
		try:
			colordata={"Text":"Black","Button":"White","Theme":"Light"}
			with open("Data/ColorData.json",'w') as f:
				json.dump(colordata,f,indent=4)
			tkinter.messagebox.showinfo('Roblox OOF Restorer','Your file is successfully restored!')
			main()
		except Exception:
			tkinter.messagebox.showerror("Error Occured!","Whoops! An unknown error occured and the file cannot be fixed.")
except requests.exceptions.RequestException:
	main()	