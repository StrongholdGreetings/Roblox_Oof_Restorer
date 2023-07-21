#Import required library
import shutil,os,time,sys,platform,tkinter,subprocess,requests,json,datetime,time
from tkinter import messagebox,ttk
from tkinter import *

def on_closing():
	if messagebox.askokcancel("Roblox OOF Restorer!",'Do you really want to quit?'):
		sys.exit()

appdir=os.getcwd()

if not os.path.exists(appdir+'/Data'):
	os.makedirs(appdir+"/Data")

version='v1.1.0'
oggfile=f'{appdir}/Data/ouch.ogg'
icofile=f'{appdir}/Data/icon.ico'
try:
	with open('Data/DownloadLog.txt','r') as f:
		currenttime=f.read()
except FileNotFoundError:
	currenttime='Never'

try:
	with open('Data/UpdateAvailable.log','r') as f:
		updatebool=f.read()
except FileNotFoundError:
	updatebool='False'
	with open('Data/UpdateAvailable.log','w') as f:
		updatebool=f.write(updatebool)


op1=35
op2=95
op3=155

xleft=0.09

savedmode='Light'

def FileRestore(x):
	if x==0:
		colordata={"Text":"Black","Button":"White"}
		with open("Data/ColorData.json",'w') as f:
			json.dump(colordata,f,indent=4)
	if x==1:
		updatedata={"NoAskUpdate":"On","CheckWhenStarts":"On"}
		with open('Data/UpdateData.json','w') as f:
			json.dump(updatedata,f,indent=4)
def FileTest(a):
		global f,colordata,updatedata
		if a==0:
			try:
				with open('Data/ColorData.json','r') as f:
					colordata=json.load(f)
				if colordata['Text']==colordata["Button"]:
					FileRestore(0)
			except FileNotFoundError:
				try:
					FileRestore(0)
					FileTest(0)
				except PermissionError:
					messagebox.showerror("Error Occured!","Your log file occured a problem and we cannot restore the file. Sorry!")
		if a==1:
			try:
				with open('Data/UpdateData.json','r') as a:
					updatedata=json.load(a)
			except FileNotFoundError:
				try:
					FileRestore(1)
					FileTest(1)
				except PermissionError:
					messagebox.showerror("Error Occured!","Your log file occured a problem and we cannot restore the file. Sorry!")

FileTest(0)
FileTest(1)

def main():
	global window
	def ApplySettings():
		global colordata,bgcolor,txtcolor,buttoncolor,modechoice,modeaddchoice,line,titlecolor
		FileTest(0)
		bgcolor='gray90'
		titlecolor='black'
		with open("Data/ColorData.json",'r') as f:
			colordata=json.load(f)
		modechoice=txtcolor=colordata["Text"]
		modeaddchoice=buttoncolor=colordata["Button"]


	def DownloadICO():
		try:
			response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/data/icon.ico")
			with open('data/icon.ico',"wb") as a:
				a.write(response.content)
			messagebox.showinfo('Roblox OOF Restorer!', "Icon has been downloaded successfully! Press Apply in settings or restart this program to apply icon.")    
		except requests.exceptions.RequestException:
			messagebox.showerror('Roblox OOF Restorer!', "Icon cannot be downloaded! Check your connection to the web.")

	def DownloadOOF():
		try:
			response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/data/ouch.ogg")
			with open('data/ouch.ogg',"wb") as a:
				a.write(response.content)
			messagebox.showinfo('Roblox OOF Restorer!', "Your old OOF has been downloaded successfully!")    
		except requests.exceptions.RequestException:
			messagebox.showerror('Roblox OOF Restorer!', "Old OOF cannot be downloaded! Check your connection to the web.")

		
	def gui():
		global window,label4
		window=Tk()
		ApplySettings()
		window.geometry('350x400')
		window.configure(bg=bgcolor)
		

		#Title on window
		label=Label(window)
		label.configure(text="Roblox OOF Restorer!",font=('Arial',15,'bold'),fg=titlecolor,bg=bgcolor)
		label.pack()

		#Credit
		label1=Label(window)
		label1.configure(text="by StrongholdGreetings on GitHub",fg=titlecolor,bg=bgcolor)
		label1.pack()

		#Version number
		label3=Label(window)
		label3.configure(text="Version 1.1.0",font=('Arial',8),fg=titlecolor,bg=bgcolor)
		label3.pack()

		label4=Label(window)
		label4.configure(text="No Icon Mode! Restore icon in Settings!",font=('Arial',8),fg=titlecolor,bg=bgcolor)
		
		label5=Label(window)
		label5.configure(text="A new update is available!",font=('Arial',7),fg=titlecolor,bg=bgcolor)
		if updatebool=='True':
			label5.pack()

		#Button to restore OOF
		button=Button(
			window, text="Restore OOF!",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=buttoncolor,
			fg=txtcolor,
			command=mainfunc
		)

		#Button to listen to oof
		button1=Button(
			window, text="Listen to OOF! (Media Player)",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=buttoncolor,
			fg=txtcolor,
			command=PlayOOF
		)

		#Button to show notes
		button2=Button(
			window, text="Notes",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=buttoncolor,
			fg=txtcolor,
			command=NoUWP
		)

		#Button to quit app
		button3=Button(
			window, text="Settings",
			font=('Arial',9,'bold'),
			width=30,
			height=2,
			bg=buttoncolor,
			fg=txtcolor,
			command=Settings
		)

		button4=Button(
			window, text="Quit",
			font=('Arial',9,'bold'),
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

		window.protocol("WM_DELETE_WINDOW", on_closing)

		#Keep window running
		window.mainloop()

	def open_secondary_window():
		global tab1,tab2,tab3,tab4,modeaddchoice,modechoice,temp1,temp2,secondary_window,inlabel7,Label
		# Create secondary (or popup) window.
		#Window for Settings
		secondary_window = tkinter.Toplevel()
		tabcontrol=ttk.Notebook(secondary_window)
		secondary_window.title("Settings")
		secondary_window.geometry('350x350')
		secondary_window.grab_set()
		tab1=ttk.Frame(tabcontrol)
		tab2=ttk.Frame(tabcontrol)
		tab3=ttk.Frame(tabcontrol)
		tab4=ttk.Frame(tabcontrol)
		secondary_window.resizable(False,False)	
		try:
			secondary_window.iconbitmap(icofile)
		except tkinter.TclError:
			if platform.system()=='Windows':
				inlabel4=Label(tab1)
				inlabel4.configure(text="No Icon Mode! Restore icon here!",font=('Arial',8),fg=titlecolor)
				inlabel4.place(relx=0.5,rely=0.82,anchor=S)
		secondary_window.configure(bg=bgcolor)
		
		canvas1=Canvas(tab1,width=330,height=230,scrollregion=(0,0,50,50))
		canvas2=Canvas(tab2,width=330,height=230,scrollregion=(0,0,50,50))
		canvas3=Canvas(tab3,width=330,height=230,scrollregion=(0,0,50,50))
		
		canvas1.grid(row=0, column=0)
		canvas2.grid(row=0, column=0)
		canvas3.grid(row=0, column=0)
		
		vsb1 = Scrollbar(tab1, orient="vertical", command=canvas1.yview)
		vsb1.grid(row=0,column=1,sticky='ns')
		vsb2 = Scrollbar(tab2, orient="vertical", command=canvas2.yview)
		vsb2.grid(row=0,column=1,sticky='ns')
		vsb3 = Scrollbar(tab3, orient="vertical", command=canvas3.yview)
		vsb3.grid(row=0,column=1,sticky='ns')
		
		label=Label(secondary_window)
		label.configure(text="SETTINGS",font=('Arial',15,'bold'),fg=titlecolor,bg=bgcolor)
		label.grid(column=0,row=0)
		labelbl=Label(secondary_window)
		labelbl.configure(text="Version 1.1.0",font=('Arial',7,'normal'),fg=titlecolor,bg=bgcolor)
		labelbl.grid()
		
		
		canvas1.config(yscrollcommand=vsb1.set)
		canvas2.config(yscrollcommand=vsb2.set)
		canvas3.config(yscrollcommand=vsb3.set)


		
		tabcontrol.add(tab1, text='Restore')
		tabcontrol.add(tab2, text='Button')
		tabcontrol.add(tab3, text='Update')

		tabcontrol.grid()
		def test():
			global tab1,tab2
			temp1=var.get()
			temp2=var1.get()
			temp3=var2.get()
			temp4=var3.get()
			if temp1==temp2:
				messagebox.showerror("Error Occured!","Your button color must not be the same as text color")
			else:
				rep=messagebox.askquestion("Roblox OOF Restorer!","Do you really want to apply settings? This app will restart to load settings.")
				if rep=='yes':
					write={"Text":temp1,"Button":temp2}
					with open('Data/ColorData.json','w') as f:
						json.dump(write,f,indent=4)
					write={"NoAskUpdate":temp3,"CheckWhenStarts":temp4}
					with open('Data/UpdateData.json','w') as f:
						json.dump(write,f,indent=4)
					messagebox.showinfo('Roblox OOF Restorer!', "Changes successfully applied! The program will restart to apply changes.")
					secondary_window.destroy()
					window.destroy()
					gui()
				else:
					secondary_window.grab_set()
		
		innerbutton3=Button(
			tab1, text="Restore",
			font=('Arial',9,'bold'),
			width=9,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=DownloadICO
		)
		innerbutton4=Button(
			tab1, text="Download",
			font=('Arial',9,'bold'),
			width=9,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=DownloadOOF
		)

		innerbutton075=Button(
		secondary_window, text="Apply",
		font=('Arial',9,'bold'),
		width=40,
		height=2,
		bg=buttoncolor,
		fg=txtcolor,
		command=test
		)
		
		# Option label
		inlabel2=Label(canvas1)
		inlabel2.configure(text="Restore Icon:",font=('Arial',10,'bold'),fg=titlecolor)
		canvas1.create_window(30,op1,anchor='w',window=inlabel2)
		
		inlabel3=Label(canvas1)
		inlabel3.configure(text="Download Old OOF:",font=('Arial',10,'bold'),fg=titlecolor)
		canvas1.create_window(30,op2,anchor='w',window=inlabel3)
		
		inlabel1=Label(canvas2)
		inlabel1.configure(text="Text Color:",font=('Arial',10,'bold'),fg=titlecolor)
		canvas2.create_window(30,op1,anchor='w',window=inlabel1)

		inlabel5=Label(canvas2)
		inlabel5.configure(text="Button:",font=('Arial',10,'bold'),fg=titlecolor)
		canvas2.create_window(30,op2,anchor='w',window=inlabel5)
		
		inlabel6=Label(canvas3)
		inlabel6.configure(text="Software Update:",font=('Arial',10,'bold'),fg=titlecolor)
		canvas3.create_window(30,35,anchor='w',window=inlabel6)
		
		updatestring=f'Last Checked: {currenttime}'
		inlabel7=Label(canvas3)
		inlabel7.configure(text=updatestring,font=('Arial',8),fg=titlecolor)
		canvas3.create_window(30,53,anchor='w',window=inlabel7)
		
		inlabel8=Label(canvas3)
		inlabel8.configure(text='Update without asking:',font=('Arial',10,'bold'),fg=titlecolor)
		canvas3.create_window(30,95,anchor='w',window=inlabel8)

		inlabel9=Label(canvas3)
		inlabel9.configure(text='Check when app starts:',font=('Arial',10,'bold'),fg=titlecolor)
		canvas3.create_window(30,150,anchor='w',window=inlabel9)
		def Update():
			global currenttime,inlabel7
			try:
				response=requests.get("https://api.github.com/repos/StrongholdGreetings/Roblox_Oof_Restorer/releases/latest")
				currenttime=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
				with open('data/DownloadLog.txt','w') as f:
					f.write(currenttime)
				inlabel7.destroy()
				updatestring=f'Last Checked: {currenttime}'
				inlabel7=Label(canvas3)
				inlabel7.configure(text=updatestring,font=('Arial',8),fg=titlecolor)
				canvas3.create_window(30,53,anchor='w',window=inlabel7)
				latest=response.json()["name"]
				if version>=latest:
					messagebox.showinfo("Roblox OOF Restorer!","Your app is already up to date. No need to update.")
				else:
					updatebool='True'
					with open("Data/UpdateAvailable.log",'w') as f:
						f.write(updatebool)
					if updatedata["NoAskUpdate"]=='Off':
						rep=messagebox.askquestion("Roblox OOF Restorer!","Your app has a new update. Do you want to update?\nNote: After clicking 'Yes', you should not close the app until a message box show up state that your download has completed!")
					else:
						rep='yes'
					if rep=='yes':
						update=f'Roblox OOF Restorer {latest}.exe'
						url = 'https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/releases/download/Roblox/Roblox.OOF.Restorer.exe'
						response=requests.get(url)
						with open(update,'wb') as down:
							down.write(response.content)
						messagebox.showinfo("Roblox OOF Restorer!",'Your app update has been successfully downloaded!')
						updatebool='False'
						with open("Data/UpdateAvailable.log",'w') as f:
							f.write(updatebool)
			except requests.exceptions.RequestException:
				messagebox.showerror("Error Occured!","Your app update cannot be downloaded! Check your connection to the web.")

		innerbutton5=Button(
			tab3, text="Check",
			font=('Arial',9,'bold'),
			width=8,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=Update
		)
		# Button place
		canvas1.create_window(247,op1,anchor='w',window=innerbutton3)
		canvas1.create_window(247,op2,anchor='w',window=innerbutton4)
		canvas3.create_window(247,op1,anchor='w',window=innerbutton5)
		innerbutton075.place(relx=0.5,rely=0.925,anchor=CENTER)
		
		mode = [
			'Black',
			'Red',
			'Orange',
			'Blue',
			'Green',
			'Yellow',
			'Magenta',
			'Cyan',
			'White'
		]
		mode1 = [
			'White',
			'Red',
			'Orange',
			'Blue',
			'Green',
			'Yellow',
			'Magenta',
			'Cyan',
			'Black'
		]
		var = StringVar(canvas2)
		var.set(colordata["Text"])
		w=OptionMenu(canvas2,var,*mode)
		w.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas2.create_window(247,op1,anchor='w',window=w)
		
		var1= StringVar(canvas2)
		var1.set(colordata["Button"])
		w1=OptionMenu(canvas2,var1,*mode1)
		w1.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas2.create_window(247,op2,anchor='w',window=w1)

		mode2=["Off","On"]
		var2= StringVar(canvas3)
		var2.set(updatedata["NoAskUpdate"])
		w2=OptionMenu(canvas3,var2,*mode2)
		w2.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas3.create_window(247,96,anchor='w',window=w2)
		
		mode3=["Off","On"]
		var3=StringVar(canvas3)
		var3.set(updatedata['CheckWhenStarts'])
		w3=OptionMenu(canvas3,var3,*mode3)
		w3.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas3.create_window(247,150,anchor='w',window=w3)
		

	#Define function for buttons
	def NotWindows():
		messagebox.showerror("Compability Error!","This app can only be run on Windows!")
	def NoUWP():
		if platform.system()!='Windows':
			NotWindows()
		else:
			messagebox.showinfo('Roblox OOF Restorer!', "This app currently doesn't support UWP (Universal Windows Platform) Roblox app. It will be added in the future (if possible).")
	def ExitApp():
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
	def mainfunc():
		if platform.system()!='Windows':
			NotWindows()    
		else:
			try:
				errorgiven=0
				adminname=os.getlogin()
				path=f'C:/Users/{adminname}/AppData/Local/Roblox/Versions'
				#Create a list that includes everything in that directory
				try:
					file=os.listdir(path)
				except FileNotFoundError:
					messagebox.showerror('Error Occured!', "Whoops! You haven't installed Roblox or not installed the right version (not support UWP app yet).")
					errorgiven=1
				#Remove .exe files from list, only folder.
				for folder in file:
					if folder.endswith('.exe'):
						file.remove(folder)
				#Check folder creation date
				date=0
				for folder in file:
					tempdir=f'{path}/{folder}'
					filecreate=os.path.getctime(tempdir)
					#Pick the latest folder created
					if filecreate>date:
						date=filecreate
						latestfolder=folder
						officialdir=f'{path}/{latestfolder}'
				filetoreplace=f'{officialdir}/content/sounds/ouch.ogg'
				appdir=os.getcwd()
				oggfile=f'{appdir}/data/ouch.ogg'
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

try:
	if updatedata['CheckWhenStarts']=='On':
		response=requests.get("https://api.github.com/repos/StrongholdGreetings/Roblox_Oof_Restorer/releases/latest")
		currenttime=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
		with open('data/DownloadLog.txt','w') as f:
			f.write(currenttime)
		latest=response.json()["name"]
		if version<latest:
			rep=messagebox.askquestion("Roblox OOF Restorer!","Your app has a new update. Do you want to update?\nNote: After clicking 'Yes', you should not close the app until a message box show up state that your download has completed!")
			updatebool='True'
			with open("Data/UpdateAvailable.log",'w') as f:
				f.write(updatebool)
			if rep=='yes':
				update=f'Roblox OOF Restorer {latest}.exe'
				url = 'https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/releases/download/Roblox/Roblox.OOF.Restorer.exe'
				response=requests.get(url)
				with open(update,'wb') as down:
					down.write(response.content)
				messagebox.showinfo("Roblox OOF Restorer!",'Your app update has been successfully downloaded!')
				updatebool='False'
				with open("Data/UpdateAvailable.log",'w') as f:
						f.write(updatebool)
	main()
except tkinter.TclError:
	rep=messagebox.showerror("Error Occured!","Seems like there is an illegal value in the JSON file. Do you want to restore all value to default?",type='yesno')
	if rep=='yes':
		try:
			colordata={"Text":"Black","Button":"White"}
			with open("Data/ColorData.json",'w') as f:
				json.dump(colordata,f,indent=4)
			messagebox.showinfo('Roblox OOF Restorer','Your file is successfully restored!')
			main()
		except Exception:
			messagebox.showerror("Error Occured!","Whoops! An unknown error occured and the file cannot be fixed.")
except requests.exceptions.RequestException:
	main()	
except Exception as error:
	messagebox.showerror('Critical Error Occured!','A critical error happened and this app needs to quit! Please tell me about this error on my GitHub page.')
