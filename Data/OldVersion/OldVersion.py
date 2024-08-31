#Import required library
LaunchBySettings=False
import shutil,os,time,sys,platform,tkinter,subprocess,requests,json,datetime,time
from tkinter import messagebox,ttk
from tkinter import *
DataInFirstTime=['This file determines if the program has been run for the first time or not. Do not modifiy, move or delete this file or the program will rerun setup (which requires Internet).\n','IsFirstTime=False']
defaultcolor={"Text":"Black","Button":"White","Theme":"Light"}
defaultupdate={"NoAskUpdate":"Off","CheckWhenStarts":"On"}

def on_closing():
	if messagebox.askyesno("Roblox OOF Restorer!",'Do you really want to quit?'):
		try:
			os.remove('Data/UpdateAvailable.temp')
			sys.exit()
		except Exception:
			sys.exit()

def OSRecognition():
	if platform.system()=='Windows':
		return 'Windows'
	elif platform.system()=='Linux':
		linuxver=platform.version()
		linuxsplit=linuxver.split(' ',3)
		if linuxsplit[2]=='PREEMPT':
			return 'Android'
		else:
			return 'Linux'
	elif platform.system()=='Darwin':
		return 'MacOS'
appdir=os.getcwd()

#Launch First Time Window if not set up!
def FirstTimeSetup():
	global bar
	#Progress Bar
	progress=Tk()
	progress.title("Roblox OOF Restorer")
	progress.aspect(1,1,1,1)
	progress.configure(bg='gray90')
	progress.geometry("350x350")
	#Title
	label=Label(progress)
	label.configure(text="Welcome to Instant Setup.",font=('Arial',15,'bold'),bg='gray90')
	label.place(relx=0.5,rely=0.05,anchor=CENTER)
	label1=Label(progress)
	label1.configure(text="Download things you need with just a click!",font=('Times New Roman',9,'bold'),bg='gray90')
	label1.place(relx=0.5,rely=0.12,anchor=CENTER)
	dash=Label(progress)
	dash.configure(text=">------------------------------------------------------<",font=('Times New Roman',9),bg='gray90')
	dash.place(relx=0.5,rely=0.18,anchor=CENTER)
	label2=Label(progress)
	label2.configure(text="Press Download to download necessary files!",font=('Times New Roman',9),bg='gray90')
	label2.place(relx=0.5,rely=0.25,anchor=CENTER)
	label3=Label(progress)
	label3.configure(text="Press Skip to skip the setup!",font=('Times New Roman',9),bg='gray90')
	label3.place(relx=0.5,rely=0.31,anchor=CENTER)
	label4=Label(progress)
	label4.configure(text="Don't trust me? Press Info for my source code",font=('Times New Roman',9),bg='gray90')
	label4.place(relx=0.5,rely=0.37,anchor=CENTER)

	bar=ttk.Progressbar(progress, orient=HORIZONTAL, length=280,mode='determinate')

	def CancelAction():
		rep=messagebox.askyesno('Instant Setup','Do you really want to skip the setup? You will have to manually download files in Settings!')
		if rep:
			with open('Data/IsFirstTime.txt','w') as f:
				for lines in DataInFirstTime:
					f.writelines(lines)
			progress.destroy()
	def MoreInfo():
		os.system('start "" "https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/blob/main/Roblox_Oof_Restorer.py"')
	def Begin():
		if messagebox.askyesno("Instant Setup","Do you want to continue?"):
			try:
				if not os.path.isdir(appdir+'/Data'):
					os.makedirs(appdir+"/Data")

				response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/icon.ico")
				with open('Data/icon.ico',"wb") as a:
					a.write(response.content)
				bar['value']+=70
				progress.update_idletasks()
				response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch.ogg")
				with open('Data/ouch.ogg',"wb") as a:
					a.write(response.content)
				bar['value']+=70
				progress.update_idletasks()
				response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch%20(NEW).ogg")
				with open('Data/NewOuch.ogg','wb') as f:
					f.write(response.content)
				bar['value']+=70
				progress.update_idletasks()
				with open('Data/IsFirstTime.txt','w') as f:
					for lines in DataInFirstTime:
						f.writelines(lines)
				bar['value']+=70
				progress.update_idletasks()
				if bar['value']==280:
					messagebox.showinfo("Instant Setup","Setup completed! You can now use the app normally!")
				progress.destroy()
			except requests.exceptions.RequestException:
				messagebox.showerror('Instant Setup', "An internet connection is required to download all necessary elements for the app to run. Please connect to the Internet and try again!")
	bar.place(relx=0.5,rely=0.6,anchor=CENTER)
	Button(progress,text='Download',width=9,height=1,command=Begin).pack(anchor=SE,side=RIGHT)
	Button(progress,text='Skip',width=7,height=1,command=CancelAction).pack(anchor=SE,side=RIGHT)
	Button(progress,text='Info',width=6,height=1,command=MoreInfo).pack(anchor=SE,side=RIGHT)
	if LaunchBySettings==False:
		progress.protocol("WM_DELETE_WINDOW", on_closing)
	progress.mainloop()

if not os.path.isdir(appdir+'/Data'):
	os.makedirs(appdir+"/Data")

try:
	with open("Data/IsFirstTime.txt","r") as f:
		IsFirst=list(f.readlines())
	if IsFirst!=DataInFirstTime:
		FirstTimeSetup()
except FileNotFoundError:
	FirstTimeSetup()
	
version='v1.2.0.1'
oggfile=f'{appdir}/Data/ouch.ogg'
icofile=f'{appdir}/Data/icon.ico'
colordatafile=f'{appdir}/Data/ColorData.json'

try:
	with open('Data/DownloadLog.txt','r') as f:
		currenttime=f.read()
except FileNotFoundError:
	currenttime='Never'

try:
	with open('Data/UpdateAvailable.temp','r') as f:
		updatebool=f.read()
except FileNotFoundError:
	updatebool='False'
	with open('Data/UpdateAvailable.temp','w') as f:
		updatebool=f.write(updatebool)


op1=35
op2=95
op3=155
op4=215
op5=275

if platform.system()=='Windows':
	widthcheckbutton=7
	widthbutton=9
else:
	widthcheckbutton=5
	widthbutton=7

xleft=0.09

savedmode='Light'

def FileRestore(x):
	if x==0:
		with open("Data/ColorData.json",'w') as f:
			json.dump(defaultcolor,f,indent=4)
	if x==1:
		with open('Data/UpdateData.json','w') as f:
			json.dump(defaultupdate,f,indent=4)
def FileTest(a):
		global f,colordata,updatedata
		if a==0:
			try:
				with open('Data/ColorData.json','r') as f:
					colordata=json.load(f)
				if colordata['Text']==colordata["Button"]:
					FileRestore(0)
				test=colordata['Text']
				test=colordata['Button']
				test=colordata['Theme']
			except FileNotFoundError:
				try:
					FileRestore(0)
					FileTest(0)
				except PermissionError:
					messagebox.showerror("Error Occured!","Your log file occured a problem and we cannot restore the file. Sorry!")
			except KeyError as c:
				missdata=str(c)
				missdata=missdata.replace("'",'')
				colordata[missdata]=defaultcolor[missdata]
				with open('Data/ColorData.json','w') as f:
					json.dump(colordata,f,indent=4)
				FileTest(0)
			except Exception:
				os.remove(colordatafile)
				FileRestore(0)	
		if a==1:
			try:
				with open('Data/UpdateData.json','r') as a:
					updatedata=json.load(a)
					test=updatedata["NoAskUpdate"]
					test=updatedata["CheckWhenStarts"]
			except FileNotFoundError:
				try:
					FileRestore(1)
					FileTest(1)
				except PermissionError:
					messagebox.showerror("Error Occured!","Your log file occured a problem and we cannot restore the file. Sorry!")
			except KeyError as c:
				missdata=str(c)
				missdata=missdata.replace("'",'')
				updatedata[missdata]=defaultupdate[missdata]
				FileTest(1)
			except Exception:
				FileRestore(1)


FileTest(0)
FileTest(1)

def main():
	global window
	def ApplySettings():
		global colordata,bgcolor,txtcolor,buttoncolor,modechoice,modeaddchoice,line,titlecolor,tabcolorchoice,tabtextchoice
		FileTest(0)
		bgcolor='gray80'
		titlecolor='black'
		tabcolorchoice='gray99'
		tabtextchoice='black'
		with open("Data/ColorData.json",'r') as f:
			colordata=json.load(f)
		modechoice=txtcolor=colordata["Text"]
		modeaddchoice=buttoncolor=colordata["Button"]
		if colordata["Theme"]=="Dark":
			bgcolor='gray9'
			titlecolor='white'
			tabcolorchoice='gray25'
			tabtextchoice='black'


	def DownloadICO():
		try:
			response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/icon.ico")
			with open('Data/icon.ico',"wb") as a:
				a.write(response.content)
			messagebox.showinfo('Roblox OOF Restorer!', "Icon has been downloaded successfully! Press Apply in settings or restart this program to apply icon.")    
		except requests.exceptions.RequestException:
			messagebox.showerror('Roblox OOF Restorer!', "Icon cannot be downloaded! Check your connection to the web.")

	def DownloadOOF():
		try:
			response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch.ogg")
			with open('Data/ouch.ogg',"wb") as a:
				a.write(response.content)
			messagebox.showinfo('Roblox OOF Restorer!', "Your old OOF has been downloaded successfully!")    
		except requests.exceptions.RequestException:
			messagebox.showerror('Roblox OOF Restorer!', "Old OOF cannot be downloaded! Check your connection to the web.")
	def RestoreNewOOF():
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
				oggfile=f'{appdir}/Data/NewOuch.ogg'
				shutil.copy(oggfile,filetoreplace)
				messagebox.showinfo('Roblox OOF Restorer!', 'Your OOF has been reverted!')
			#Error occured -> Show message box
			except FileNotFoundError:
				messagebox.showerror('Error Occured!', 'Cannot found "ouch.ogg". Please put that file in the app directory or download in Settings.')
			except Exception:
				if errorgiven==0:
					messagebox.showerror('Error Occured!', 'An unknown error has occured! Please tell me about this error on GitHub.')
		
	def gui():
		global window,label4
		window=Tk()
		ApplySettings()
		if OSRecognition()=='Android':
			window.geometry('350x420')
		else:
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
		label3.configure(text="Version 1.2.0.1",font=('Arial',8),fg=titlecolor,bg=bgcolor)
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
		button.place(relx=0.5,rely=0.3,anchor=CENTER)
		button2.place(relx=0.5,rely=0.47,anchor=CENTER)
		button3.place(relx=0.5,rely=0.64,anchor=CENTER)
		button4.place(relx=0.5,rely=0.81,anchor=CENTER)

		#Window title
		window.title("Roblox OOF Restorer!")

		#Show icon on Title bar
		try:
			window.iconbitmap(icofile)
		except tkinter.TclError:
			if platform.system()=='Windows':
				label4.place(relx=0.5,rely=1,anchor=S)

		window.protocol("WM_DELETE_WINDOW", on_closing)

		#Keep window running
		window.mainloop()

	def open_secondary_window():
		LaunchBySettings=True
		global tab1,tab2,tab3,tab4,modeaddchoice,modechoice,temp1,temp2,secondary_window,inlabel7,Label
		# Create secondary (or popup) window.
		#Window for Settings
		secondary_window = tkinter.Toplevel()
		tabcontrol=ttk.Notebook(secondary_window)
		secondary_window.title("Settings")
		
		# Changing tab color
		s = ttk.Style()
		s.theme_use('default')
		s.configure('TNotebook', background=bgcolor,foreground=titlecolor)
		s.map("TNotebook")
		s1 = ttk.Style()
		s1.configure('TNotebook.Tab', background=bgcolor,foreground=titlecolor)
		s1.map("TNotebook.Tab", background= [("selected", tabcolorchoice)],foreground=[("selected", tabtextchoice)])


		if platform.system()=='Windows':
			secondary_window.geometry('350x360')
		elif OSRecognition()=="Android":
			secondary_window.geometry('350x370')
		else:
			secondary_window.geometry('350x365')
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
		
		canvas1=Canvas(tab1,width=330,height=230,scrollregion=(0,0,900,300),bg=bgcolor)
		canvas2=Canvas(tab2,width=330,height=230,scrollregion=(0,0,900,260),bg=bgcolor)
		canvas3=Canvas(tab3,width=330,height=230,scrollregion=(0,0,50,50),bg=bgcolor)
		
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
		labelbl.configure(text="Version 1.2.0.1",font=('Arial',7,'normal'),fg=titlecolor,bg=bgcolor)
		labelbl.grid()

		canvas1.config(yscrollcommand=vsb1.set)
		canvas2.config(yscrollcommand=vsb2.set)
		canvas3.config(yscrollcommand=vsb3.set)


		
		tabcontrol.add(tab1, text='Restore')
		tabcontrol.add(tab2, text='UI')
		tabcontrol.add(tab3, text='Update')

		tabcontrol.grid()
	#Update save file to apply settings	
		def test():
			global tab1,tab2
			temp1=var.get()
			temp2=var1.get()
			temp3=var2.get()
			temp4=var3.get()
			temp5=var4.get()
			if temp1==temp2:
				messagebox.showerror("Error Occured!","Your button color must not be the same as text color")
			else:
				rep=messagebox.askquestion("Roblox OOF Restorer!","Do you really want to apply settings? This app will restart to load settings.")
				if rep=='yes':
					write={"Text":temp1,"Button":temp2,"Theme":temp5}
					with open('Data/ColorData.json','w') as f:
						json.dump(write,f,indent=4)
					write={"NoAskUpdate":temp3,"CheckWhenStarts":temp4}
					with open('Data/UpdateData.json','w') as f:
						json.dump(write,f,indent=4)
					messagebox.showinfo('Roblox OOF Restorer!', "Changes successfully applied! The program will restart to apply changes.")
					secondary_window.destroy()
					window.destroy()
					gui()
		def ResetColor():	
			rep=messagebox.askquestion("Roblox OOF Restorer!","Do you really want to reset all color settings? This app will restart to load settings.")
			if rep=='yes':
				with open('Data/ColorData.json','w') as f:
					json.dump(defaultcolor,f,indent=4)
				messagebox.showinfo('Roblox OOF Restorer!', "Your UI settings have been successfully reset! Click OK to reload")
				secondary_window.destroy()
				window.destroy()
				gui()
		
		innerbutton3=Button(
			tab1, text="Restore",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=DownloadICO
		)
		innerbutton4=Button(
			tab1, text="Download",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=DownloadOOF
		)
		
		innerbutton6=Button(
			tab2, text="Restore",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=ResetColor
		)

		innerbutton7=Button(
			tab1, text="Play",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=PlayOOF
		)
		
		innerbutton8=Button(
			tab1, text="Restore",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=RestoreNewOOF
		)
		
		innerbutton9=Button(
			tab1, text="Rerun",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=FirstTimeSetup
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
		#Tab1
		inlabel2=Label(canvas1)
		inlabel2.configure(text="Restore Icon:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas1.create_window(30,op1,anchor='w',window=inlabel2)

		inlabel3=Label(canvas1)
		inlabel3.configure(text="Download Old OOF:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas1.create_window(30,op2,anchor='w',window=inlabel3)
		
		inlabel14=Label(canvas1)
		inlabel14.configure(text="Play Old OOF:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas1.create_window(30,op3,anchor='w',window=inlabel14)
		
		inlabel15=Label(canvas1)
		inlabel15.configure(text="Revert to Ouch:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas1.create_window(30,op4,anchor='w',window=inlabel15)
		
		inlabel16=Label(canvas1)
		inlabel16.configure(text="Rerun Setup:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas1.create_window(30,op5,anchor='w',window=inlabel16)
		#Tab 2
		inlabel1=Label(canvas2)
		inlabel1.configure(text="Text Color:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas2.create_window(30,op1,anchor='w',window=inlabel1)

		inlabel5=Label(canvas2)
		inlabel5.configure(text="Button:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas2.create_window(30,op2,anchor='w',window=inlabel5)
		
		inlabel10=Label(canvas2)
		inlabel10.configure(text="Background Theme:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas2.create_window(30,152,anchor='w',window=inlabel10)
		
		inlabel12=Label(canvas2)
		inlabel12.configure(text="Won't affect button color",font=('Arial',8),fg=titlecolor,bg=bgcolor)
		canvas2.create_window(30,170,anchor='w',window=inlabel12)
		
		inlabel13=Label(canvas2)
		inlabel13.configure(text="Reset to default:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas2.create_window(30,op4,anchor='w',window=inlabel13)
		#Tab 3
		inlabel6=Label(canvas3)
		inlabel6.configure(text="Software Update:",font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas3.create_window(30,35,anchor='w',window=inlabel6)
		
		updatestring=f'Last Checked: {currenttime}'
		inlabel7=Label(canvas3)
		inlabel7.configure(text=updatestring,font=('Arial',8),fg=titlecolor,bg=bgcolor)
		canvas3.create_window(30,53,anchor='w',window=inlabel7)
		
		
		inlabel8=Label(canvas3)
		inlabel8.configure(text='Update without asking:',font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas3.create_window(30,op2,anchor='w',window=inlabel8)

		inlabel9=Label(canvas3)
		inlabel9.configure(text='Check when app starts:',font=('Arial',10,'bold'),fg=titlecolor,bg=bgcolor)
		canvas3.create_window(30,op3,anchor='w',window=inlabel9)
		def Update():
			global currenttime,inlabel7
			try:
				response=requests.get("https://api.github.com/repos/StrongholdGreetings/Roblox_Oof_Restorer/releases/latest")
				currenttime=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
				with open('Data/DownloadLog.txt','w') as f:
					f.write(currenttime)
				inlabel7.destroy()
				updatestring=f'Last Checked: {currenttime}'
				inlabel7=Label(canvas3)
				inlabel7.configure(text=updatestring,font=('Arial',8),fg=titlecolor,bg=bgcolor)
				canvas3.create_window(30,53,anchor='w',window=inlabel7)
				latest=response.json()["name"]
				if version>=latest:
					messagebox.showinfo("Roblox OOF Restorer!","Your app is already up to date. No need to update.")
				else:
					updatebool='True'
					with open("Data/UpdateAvailable.temp",'w') as f:
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
						with open("Data/UpdateAvailable.temp",'w') as f:
							f.write(updatebool)
			except requests.exceptions.RequestException:
				messagebox.showerror("Error Occured!","Cannot check for updates! Check your connection to the web.")

		innerbutton5=Button(
			tab3, text="Check",
			font=('Arial',9,'bold'),
			width=widthcheckbutton,
			height=1,
			bg=buttoncolor,
			fg=txtcolor,
			command=Update
		)
		# Button place
		canvas1.create_window(316,op1,anchor='e',window=innerbutton3)
		canvas1.create_window(316,op2,anchor='e',window=innerbutton4)
		canvas3.create_window(316,op1,anchor='e',window=innerbutton5)
		canvas2.create_window(316,op4,anchor='e',window=innerbutton6)
		canvas1.create_window(316,op3,anchor='e',window=innerbutton7)
		canvas1.create_window(316,op4,anchor='e',window=innerbutton8)
		canvas1.create_window(316,op5,anchor='e',window=innerbutton9)
		innerbutton075.place(relx=0.5,rely=0.925,anchor=CENTER)
		
		mode = [
			'Black',
			'Red',
			'Orange',
			'Blue',
			'Green',
			'Yellow',
			'Magenta',
			'Purple',
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
			'Purple',	
			'Cyan',
			'Black',
		]
		
		var = StringVar(canvas2)
		var.set(colordata["Text"])
		w=OptionMenu(canvas2,var,*mode)
		w.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas2.create_window(316,op1,anchor='e',window=w)
		
		var1= StringVar(canvas2)
		var1.set(colordata["Button"])
		w1=OptionMenu(canvas2,var1,*mode1)
		w1.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas2.create_window(316,op2,anchor='e',window=w1)

		mode2=["Off","On"]
		var2= StringVar(canvas3)
		var2.set(updatedata["NoAskUpdate"])
		w2=OptionMenu(canvas3,var2,*mode2)
		w2.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas3.create_window(316,op2,anchor='e',window=w2)
		
		mode3=["Off","On"]
		var3=StringVar(canvas3)
		var3.set(updatedata['CheckWhenStarts'])
		w3=OptionMenu(canvas3,var3,*mode3)
		w3.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas3.create_window(316,op3,anchor='e',window=w3)
		
		mode4=["Light","Dark"]
		var4=StringVar(canvas2)
		var4.set(colordata['Theme'])
		w4=OptionMenu(canvas2,var4,*mode4)
		w4.configure(font=('Arial',9,'bold'),fg=txtcolor,bg=buttoncolor)
		canvas2.create_window(316,op3,anchor='e',window=w4)
		
		

	#Define function for buttons
	def NotWindows():
		if OSRecognition()=='Android':
				messagebox.showerror("Compability Error!","Sorry! This app can't be run on Android (yet)")
		elif OSRecognition()=='Linux':
				messagebox.showerror("Compability Error!","Sorry! Just to remind you that Roblox doesn't support Linux.")
	def NoUWP():
		if platform.system()!='Windows':
			NotWindows()
		else:
			messagebox.showinfo('Roblox OOF Restorer!', "This app currently doesn't support UWP (Universal Windows Platform) Roblox app.")
	def ExitApp():
		rep=messagebox.askquestion(title="Roblox OOF Restorer!", message='Do you want to quit the app?')
		if rep=='yes':
			sys.exit()
	def PlayOOF():
		if platform.system()!='Windows':
			messagebox.showerror("Error Occured!","This feature cannot be run on your system!")
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
				rep=messagebox.askyesno('Roblox OOF Restorer!', "Roblox will be force closed to install OOF! Do you really want to continue?")
				if rep:
					os.system('taskkill /im RobloxPlayerLauncher.exe')
					os.system('taskkill /im RobloxPlayerBeta.exe')
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
		with open('Data/DownloadLog.txt','w') as f:
			f.write(currenttime)
		latest=response.json()["name"]
		if version<latest:
			rep=messagebox.askquestion("Roblox OOF Restorer!","Your app has a new update. Do you want to update?\nNote: After clicking 'Yes', you should not close the app until a message box show up state that your download has completed!")
			updatebool='True'
			with open("Data/UpdateAvailable.temp",'w') as f:
				f.write(updatebool)
			if rep=='yes':
				update=f'Roblox OOF Restorer {latest}.exe'
				url = 'https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/releases/download/Roblox/Roblox.OOF.Restorer.exe'
				response=requests.get(url)
				with open(update,'wb') as down:
					down.write(response.content)
				messagebox.showinfo("Roblox OOF Restorer!",'Your app update has been successfully downloaded!')
				updatebool='False'
				with open("Data/UpdateAvailable.temp",'w') as f:
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
