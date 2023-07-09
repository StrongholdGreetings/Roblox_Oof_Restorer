#Import required library
import shutil,os,time,ctypes,sys,platform,tkinter
from tkinter import messagebox,ttk
from tkinter import *
import subprocess
import requests

modechoice='Black'
modeaddchoice='White'

savedmode='Light'
def ApplySettings():
	global data,bgcolor,txtcolor,buttoncolor,modechoice,modeaddchoice
	bgcolor='white'
	with open("Data/Log.txt",'r') as f:
		data=f.readlines()
	modechoice=data[0]
	modeaddchoice=data[1]
	buttoncolor=modeaddchoice.removesuffix("\n")
	txtcolor=modechoice.removesuffix("\n")

appdir=os.getcwd()
oggfile=f'{appdir}/Data/ouch.ogg'
icofile=f'{appdir}/Data/icon.ico'

if not os.path.exists(appdir+'/Data'):
	os.makedirs(appdir+"/Data")

def DownloadICO():
	try:
		response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/icon.ico")
		with open('Data/icon.ico',"wb") as a:
			a.write(response.content)
		messagebox.showinfo('Roblox OOF Restorer!', "Icon has been downloaded successfully! Press Apply in settings or restart this program to apply icon.")    
	except requests.exceptions.RequestException:
		messagebox.showinfo('Roblox OOF Restorer!', "Icon cannot be downloaded! Check your connection to the web.")

def DownloadOOF():
	try:
		response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch.ogg")
		with open('Data/ouch.ogg',"wb") as a:
			a.write(response.content)
		messagebox.showinfo('Roblox OOF Restorer!', "Your old OOF has been downloaded successfully!")    
	except requests.exceptions.RequestException:
		messagebox.showerror('Roblox OOF Restorer!', "Old OOF cannot be downloaded! Check your connection to the web.")


def gui():
	global window,label4
	ApplySettings()
	window=Tk()
	window.geometry('300x350')
	window.configure(bg=bgcolor)

	#Title on window
	label=Label(window)
	label.configure(text="Roblox OOF Restorer!",font=('Arial',15,'bold'),fg=txtcolor,bg=bgcolor)
	label.pack()

	#Credit
	label1=Label(window)
	label1.configure(text="by StrongholdGreetings on GitHub",fg=txtcolor,bg=bgcolor)
	label1.pack()

	#Version number
	label3=Label(window)
	label3.configure(text="Version 1.0.0",font=('Arial',8),fg=txtcolor,bg=bgcolor)
	label3.pack()

	label4=Label(window)
	label4.configure(text="No Icon Mode! Restore icon in Settings!",font=('Arial',8),fg=txtcolor,bg=bgcolor)

	#Button to restore OOF
	button=Button(
		window, text="Restore OOF!",
		width=30,
		height=2,
		bg=buttoncolor,
		fg=txtcolor,
		command=main
	)

	#Button to listen to oof
	button1=Button(
		window, text="Listen to OOF! (Media Player)",
		width=30,
		height=2,
		bg=buttoncolor,
		fg=txtcolor,
		command=PlayOOF
	)

	#Button to show notes
	button2=Button(
		window, text="Notes",
		width=30,
		height=2,
		bg=buttoncolor,
		fg=txtcolor,
		command=NoUWP
	)
	
	#Button to quit app
	button3=Button(
		window, text="Settings",
		width=30,
		height=2,
		bg=buttoncolor,
		fg=txtcolor,
		command=Settings
	)

	button4=Button(
		window, text="Quit",
		width=30,
		height=2,
		bg=buttoncolor,
		fg=txtcolor,
		command=ExitApp
	)

	#Button placement
	button.place(relx=0.5,rely=0.28,anchor=CENTER)
	button1.place(relx=0.5,rely=0.41,anchor=CENTER)
	button2.place(relx=0.5,rely=0.54,anchor=CENTER)
	button3.place(relx=0.5,rely=0.67,anchor=CENTER)
	button4.place(relx=0.5,rely=0.8,anchor=CENTER)

	#Window title
	window.title("Roblox OOF Restorer!")

	#Show icon on Title bar
	try:
		window.iconbitmap(icofile)
	except tkinter.TclError:
		if platform.system()=='Windows':
			label4.place(relx=0.5,rely=1,anchor=S)

	#Lock window size
	window.resizable(False,False)

	#Keep window running
	window.mainloop()

def open_secondary_window():
	global tab1,tab2,modeaddchoice,modechoice,temp1,temp2
	# Create secondary (or popup) window.
	try:
		with open('Data/Log.txt','r') as f:
			savedmode=f.read()
	except FileNotFoundError:
		savedmode="Black"
	#Window for Settings
	secondary_window = tkinter.Toplevel(bg=bgcolor)
	tabcontrol=ttk.Notebook(secondary_window)
	secondary_window.title("Settings")
	secondary_window.geometry('300x300')
	tab1=ttk.Frame(tabcontrol)
	tab2=ttk.Frame(tabcontrol)
	secondary_window.grab_set()
	try:
		secondary_window.iconbitmap(icofile)
	except tkinter.TclError:
		if platform.system()=='Windows':
			inlabel4=Label(tab1)
			inlabel4.configure(text="No Icon Mode! Restore icon here!",font=('Arial',8),fg=txtcolor,bg=buttoncolor)
			inlabel4.place(relx=0.5,rely=0.82,anchor=S)
	secondary_window.configure(bg=bgcolor)
	label=Label(secondary_window)
	label.configure(text="SETTINGS",font=('Arial',15,'bold'),fg=txtcolor,bg=bgcolor)
	label.pack()


	tabcontrol.add(tab1, text='Restore')
	tabcontrol.add(tab2, text='Color')
	tabcontrol.pack(expand=1,fill='both')



	def test():
		global tab1,tab2
		temp1=var.get()
		temp2=var1.get()
		if temp1==temp2:
			messagebox.showerror("Error Occured!","Your button color must not be the same as text color")
		else:
			write=[temp1+"\n",temp2+"\n"]
			with open('Data/Log.txt','w') as f:
				for line in write:
					f.write(line)
			messagebox.showinfo('Roblox OOF Restorer!', "Changes successfully applied! The program will restart to apply changes.")
			secondary_window.destroy()
			window.destroy()
			gui()


	innerbutton3=Button(
		tab1, text="Restore",
		width=9,
		height=1,
		bg=buttoncolor,
		fg=txtcolor,
		command=DownloadICO
	)

	innerbutton4=Button(
		tab1, text="Download",
		width=9,
		height=1,
		bg=buttoncolor,
		fg=txtcolor,
		command=DownloadOOF
	)

	# Create a button to close (destroy) this window.
	inlabel2=Label(tab1)
	inlabel2.configure(text="Restore Icon:",font=('Arial',10,'normal'),fg=txtcolor,bg='white')
	inlabel2.place(relx=0.1,rely=0.15,anchor=W)

	inlabel3=Label(tab1)
	inlabel3.configure(text="Download Old OOF:",font=('Arial',10,'normal'),fg=txtcolor,bg='white')
	inlabel3.place(relx=0.1,rely=0.35,anchor=W)

	inlabel1=Label(tab2)
	inlabel1.configure(text="Text Color:",font=('Arial',10,'normal'),fg=txtcolor,bg='white')
	inlabel1.place(relx=0.1,rely=0.15,anchor=W)

	inlabel5=Label(tab2)
	inlabel5.configure(text="Button:",font=('Arial',10,'normal'),fg=txtcolor,bg='white')
	inlabel5.place(relx=0.1,rely=0.35,anchor=W)
	innerbutton3.place(relx=0.75,rely=0.15,anchor=CENTER)
	innerbutton4.place(relx=0.75,rely=0.35,anchor=CENTER)

	innerbutton=Button(
	tab1, text="Apply",
	width=35,
	height=2,
	bg=buttoncolor,
	fg=txtcolor,
	command=test
)

	innerbutton05=Button(
	tab2, text="Apply",
	width=35,
	height=2,
	bg=buttoncolor,
	fg=txtcolor,
	command=test
	)


	innerbutton.place(relx=0.5,rely=0.9,anchor=CENTER)
	innerbutton05.place(relx=0.5,rely=0.9,anchor=CENTER)

	mode = [
		'Black',
		'Red',
		'Blue',
		'Green',
		'Yellow',
		'Magenta',
		'Cyan'
	]

	mode1 = [
		'White',
		'Red',
		'Blue',
		'Green',
		'Yellow',
		'Magenta',
		'Cyan',
		'Black'
	]

	var = StringVar(tab2)
	var.set(data[0].removesuffix("\n"))

	w=OptionMenu(tab2,var,*mode)
	w.configure(fg=txtcolor,bg=buttoncolor)
	w.place(relx=0.75,rely=0.15,anchor=CENTER)

	var1= StringVar(tab2)
	var1.set(data[1].removesuffix("\n"))

	w1=OptionMenu(tab2,var1,*mode1)
	w1.configure(fg=txtcolor,bg=buttoncolor)
	w1.place(relx=0.75,rely=0.35,anchor=CENTER)

	secondary_window.resizable(False,False)


#Define function for buttons
def NotWindows():
	messagebox.showerror("Compability Error!","This app can only be run on Windows!")
def Mbox(title, text, style):
	return ctypes.windll.user32.MessageBoxW(0, text, title, style)
def NoUWP():
	if platform.system()!='Windows':
		NotWindows()
	else:
		messagebox.showinfo('Roblox OOF Restorer!', "This app currently doesn't support UWP (Universal Windows Platform) Roblox app. It will be added in the future (if possible).")
def ExitApp():
	if platform.system()!='Windows':
		rep='yes'
	#Confirmation message box
	else:
		rep=messagebox.askquestion(title="Roblox OOF Restorer!", message='Do you want to quit the app?')
	if rep=='yes':
		sys.exit()
def PlayOOF():
	if platform.system()!='Windows':
		NotWindows()
	else:
		subprocess.Popen(['start', oggfile], shell=True)
def Settings():
	open_secondary_window()
#---------------------------------------------------------------------------------------------------------------------------------------------------
#Main software
def main():
	if platform.system()!='Windows':
		NotWindows()    
	else:
		try:
			errorgiven=0
			adminname=os.getlogin()
			path=f'C:/Users/{adminname}/AppData/Local/Roblox/Versions'
			#Create a list that includes everything in that directory
			try:
				dir=os.listdir(path)
			except FileNotFoundError:
				messagebox.showerror('Error Occured!', "Whoops! You haven't installed Roblox or not installed the right version (not support UWP app yet).")
				errorgiven=1
			#Remove .exe files from list, only folder.
			for folder in dir:
				if folder.endswith('.exe'):
					dir.remove(folder)
			#Check folder creation date
			date=0
			for folder in dir:
				tempdir=f'{path}/{folder}'
				filecreate=os.path.getctime(tempdir)
				#Pick the latest folder created
				if filecreate>date:
					date=filecreate
					latestfolder=folder
					officialdir=f'{path}/{latestfolder}'
			filetoreplace=f'{officialdir}/content/sounds/ouch.ogg'
			appdir=os.getcwd()
			oggfile=f'{appdir}/Data/ouch.ogg'
			shutil.copy(oggfile,filetoreplace)
			messagebox.showinfo('Roblox OOF Restorer!', 'Your OOF has been successfully restored! Please reuse everytime Roblox updates!')
		#Error occured -> Show message box
		except FileNotFoundError:
			messagebox.showerror('Error Occured!', 'Cannot found "ouch.ogg". Please put that file in the app directory or download in Settings.')
		except Exception:
			if errorgiven==0:
				messagebox.showerror('Error Occured!', 'An unknown error has occured! Please tell me about this error on GitHub.')

#Display Window
gui()
