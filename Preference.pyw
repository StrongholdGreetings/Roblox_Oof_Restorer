LaunchBySettings=False
import shutil,os,time,sys,platform,tkinter,requests,json,datetime,time,random
from tkinter import ttk
import AppFunction,FirstTimeSetup
#Define variable
appdir=os.getcwd()
version='v1.3'
oggfile=f'{appdir}/Data/Media/ouch.ogg'
icofile=f'{appdir}/Data/Media/icon.ico'
colordatafile=f'{appdir}/Data/ColorData.json'
op1=35
op2=95
op3=155
op4=215
op5=275

def RunRestoreNewOOF():
	AppFunction.mainfunc(1)

def run():
	try:	
		LaunchBySettings=True
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
		with open("Data/ColorData.json",'r') as f:
			colordata=json.load(f)
		with open("Data/UpdateData.json",'r') as f:
			updatedata=json.load(f)
		
		global tab1,tab2,tab3,tab4,modeaddchoice,modechoice,temp1,temp2,secondary_window,inlabel7,Label
		# Create secondary (or popup) window.
		#Window for Settings
		secondary_window = tkinter.Tk()
		tabcontrol=ttk.Notebook(secondary_window)
		secondary_window.title("Settings")

		def ExitSettings():
			ask=tkinter.messagebox.askyesno("Roblox OOF Restorer!",'You have to click "Apply" to apply any unsaved settings. Do you still want to quit?')
			if ask:
				try:
					secondary_window.destroy()
				except Exception:
					secondary_window.destroy()
		ThemeData=AppFunction.ApplySettings()
		# Changing tab color
		if AppFunction.OSRecognition()=='Windows':
			secondary_window.geometry('350x360')
		elif AppFunction.OSRecognition()=="Android":
			secondary_window.geometry('350x370')
		else:
			secondary_window.geometry('350x365')
		secondary_window.grab_set()
		tab1=ttk.Frame(tabcontrol)
		tab2=ttk.Frame(tabcontrol)
		tab3=ttk.Frame(tabcontrol)
		tab4=ttk.Frame(tabcontrol)
		tab5=ttk.Frame(tabcontrol)
		secondary_window.resizable(False,False)	
		try:
			secondary_window.iconbitmap(icofile)
		except tkinter.TclError:
			pass
		secondary_window.configure(bg=ThemeData["bgcolor"])
		secondary_window.protocol("WM_DELETE_WINDOW",ExitSettings)

		canvas1=tkinter.Canvas(tab1,width=325,height=225,scrollregion=(0,0,900,310),bg=ThemeData["bgcolor"])
		canvas2=tkinter.Canvas(tab2,width=325,height=225,scrollregion=(0,0,900,260),bg=ThemeData["bgcolor"])
		canvas3=tkinter.Canvas(tab3,width=325,height=225,scrollregion=(0,0,50,50),bg=ThemeData["bgcolor"])
		canvas4=tkinter.Canvas(tab4,width=325,height=225,scrollregion=(0,0,50,50),bg=ThemeData["bgcolor"])
		canvas5=tkinter.Canvas(tab5,width=325,height=225,scrollregion=(0,0,50,50),bg=ThemeData["bgcolor"])

		canvas1.grid(row=0, column=0)
		canvas2.grid(row=0, column=0)
		canvas3.grid(row=0, column=0)
		canvas4.grid(row=0, column=0)
		canvas5.grid(row=0, column=0)

		vsb1 = tkinter.Scrollbar(tab1, orient="vertical", command=canvas1.yview)
		vsb1.grid(row=0,column=1,sticky='ns')
		vsb2 = tkinter.Scrollbar(tab2, orient="vertical", command=canvas2.yview)
		vsb2.grid(row=0,column=1,sticky='ns')
		vsb3 = tkinter.Scrollbar(tab3, orient="vertical", command=canvas3.yview)
		vsb3.grid(row=0,column=1,sticky='ns')
		vsb4 = tkinter.Scrollbar(tab4, orient="vertical", command=canvas4.yview)
		vsb4.grid(row=0,column=1,sticky='ns')
		vsb5 = tkinter.Scrollbar(tab5, orient="vertical", command=canvas4.yview)
		vsb5.grid(row=0,column=1,sticky='ns')

		label=tkinter.Label(secondary_window)
		label.configure(text="SETTINGS",font=('Arial',15,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		label.grid(column=0,row=0)
		labelbl=tkinter.Label(secondary_window)
		labelbl.configure(text="Version 1.3",font=('Arial',7,'normal'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		labelbl.grid()
		
		canvas1.config(yscrollcommand=vsb1.set)
		canvas2.config(yscrollcommand=vsb2.set)
		canvas3.config(yscrollcommand=vsb3.set)
		canvas4.config(yscrollcommand=vsb4.set)
		canvas5.config(yscrollcommand=vsb5.set)

		tabcontrol.add(tab4, text='Roblox')
		tabcontrol.add(tab1, text='Restore')
		tabcontrol.add(tab2, text='UI')
		tabcontrol.add(tab3, text='Update')

		tabcontrol.grid()
		#Upate save file to apply settings	
		def SaveSettings():
			global tab1,tab2
			temp1=var.get()
			temp2=var1.get()
			temp3=var2.get()
			temp4=var3.get()
			temp5=var4.get()
			temp6=var5.get()
			if temp1==temp2:
				tkinter.messagebox.showerror("Error Occured!","Your button color must not be the same as text color")
			else:
				rep=tkinter.messagebox.askquestion("Roblox OOF Restorer!","Do you really want to apply settings?")
				if rep=='yes':
					write={"Text":temp1,"Button":temp2,"Theme":temp5}
					with open('Data/ColorData.json','w') as f:
						json.dump(write,f,indent=4)
					write={"NoAskUpdate":temp3,"CheckWhenStarts":temp4,"CheckRobloxWhenStarts":temp6}
					with open('Data/UpdateData.json','w') as f:
						json.dump(write,f,indent=4)
					tkinter.messagebox.showinfo('Roblox OOF Restorer!', "Changes successfully applied! Please restart the program to apply changes!")
					secondary_window.destroy()
		def Update():
			global currenttime,inlabel7
			try:
				response=requests.get("https://api.github.com/repos/StrongholdGreetings/Roblox_Oof_Restorer/releases/latest")
				currenttime=datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
				with open('Data/TXT/DownloadLog.txt','w') as f:
					f.write(currenttime)
				inlabel7.destroy()
				updatestring=f'Last Checked: {currenttime}'
				inlabel7=tkinter.Label(canvas3)
				inlabel7.configure(text=updatestring,font=('Arial',8),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
				canvas3.create_window(25,53,anchor='w',window=inlabel7)
				latest=response.json()["name"]
				if version==latest:
					tkinter.messagebox.showinfo("Roblox OOF Restorer!","Your app is already up to date. No need to update.")
				elif version>latest:
					randomness=random.randint(1,2)	
					tkinter.messagebox.showinfo("Roblox OOF Restorer!","Hi there! No need to worry about updates, since we are working on one (^_^)")
				else:
					updatebool='True'
					with open("Data/TXT/UpdateAvailable.temp",'w') as f:
						f.write(updatebool)
					if updatedata["NoAskUpdate"]=='Off':
						rep=tkinter.messagebox.askquestion("Roblox OOF Restorer!","Your app has a new update. Do you want to update?\nNote: After clicking 'Yes', you should not close the app until a message box shows up stating that your download has completed!")
					else:
						rep='yes'
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
			except requests.exceptions.RequestException:
				tkinter.messagebox.showerror("Error Occured!","Cannot check for updates! Check your connection to the web.")
		def CloseWindowAfterResetUI():
			if AppFunction.ResetColor()=='yes':
				secondary_window.destroy()
		# Option label
		#Tab1
		inlabel2=tkinter.Label(canvas1)
		inlabel2.configure(text="Restore Icon:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas1.create_window(25,op1,anchor='w',window=inlabel2)
		
		inlabel3=tkinter.Label(canvas1)
		inlabel3.configure(text="Download Old OOF:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas1.create_window(25,op2,anchor='w',window=inlabel3)

		inlabel14=tkinter.Label(canvas1)
		inlabel14.configure(text="Play Old OOF:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas1.create_window(25,op3,anchor='w',window=inlabel14)

		inlabel15=tkinter.Label(canvas1)
		inlabel15.configure(text="Revert to Ouch:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas1.create_window(25,op4,anchor='w',window=inlabel15)

		inlabel16=tkinter.Label(canvas1)
		inlabel16.configure(text="Rerun Setup:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas1.create_window(25,op5,anchor='w',window=inlabel16)
		#Tab 2
		inlabel1=tkinter.Label(canvas2)
		inlabel1.configure(text="Text Color:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas2.create_window(25,op1,anchor='w',window=inlabel1)
		inlabel5=tkinter.Label(canvas2)
		inlabel5.configure(text="Button:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas2.create_window(25,op2,anchor='w',window=inlabel5)

		inlabel10=tkinter.Label(canvas2)
		inlabel10.configure(text="Background Theme:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas2.create_window(25,152,anchor='w',window=inlabel10)

		inlabel12=tkinter.Label(canvas2)
		inlabel12.configure(text="Won't affect button color",font=('Tahoma',7),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas2.create_window(25,170,anchor='w',window=inlabel12)

		inlabel13=tkinter.Label(canvas2)
		inlabel13.configure(text="Reset to default:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas2.create_window(25,op4,anchor='w',window=inlabel13)
		#Tab 3
		inlabel6=tkinter.Label(canvas3)
		inlabel6.configure(text="Software Update:",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas3.create_window(25,op1,anchor='w',window=inlabel6)

		updatestring=f'Last Checked: {currenttime}'
		inlabel7=tkinter.Label(canvas3)
		inlabel7.configure(text=updatestring,font=('Tahoma',7),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas3.create_window(25,53,anchor='w',window=inlabel7)
		
		inlabel8=tkinter.Label(canvas3)
		inlabel8.configure(text='Update without asking:',font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas3.create_window(25,op2,anchor='w',window=inlabel8)
		inlabel9=tkinter.Label(canvas3)
		inlabel9.configure(text='Check when app starts:',font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas3.create_window(25,op3,anchor='w',window=inlabel9)

		#Tab 4
		inlabel11=tkinter.Label(canvas4)
		inlabel11.configure(text="Smart OOF Restorer",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas4.create_window(25,35,anchor='w',window=inlabel11)
		
		explain11=tkinter.Label(canvas4)
		explain11.configure(text="Auto-restore OOF if Roblox updates found",font=('Tahoma',7),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas4.create_window(25,50,anchor='w',window=explain11)
		
		inlabel17=tkinter.Label(canvas4)
		inlabel17.configure(text="Bye Roblox Studio Installer",font=('Arial',10,'bold'),fg=ThemeData["titlecolor"],bg=ThemeData["bgcolor"])
		canvas4.create_window(25,op2,anchor='w',window=inlabel17)

		innerbutton3=tkinter.Button(
			tab1, text="Restore",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=AppFunction.DownloadICO
		)
		innerbutton4=tkinter.Button(
			tab1, text="Download",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=AppFunction.DownloadOOF
		)

		innerbutton6=tkinter.Button(
			tab2, text="Restore",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=CloseWindowAfterResetUI
		)
		innerbutton7=tkinter.Button(
			tab1, text="Play",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=AppFunction.PlayOOF
		)

		innerbutton8=tkinter.Button(
			tab1, text="Restore",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=RunRestoreNewOOF
		)

		innerbutton9=tkinter.Button(
			tab1, text="Rerun",
			font=('Arial',9,'bold'),
			width=widthbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=FirstTimeSetup.Run
		)
		innerbutton075=tkinter.Button(
		secondary_window, text="Apply",
		font=('Arial',9,'bold'),
		width=40,
		height=2,
		bg=colordata["Button"],
		fg=colordata["Text"],
		command=SaveSettings
		)

		innerbutton5=tkinter.Button(
			tab3, text="Check",
			font=('Arial',9,'bold'),
			width=widthcheckbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=Update
		)
		innerbutton1=tkinter.Button(
			tab4, text="Remove",
			font=('Arial',9,'bold'),
			width=widthcheckbutton,
			height=1,
			bg=colordata["Button"],
			fg=colordata["Text"],
			command=AppFunction.RemoveRobloxStudioExistence
		)

		# Button place
		canvas1.create_window(310,op1,anchor='e',window=innerbutton3)
		canvas1.create_window(310,op2,anchor='e',window=innerbutton4)
		canvas1.create_window(310,op3,anchor='e',window=innerbutton7)
		canvas1.create_window(310,op4,anchor='e',window=innerbutton8)
		canvas1.create_window(310,op5,anchor='e',window=innerbutton9)
		canvas2.create_window(310,op4,anchor='e',window=innerbutton6)
		canvas3.create_window(310,op1,anchor='e',window=innerbutton5)
		canvas4.create_window(310,op2,anchor='e',window=innerbutton1)
		innerbutton075.place(relx=0.5,rely=0.925,anchor=tkinter.CENTER)

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

		var = tkinter.StringVar(canvas2)
		var.set(colordata["Text"])
		w=tkinter.OptionMenu(canvas2,var,*mode)
		w.configure(font=('Arial',9,'bold'),fg=colordata["Text"],bg=colordata["Button"])
		canvas2.create_window(310,op1,anchor='e',window=w)

		var1= tkinter.StringVar(canvas2)
		var1.set(colordata["Button"])
		w1=tkinter.OptionMenu(canvas2,var1,*mode1)
		w1.configure(font=('Arial',9,'bold'),fg=colordata["Text"],bg=colordata["Button"])
		canvas2.create_window(310,op2,anchor='e',window=w1)
		
		mode2=["Off","On"]
		var2= tkinter.StringVar(canvas3)
		var2.set(updatedata["NoAskUpdate"])
		w2=tkinter.OptionMenu(canvas3,var2,*mode2)
		w2.configure(font=('Arial',9,'bold'),fg=colordata["Text"],bg=colordata["Button"])
		canvas3.create_window(310,op2,anchor='e',window=w2)

		mode3=["Off","On"]
		var3=tkinter.StringVar(canvas3)
		var3.set(updatedata['CheckWhenStarts'])
		w3=tkinter.OptionMenu(canvas3,var3,*mode3)
		w3.configure(font=('Arial',9,'bold'),fg=colordata["Text"],bg=colordata["Button"])
		canvas3.create_window(310,op3,anchor='e',window=w3)

		mode4=["Light","Dark","Midnight"]
		var4=tkinter.StringVar(canvas2)
		var4.set(colordata['Theme'])
		w4=tkinter.OptionMenu(canvas2,var4,*mode4)
		w4.configure(font=('Arial',9,'bold'),fg=colordata["Text"],bg=colordata["Button"])
		canvas2.create_window(310,op3,anchor='e',window=w4)

		mode5=["Off","On"]
		var5=tkinter.StringVar(canvas3)
		var5.set(updatedata['CheckRobloxWhenStarts'])
		w5=tkinter.OptionMenu(canvas4,var5,*mode5)
		w5.configure(font=('Arial',9,'bold'),fg=colordata["Text"],bg=colordata["Button"])
		canvas4.create_window(310,op1,anchor='e',window=w5)
	except tkinter.TclError:
		secondary_window.destroy()
		tkinter.messagebox.showerror("Error","An instance of Settings is running!")
if __name__=="__main__":
	run()