from email.mime import image
from msilib.schema import RadioButton
import PIL
from PIL import Image , ImageTk , ImageFilter , ImageEnhance
from tkinter import Button, IntVar, Radiobutton, Tk , Label, filedialog



def cargar():
        if opcion.get()==1:
         archivo= filedialog.askopenfilename()
         foto2= Image.open(archivo)
         render2=ImageTk.PhotoImage(foto2)
         reducida = foto2.resize((300,300), Image.Resampling.LANCZOS)
         render2= ImageTk.PhotoImage(reducida)
         label2.configure(image=render2)
         label2.image = render2
        if opcion.get()==2:
         archivo= filedialog.askopenfilename()
         foto2= Image.open(archivo)
         foto2=foto2.convert("L")
         render2=ImageTk.PhotoImage(foto2)
         reducida = foto2.resize((300,300), Image.Resampling.LANCZOS)
         render2= ImageTk.PhotoImage(reducida)
         label2.configure(image=render2)
         label2.image = render2
        if opcion.get()==3:
         archivo= filedialog.askopenfilename()
         foto2= Image.open(archivo)
         foto2=foto2.filter(ImageFilter.BLUR)
         render2=ImageTk.PhotoImage(foto2)
         reducida = foto2.resize((300,300), Image.Resampling.LANCZOS)
         render2= ImageTk.PhotoImage(reducida)
         label2.configure(image=render2)
         label2.image = render2
        if opcion.get()==4:
         archivo= filedialog.askopenfilename()
         foto2= Image.open(archivo)
         foto2=foto2.filter(ImageFilter.CONTOUR)
         render2=ImageTk.PhotoImage(foto2)
         reducida = foto2.resize((300,300), Image.Resampling.LANCZOS)
         render2= ImageTk.PhotoImage(reducida)
         label2.configure(image=render2)
         label2.image = render2
        if opcion.get()==5:
         archivo= filedialog.askopenfilename()
         foto2= Image.open(archivo)
         foto2=foto2.filter(ImageFilter.SHARPEN)
         render2=ImageTk.PhotoImage(foto2)
         reducida = foto2.resize((300,300), Image.Resampling.LANCZOS)
         render2= ImageTk.PhotoImage(reducida)
         label2.configure(image=render2)
         label2.image = render2
               
        


  
ventana = Tk()
ventana.geometry("500x500")
ventana.title("EDITOR DE FOTOS")


opcion = IntVar()
label2=Label(ventana)
label3=Label(ventana)
label4=Label(ventana, text="Selecciona una opción y luego carga la imagen:"  ,bg="pink")

boton2=Button(ventana,text="Cargar foto" ,bg="pink", command=cargar)
radio1=Radiobutton(ventana, text="Normal", value=1, variable=opcion )
radio2=Radiobutton(ventana, text="Blanco/negro", value=2, variable=opcion )
radio3=Radiobutton(ventana, text="Desenfocar", value=3, variable=opcion )
radio4=Radiobutton(ventana, text="Contorno", value=4, variable=opcion )
radio5=Radiobutton(ventana, text="Contraste", value=5, variable=opcion )


label2.place(x=10,y=40)
label3.place(x=10,y=40)
boton2.place(x=400,y=100)
radio1.place(y=400)
radio2.place(x=70,y=400)
radio3.place(x=160,y=400)
radio4.place(x=250,y=400)
radio5.place(x=330,y=400)
label4.place(x=5 , y=380)

ventana.mainloop()


