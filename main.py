from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

def acopiar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())


def apegar():
    editor.insert(INSERT, editor.clipboard_get())


def acortar():
    editor.clipboard_clear()

    editor.clipboard_append(editor.selection_get())

    editor.delete("sel.first", "sel.last")

def adeshacer():
    editor.edit_undo()


def arehacer():
    editor.edit_redo()


def anuevo():
    editor.delete(1.0,END)


def aabrir():
    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])
    if documento != None:
        editor.insert(1.0,documento.read())


def aguardar():
    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])
    print(documento.write(editor.get(1.0,END)))


def asalir():
    ventana.destroy()

def aacerca():
    messagebox.showinfo("Acerca del Bloc de Notas","Este bloc de notas es un lector de archivos de texto plano y es un proyecto," 


                                                    "que ayuda a practicar el uso de gui, manipulacion de archivos de texto y algunaas funciones extra")               



if __name__ == "__main__":
    ventana = Tk()

    menubar = Menu(ventana)

    archivo = Menu(menubar, tearoff=0)

    archivo.add_command(label="Nuevo ", command= anuevo)

    archivo.add_command(label="Abrir ", command= aabrir)

    archivo.add_command(label="Guardar ", command= aguardar)

    archivo.add_command(label="Salir ", command= asalir)
    
    menubar.add_cascade(label="Archivo", menu= archivo)


    editar = Menu(menubar, tearoff= 0)

    editar.add_command(label="Deshacer ", command= adeshacer)

    editar.add_command(label="Rehacer ", command= arehacer)
    
    editar.add_command(label="Copiar ", command= acopiar)

    editar.add_command(label="Pegar ", command= apegar)
    
    editar.add_command(label="Cortar ", command= acortar)
    
    

    menubar.add_cascade(label="Edicion", menu= editar)


    ayuda = Menu(menubar,tearoff=0)

    ayuda.add_command(label="Acerca del bloc de notas", command= aacerca)

    menubar.add_cascade(label="Ayuda", menu= ayuda)


    editor = Text(ventana, undo= True,font=("arial",11),height=195, width= 195)

    editor.pack()


    
    ventana.title("Bloc de Notas")
    
    ventana.geometry("695x424")
    ventana.config(menu=menubar)
    ventana.mainloop()
