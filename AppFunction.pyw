#Import required library
import shutil,os,time,sys,platform,tkinter,requests,json,datetime,time,random
appdir=os.getcwd()
adminname=os.getlogin()
defaultcolor={"Text":"Black","Button":"White","Theme":"Light"}
defaultupdate={"NoAskUpdate":"Off","CheckWhenStarts":"On","CheckRobloxWhenStarts": "Off"}
version='v1.3'
oggfile=f'{appdir}/Data/Media/ouch.ogg'
icofile=f'{appdir}/Data/Media/icon.ico'
colordatafile=f'{appdir}/Data/ColorData.json'

def GetUpdate():
	global officialdir
	adminname=os.getlogin()
	path=f'C:/Users/{adminname}/AppData/Local/Roblox/Versions'
	for root, dirs, files in os.walk(path):
	    for file in files:
	        if file in ["RobloxPlayerLauncher.exe","RobloxPlayerInstaller.exe","RobloxPlayerBeta.exe"]:
	            listdir=os.path.join(root, file)
	dirlist=listdir.replace("\\","/")
	dirgot=dirlist.split("/")
	officialdir=f"{path}"+"/"+f"{dirgot[-2]}"
	return officialdir
def mainfunc(purpose):
	if platform.system()!='Windows':
		NotWindows()    
	else:
		try:
			rep=tkinter.messagebox.askyesno('Roblox OOF Restorer!', "Roblox will be force closed to install OOF! Do you really want to continue?")
			if rep:
				os.system('taskkill /im RobloxPlayerLauncher.exe')
				os.system('taskkill /im RobloxPlayerBeta.exe')
				errorgiven=0
				GetUpdate()
				#File replace
				if purpose==0:
					filetoreplace=f'{officialdir}/content/sounds/ouch.ogg'
					#For some reason if I don't call oggfile again it won't work so it stays here for now!
					appdir=os.getcwd()
					oggfile=f'{appdir}/Data/Media/ouch.ogg'
					shutil.copy(oggfile,filetoreplace)
					tkinter.messagebox.showinfo('Roblox OOF Restorer!', 'Your OOF has been successfully restored! Please reuse everytime Roblox updates!')
				elif purpose==1:
					filetoreplace=f'{officialdir}/content/sounds/ouch.ogg'
					appdir=os.getcwd()
					oggfile=f'{appdir}/Data/Media/NewOuch.ogg'
					shutil.copy(oggfile,filetoreplace)
					tkinter.messagebox.showinfo('Roblox OOF Restorer!', 'Your OOF has been reverted!')
		#Error occured -> Show message box
		except FileNotFoundError:
			if purpose==0:
				tkinter.messagebox.showerror('Error Occured!', 'Cannot found "ouch.ogg". Please put that file in the app directory or download in Settings.')
			elif purpose==1:
				tkinter.messagebox.showerror('Error Occured!', 'Cannot found "NewOuch.ogg". Please put that file in the app directory or download using Instant Setup.')
		except Exception:
			if errorgiven==0:
				tkinter.messagebox.showerror('Error Occured!', 'An unknown error has occured! Please tell me about this error on GitHub.')




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
					tkinter.messagebox.showerror("Error Occured!","Your log file occured a problem and we cannot restore the file. Sorry!")
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
					tkinter.messagebox.showerror("Error Occured!","Your log file occured a problem and we cannot restore the file. Sorry!")
			except KeyError as c:
				missdata=str(c)
				missdata=missdata.replace("'",'')
				updatedata[missdata]=defaultupdate[missdata]
				FileTest(1)
			except Exception:
				FileRestore(1)


def ApplySettings():
	global colordata,bgcolor,txtcolor,buttoncolor,modechoice,modeaddchoice,line,titlecolor,tabcolorchoice,tabtextchoice
	FileTest(0)
	ThemeColorData={"bgcolor":"gray80","titlecolor":"black","tabcolorchoice":"gray99","tabtextchoice":"black"}
	with open("Data/ColorData.json",'r') as f:
		colordata=json.load(f)
	modechoice=txtcolor=colordata["Text"]
	modeaddchoice=buttoncolor=colordata["Button"]
	if colordata["Theme"]=="Dark":
		ThemeColorData={"bgcolor":"gray15","titlecolor":"white","tabcolorchoice":"gray25","tabtextchoice":"black"}
	if colordata["Theme"]=="Midnight":
		ThemeColorData={"bgcolor":"black","titlecolor":"white","tabcolorchoice":"gray9","tabtextchoice":"black"}
	return ThemeColorData
	
def DownloadICO():
	try:
		response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/icon.ico")
		with open('Data/Media/icon.ico',"wb") as a:
			a.write(response.content)
		tkinter.messagebox.showinfo('Roblox OOF Restorer!', "Icon has been downloaded successfully! Press Apply in settings or restart this program to apply icon.")    
	except requests.exceptions.RequestException:
		tkinter.messagebox.showerror('Roblox OOF Restorer!', "Icon cannot be downloaded! Check your connection to the web.")
def DownloadOOF():
	try:
		response=requests.get("https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/raw/main/Data/ouch.ogg")
		with open('Data/Media/ouch.ogg',"wb") as a:
			a.write(response.content)
		tkinter.messagebox.showinfo('Roblox OOF Restorer!', "Your old OOF has been downloaded successfully!")    
	except requests.exceptions.RequestException:
		tkinter.messagebox.showerror('Roblox OOF Restorer!', "Old OOF cannot be downloaded! Check your connection to the web.")
def PlayOOF():
	if platform.system()!='Windows':
		tkinter.messagebox.showerror("Error Occured!","This feature cannot be run on your system!")
	else:
		SendStringToOS=f"{oggfile}"
		os.system(SendStringToOS)
	
def ResetColor():	
	rep=tkinter.messagebox.askquestion("Roblox OOF Restorer!","Do you really want to reset all color settings? This app will restart to load settings.")
	if rep=='yes':
		with open('Data/ColorData.json','w') as f:
			json.dump(defaultcolor,f,indent=4)
		tkinter.messagebox.showinfo('Roblox OOF Restorer!', "Your UI settings have been successfully reset! Restart the app to reload your settings.")
	return rep
def UpdateOnStart():
	with open("Data/UpdateData.json","r") as f:
		updatedata=json.load(f)
	if updatedata['CheckWhenStarts']=='On':
		response=requests.get("https://api.github.com/repos/StrongholdGreetings/Roblox_Oof_Restorer/releases/latest")
		currenttime=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
		with open('Data/TXT/DownloadLog.txt','w') as f:
			f.write(currenttime)
		latest=response.json()["name"]
		if version>latest:
			randomness=random.randint(1,2)
			if randomness==1:
				tkinter.messagebox.showerror("Error!","How do you even have this confidential version!!! The program will automatically shut down to prevent spoilers!")
				sys.exit()
		if version<latest:
			rep=tkinter.messagebox.askquestion("Roblox OOF Restorer!","Your app has a new update. Do you want to update?\nNote: After clicking 'Yes', you should not close the app until a message box show up state that your download has completed!")
			updatebool='True'
			with open("Data/TXT/UpdateAvailable.temp",'w') as f:
				f.write(updatebool)
			if rep=='yes':
				update=f'Roblox OOF Restorer {latest}.exe'
				url = 'https://github.com/StrongholdGreetings/Roblox_Oof_Restorer/releases/download/Roblox/Roblox.OOF.Restorer.exe'
				response=requests.get(url)
				with open(update,'wb') as down:
					down.write(response.content)
				tkinter.messagebox.showinfo("Roblox OOF Restorer!",'Your app update has been successfully downloaded!')
				updatebool='False'
				with open("Data/TXT/UpdateAvailable.temp",'w') as f:
					f.write(updatebool)

def CheckRobloxUpdates():
	CurrentValue=GetUpdate()
	try:
		with open("Data/UpdateData.json",'r') as f:
			updatedata=json.load(f)
			CheckValue=updatedata["CheckRobloxWhenStarts"]
	except FileNotFoundError:
		CheckValue="Off"
	except KeyError:
		CheckValue="Off"
		updatedata={"NoAskUpdate":updatedata["NoAskUpdate"],"CheckWhenStarts":updatedata["CheckWhenStarts"],"CheckRobloxWhenStarts": "Off"}
		with open("Data/UpdateData.json",'w') as f:
			json.dump(updatedata,f,indent=4)
		CheckRobloxUpdates()
	if CheckValue=="On":
		try:
			with open("Data/TXT/RobloxUpdate.txt",'r') as f:
				PastValue=f.read()
		except FileNotFoundError:
			with open("Data/TXT/RobloxUpdate.txt",'w') as f:
				f.write(CurrentValue)
				PastValue="null"
		if CurrentValue!=PastValue:
			with open("Data/TXT/RobloxUpdate.txt",'w') as f:
				f.write(CurrentValue)
			ask=tkinter.messagebox.askyesno("Roblox OOF Restorer!","A new version of Roblox might be installed on your device. Do you want to restore OOF now?")
			if ask:
				mainfunc(1)
	
def ExitApp():
	ask=tkinter.messagebox.askyesno("Roblox OOF Restorer!",'Do you really want to quit?')
	if ask:
		try:
			os.remove('Data/TXT/UpdateAvailable.temp')
			sys.exit()
		except Exception:
			sys.exit()
	

def NotWindows():
	if OSRecognition()=='Android':
		tkinter.messagebox.showerror("Compability Error!","Sorry! This app can't be run on Android (yet)")
	elif OSRecognition()=='Linux':
		tkinter.messagebox.showerror("Compability Error!","Sorry! Just to remind you that Roblox doesn't support Linux.")
def NoUWP():
	if platform.system()!='Windows':
		NotWindows()
	else:
		tkinter.messagebox.showinfo('Roblox OOF Restorer!', "This app currently doesn't support UWP (Universal Windows Platform) Roblox app.")

def RemoveRobloxStudioExistence():
	#C:\Users\Lenovo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Roblox
	StartMenuCatched=0
	DesktopCatched=0
	InstallerCatched=0
	MenuShortcut=f"C:/Users/{adminname}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Roblox/Roblox Studio.lnk"
	InstallerFile=f"C:/Users/{adminname}/AppData/Local/Roblox/Versions/RobloxStudioInstaller.exe"
	AppFile=f"C:/Users/{adminname}/AppData/Local/Roblox/Versions/RobloxStudioLauncher.exe"
	BetaFile=f"C:/Users/{adminname}/AppData/Local/Roblox/Versions/RobloxStudioLauncherBeta.exe"
	DesktopShortcut=f"C:/Users/{adminname}/Desktop/Roblox Studio.lnk"
	try:
		os.remove(MenuShortcut)
		StartMenuStatus="Success"
	except FileNotFoundError:
		StartMenuStatus="Shortcut not exist!"
		StartMenuCatched+=1
	except Exception:
		if StartMenuCatched==0:
			StartMenuStatus="Failed"
	try:
		os.remove(DesktopShortcut)
		DesktopStatus="Success"
	except FileNotFoundError:
		DesktopStatus="Shortcut not exist!"
		DesktopCatched+=1
	except Exception:
		if DesktopCatched==0:
			DesktopStatus="Failed"
	try:
		os.remove(InstallerFile)
		InstallerStatus="Success"
	except FileNotFoundError:
		try:
			os.remove(AppFile)
			InstallerStatus="Success"
		except FileNotFoundError:
			try:
				os.remove(BetaFile)
				InstallerStatus='Success'
			except FileNotFoundError:
				InstallerCatched+=1
				InstallerStatus="File not exist!"
	except Exception:
		if InstallerCatched==0:
			InstallerStatus="Failed"
	tkinter.messagebox.showinfo("Roblox OOF Restorer!",f"The removal process has been finished!\n\n- Start Menu shortcut: {StartMenuStatus}\n- Desktop shortcut: {DesktopStatus}\n- Installer file: {InstallerStatus}\n\nPress OK to continue!")
if __name__=="__main__":
	a=GetUpdate()
	print(a)