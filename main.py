import tkinter as tk

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)
      
        self.ventana.mainloop()

    def menu(self):

        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        ventana_inscribir = tk.Toplevel(self.ventana)
        ventana_inscribir.title("Inscribir Banda")#esta ventana es la secundaria sobre la cual se trabaja
        fondo_ins = tk.Label(ventana_inscribir, bg="#000000", padx=300, pady=300)
        fondo_ins.pack()
        ficha_text = tk.Label(fondo_ins, text="Ficha: ", bg="#000000" , fg="#40E0D0", font=("Arial", 14, "bold"))
        ficha_text.grid(row = 1, column= 5, padx=10, pady=20, sticky="w")
        ficha_entrada = tk.Entry(fondo_ins) #Guarda
        ficha_entrada.grid(row = 1, column = 10, padx=10, pady=5)
        nombre_text = tk.Label(fondo_ins, text="Nombre: ", bg="#000000" , fg="#40E0D0", font=("Arial", 14, "bold"))
        nombre_text.grid(row=2, column=5, padx=10, pady=20, sticky="w")
        nombre_entrada = tk.Entry(fondo_ins) #Guarda
        nombre_entrada.grid(row=2, column=10, padx=10, pady=5)
        instituto_text = tk.Label(fondo_ins, text="Instituto: ", bg="#000000", fg="#40E0D0", font=("Arial", 14, "bold"))
        instituto_text.grid(row=3, column=5, padx=10, pady=20, sticky="w")
        instituto_entrada = tk.Entry(fondo_ins)  # Guarda
        instituto_entrada.grid(row=3, column=10, padx=10, pady=5)
        categoria_text = tk.Label(fondo_ins, text="Seleccione la categoria: ",bg="#000000" , fg="#40E0D0", font=("Arial", 14, "bold"))
        categoria_text.grid(row=4, column=5, padx=10, pady=5)
        opcion = tk.StringVar() #la categoria se guardara en esta variable con el metodo get
        opcion.set("Categorías") #Es el mensaje que se guarda en este boton de submenu
        listado = ["Primaria", "Básico", "Diversificado"] #Lista para el submenu
        menu_categoria = tk.OptionMenu(fondo_ins, opcion, *listado)
        menu_categoria.grid(row=4, column=10, padx=10, pady=5)
        criterios = ["Ritmo ", "Uniformidad", "Coreografía", "Alineación", "Puntualidad"]
        adicional = ", ".join(criterios)
        aviso_importante = tk.Label(fondo_ins,text=f"Categorias a calificar: \n{adicional}",bg="#000000", fg="#FFFF00", font=("Arial", 12, "bold"))
        aviso_importante.grid(row=5, column=10, padx=0, pady=5)
        guardar = tk.Button(fondo_ins,text="Guardar",bg="#D3D3D3", fg="#000000",  font=("Arial", 12, "bold"),)
        guardar.grid(row=6, column=10, padx=10, pady=7)
        aviso_error = tk.Label(fondo_ins, text="Guardando", bg="#000000", fg="#FF0000", font=("Arial", 12, "bold"))
        aviso_error.grid(row=6, column=5, padx=10, pady=5)



    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registrar Evaluación")
        fondo_reg = tk.Label(ventana_registro, bg="#000000", padx=300, pady=300)
        fondo_reg.pack()
        id_banda_texto = tk.Label(fondo_reg, text="Ingrese el ID de la banda: ", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
        id_banda_texto.grid(row=1, column=5, padx=10, pady=20, sticky="w" )
        id_banda_entrada = tk.Entry(fondo_reg)
        id_banda_entrada.grid(row=1, column=10, padx=10, pady=5)
        buscar = tk.Button(fondo_reg, text="Buscar", font=("Arial", 12, "bold"), bg="#D3D3D3", fg="#000000" )
        buscar.grid(row=2, column=10, padx=10, pady=10)
        #por medio del boton se ejecutara un metodo propio de una clase del archivo banda donde retorne True o false
        x=3
        if x>5:
            print('Si el codigo esta bien entonces procede a todo esto')

        else:
            error_aviso = tk.Label(fondo_reg, text="No hay registros intente nuevamente", font=("Arial", 12, "bold"), bg="#000000", fg="#FF0000")
            error_aviso.grid(row=2, column=5, padx=5, pady=20)
            id_banda_entrada.delete(0, tk.END)




    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(self.ventana)
        ventana_listado.title("Listado de Bandas")
        fondo_lista = tk.Label(ventana_listado, bg="#000000", padx=300, pady=300)
        fondo_lista.pack()

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")
        fondo_ranking  = tk.Label(ventana_ranking, bg="#000000", padx=300, pady=300)
        fondo_ranking.pack()



if __name__ == "__main__":
    ConcursoBandasApp()
