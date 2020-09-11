from tkinter import *
from tkinter import filedialog
#Put in Version(?), Offset(?), Mapping Points(?)


root = Tk()
root.geometry('500x500')
root.title("Auto Assign Widget")

cw=StringVar() #Copper Weight
pp=StringVar() #Prepreg
mt=StringVar() #Material
bdt=StringVar() #Board Thickness
al=StringVar() #Alignment
cln = IntVar() #Clean
aa = IntVar() #Auto-Assign
sk = IntVar() #Skyve 
skc = IntVar() #Skyve Clean 
os = StringVar() #Offsets

def printt():   #Print command
	cw1=cw.get()
	pp1=pp.get()
	mt1=mt.get()
	bdt1=bdt.get()
	al1=al.get()
	cln1=cln.get()
	aa1=aa.get()
	sk1=sk.get()
	skc1=skc.get()
	text="M48\n"+(f"Clean, {cln1}\n")+(f"Auto-Assign, {aa1}\n")+(f"Clean, {sk1}\n")+(f"Skyve-Clean, {skc1}\n")+(f"Cu, {cw1}\n")+(f"PP, {pp1}\n")+(f"Mat, {mt1}\n")+(f"Thk, {bdt1};0.1\n")+(f"Align. {al1}\n")+"%"
	return text
	

def exitt():  #Defining the exit fucntion for the exit button command
	exit()

def file_save():
    text = printt()    
    f = filedialog.askopenfilename(initialdir = "/C:/Python_Stuff/Master AA GUI",title = "Select File",filetypes = (("Excellon Files","*.ex2"),("All Files","*.*")))
    								#initialdir = directory it points to for ToolPath
    if f is None: 
        return
    with open(f, 'r') as original: data = original.read()
    with open(f, 'w') as modified: modified.write(text+"\n" + data)

def show():
	cln1=cln.get()
	aa1=aa.get()
	sk1=sk.get()
	skc1=skc.get()
	cw1=cw.get()
	pp1=pp.get()
	mt1=mt.get()
	bdt1=bdt.get()
	al1=al.get()
	#os1=os.get()
	myLabel = Label(root, text=(f"Clean, {cln1}")).grid(row=15, column=1)
	myLabel = Label(root, text=(f"Auto-Assign, {aa1}")).grid(row=16, column=1)
	myLabel = Label(root, text=(f"Skyve, {sk1}")).grid(row=17, column=1)
	myLabel = Label(root, text=(f"Skyve-Clean, {skc1}")).grid(row=18, column=1)
	myLabel = Label(root, text=(f"Copper Weight, {cw1}")).grid(row=19, column=1)
	myLabel = Label(root, text=(f"Pre-Preg, {pp1}")).grid(row=20, column=1)
	myLabel = Label(root, text=(f"Material, {mt1}")).grid(row=21, column=1)
	myLabel = Label(root, text=(f"Board Thickness, {bdt1};0.1")).grid(row=22, column=1)
	myLabel = Label(root, text=(f"Alignment Target, {al1}")).grid(row=23, column=1)
	#myLabel = Label(root, text=(f""))

label_0=Label(root, text="Schmoll Auto Assign Widget")
label_0.grid(row=2, column=1)


c =Checkbutton(root, text="Clean", variable=cln)
c.grid(row=4, column=1)
c =Checkbutton(root, text="Auto-Assign", variable=aa)
c.grid(row=4, column=2)
c =Checkbutton(root, text="Skyve", variable=sk)
c.grid(row=5, column=1)
c =Checkbutton(root, text="Skyve Clean", variable=skc)
c.grid(row=5, column=2)

list1=['Qoz', 'Toz', 'Hoz', '1oz']
droplist=OptionMenu(root, cw, *list1)
cw.set("Copper Weight")
droplist.config(width=15)
droplist.grid(row=4, column=0)

list2=['1x106', '1x1027', '1x1080', '1x1067']
droplist=OptionMenu(root, pp, *list2)
pp.set("Pre-Preg Style")
droplist.config(width=15)
droplist.grid(row=5, column=0)

list3=['370HR', 'MEG6', 'R6202', 'FR408']
droplist=OptionMenu(root, mt, *list3)
mt.set("Material Type")
droplist.config(width=15)
droplist.grid(row=6, column=0)

list4=['1mm', '2mm', '3mm', '4mm']
droplist=OptionMenu(root, al, *list4)
al.set("Alignment Target")
droplist.config(width=15)
droplist.grid(row=7, column=0)

#list5=['18x24 Top', '18x24 Bot', '12x18 Top', '12x18 Bot']
#droplist=OptionMenu(root, os, *list5)
#os.set("Offsets")
#droplist.config(width=15)
#droplist.grid(row=6, column=1)

label_1=Label(root, text='Board Thickness')
label_1.grid(row=8, column=0)
entry_1= Entry(root, textvar=bdt)
entry_1.grid(row=8, column=1)


but_quit = Button(root, text='Quit', command=exitt).grid(row=13, column=2)
but_SaveAs = Button(root, text = 'Export To', command=file_save).grid(row=13, column=0)
but_test = Button(root, text = 'Test', command=show).grid(row=13, column=1)

root.mainloop()
