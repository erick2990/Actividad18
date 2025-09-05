import tkinter as tk
import Banda
class ConcursoBandasApp:


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")
        self.dinamica = Banda.Concurso()


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
        #opcion.set("Categorías") #Es el mensaje que se guarda en este boton de submenu
        listado = ["Primaria", "Básico", "Diversificado"] #Lista para el submenu
        menu_categoria = tk.OptionMenu(fondo_ins, opcion, *listado)
        menu_categoria.grid(row=4, column=10, padx=10, pady=5)
        criterios = ["Ritmo ", "Uniformidad", "Coreografía", "Alineación", "Puntualidad"]
        adicional = ", ".join(criterios)
        aviso_importante = tk.Label(fondo_ins,text=f"Categorias a calificar: \n{adicional}",bg="#000000", fg="#FFFF00", font=("Arial", 12, "bold"))
        aviso_importante.grid(row=5, column=10, padx=0, pady=5)

        def enviar_datos():
            ficha = ficha_entrada.get()
            nombre = nombre_entrada.get()
            instituto = instituto_entrada.get()
            ca  = opcion.get()
            if self.dinamica.inscribir_banda(ficha, nombre, instituto, ca):
                aviso_error.config(text="Datos guardados de forma exitosa")
                ficha_entrada.delete(0, tk.END)
                nombre_entrada.delete(0, tk.END)
                instituto_entrada.delete(0, tk.END)

            else:
                aviso_error.config(text="Verificar entradas")

        guardar = tk.Button(fondo_ins,text="Guardar", command=enviar_datos,bg="#D3D3D3", fg="#000000",  font=("Arial", 12, "bold"))
        guardar.grid(row=6, column=10, padx=10, pady=7)
        aviso_error = tk.Label(fondo_ins, text="Guardando", bg="#000000", fg="#FF0000", font=("Arial", 12, "bold"))
        aviso_error.grid(row=6, column=5, padx=10, pady=5)





    def registrar_evaluacion(self):


        print("Se abrió la ventana: Registrar Evaluación")
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registrar Evaluación")
        fondo_reg = tk.Frame(ventana_registro, bg="#000000", padx=100, pady=200)
        fondo_reg.pack()
        id_banda_texto = tk.Label(fondo_reg, text="Ingrese el ID de la banda: ", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
        id_banda_texto.grid(row=1, column=5, padx=10, pady=20, sticky="w" )
        id_banda_entrada = tk.Entry(fondo_reg)
        id_banda_entrada.grid(row=1, column=10, padx=10, pady=5)

        def buscar_evaluar():
            if self.dinamica.exitencia(id_banda_entrada.get()):
                fondo_reg.destroy() #Se destruye el frame donde se realizo la busqueda y se apertura uno nuevo en esta venta
                frame_puntos = tk.Frame(ventana_registro, bg="#000000", padx=100, pady=200)
                frame_puntos.pack()
                print('Ventana para ingresar los parametros y enviarlos')
                nota_texto = tk.Label(frame_puntos, text="Ingrese los datos", bg="#000000", fg="#D3D3D3", font=("Arial", 12, "bold"))
                nota_texto.grid(row=1, column=5, padx=20, pady=5)


            else:
                aviso_error.config(text="ID no encontrado")

        buscar = tk.Button(fondo_reg, text="Buscar", command=buscar_evaluar,font=("Arial", 12, "bold"), bg="#D3D3D3", fg="#000000")
        buscar.grid(row=2, column=10, padx=10, pady=10)
        aviso_error = tk.Label(fondo_reg, bg="#000000", fg="red", font=("Arial", 12, "bold"))
        aviso_error.grid(row = 2, column=5, padx=10, pady=20)



    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(self.ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.config(bg="black")
        fondo_lista = tk.Frame(ventana_listado, bg="#000000", padx=100, pady=200)
        fondo_lista.pack()
        cantidad_bandas =1
        for id, banda in self.dinamica.participantes.items():
            banda_tmp = tk.Label(fondo_lista, text=f"{banda}", bg="#000000", fg="#FFA500", font=("Arial", 12, "bold"), justify="left" )
            banda_tmp.grid(row=cantidad_bandas, column=0, padx=0, sticky="w")
            cantidad_bandas+=1



    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")
        fondo_ranking  = tk.Label(ventana_ranking, bg="#000000", padx=300, pady=300)
        fondo_ranking.pack()



if __name__ == "__main__":
    ConcursoBandasApp()
