import tkinter as tk
import Banda
from PIL import Image, ImageTk #importado desde la bach propio de python 3

class ConcursoBandasApp:


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x400")
        self.dinamica = Banda.Concurso()
        self.menu()

        imagen = Image.open("fondo.png")
        acomodar = imagen.resize((200, 100))
        self.imagen = ImageTk.PhotoImage(acomodar)
        fondo_grafico = tk.Label(self.ventana, image=self.imagen)
        fondo_grafico.pack(pady=10)

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Georgia", 12, "italic"),
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
        barra.add_cascade(label="OPCIONES", menu=opciones, font=("Arial", 12, "underline"))
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
        fondo_reg = tk.Frame(ventana_registro, bg="#000000", padx=10, pady=10)
        fondo_reg.pack()
        id_banda_texto = tk.Label(fondo_reg, text="Ingrese el ID de la banda: ", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
        id_banda_texto.grid(row=1, column=5, padx=10, pady=20, sticky="w" )
        id_banda_entrada = tk.Entry(fondo_reg)
        id_banda_entrada.grid(row=1, column=10, padx=10, pady=5)

        def buscar_evaluar():
            if self.dinamica.exitencia(id_banda_entrada.get()):
                ficha_banda = id_banda_entrada.get()  # guarda el numero de ficha
                punteos = [0,1,2,3,4,5,6,7,8,9,10]
                aviso_error.config(text="")

                print('Ventana para ingresar los parametros y enviarlos')
                nota_texto = tk.Label(fondo_reg, text=f"Ingrese los datos para {self.dinamica.nombre_banda(id_banda_entrada.get())}", bg="#000000", fg="#D3D3D3", font=("Arial", 12, "bold"))
                nota_texto.grid(row=3, column=0,sticky="w")
                ritmo_texto = tk.Label(fondo_reg, text="Ritmo", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
                ritmo_texto.grid(row=4, column=0,sticky="w")
                puntos_ritmo = tk.StringVar() #Retorna un tipo string pero se convierte a int cuando se envia
                listado_ritmo = tk.OptionMenu(fondo_reg, puntos_ritmo, *punteos)
                listado_ritmo.grid(row=4, column=8,sticky="e")
                uniformidad_texto = tk.Label(fondo_reg, text="Uniformidad", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
                uniformidad_texto.grid(row=5, column=0, sticky="w")
                puntos_unifomidad = tk.StringVar()#puntos de uniformidad
                listado_unif = tk.OptionMenu(fondo_reg, puntos_unifomidad, *punteos)
                listado_unif.grid(row=5, column=8, sticky="e")
                coreo_texto = tk.Label(fondo_reg, text="Coreografía", font=("Arial", 12,"bold"), bg="#000000", fg="#40E0D0")
                coreo_texto.grid(row=6, column=0, sticky="w")
                puntos_coreo = tk.StringVar() #Puntos por coreografia
                listado_coreo = tk.OptionMenu(fondo_reg, puntos_coreo, *punteos)
                listado_coreo.grid(row=6, column=8, sticky="e")
                ali_texto = tk.Label(fondo_reg, text="ALineación", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
                ali_texto.grid(row=7, column=0, sticky="w")
                puntos_alineacion = tk.StringVar()
                listado_ali = tk.OptionMenu(fondo_reg, puntos_alineacion, *punteos)
                listado_ali.grid(row=7, column=8, sticky="e")
                puntualidad_texto = tk.Label(fondo_reg, text="Puntualidad", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
                puntualidad_texto.grid(row=8, column=0, sticky="w")
                puntos_puntualidad = tk.StringVar()
                listado_puntualidad = tk.OptionMenu(fondo_reg, puntos_puntualidad, *punteos)
                listado_puntualidad.grid(row=8, column=8, sticky="e")

                def registrar_punteo():
                    ritmo = int(puntos_ritmo.get())
                    uniformidad = int(puntos_unifomidad.get())
                    coreografia = int(puntos_coreo.get())
                    alineacion = int(puntos_alineacion.get())
                    puntualidad = int(puntos_puntualidad.get())
                    self.dinamica.participantes[ficha_banda].set_puntajes(ritmo, uniformidad, coreografia, alineacion, puntualidad)
                    self.dinamica.guardar_puntajes()
                    print('Datos Guardados')
                    mensaje = tk.Label(fondo_reg, text="Datos Guardaos", font=("Arial", 12, "bold"), bg="#000000", fg="#00FF00")
                    mensaje.grid(row = 10, column=0, sticky="w")
                    #Despues de configurar los valores se cierra la ventana
                    def borrar():
                        id_banda_entrada.delete(0, tk.END)
                        puntos_ritmo.set("")
                        puntos_unifomidad.set("")
                        puntos_coreo.set("")
                        puntos_alineacion.set("")
                        puntos_puntualidad.set("")
                        nota_texto.config(text="")
                        mensaje.config(text="")

                    boton_limpiar = tk.Button(fondo_reg, text="Limpiar", command=borrar, font=("Arial", 12, "bold"))
                    boton_limpiar.grid(row=11, column=0, sticky="e")

                guardar = tk.Button(fondo_reg, text="GUARDAR", command = registrar_punteo,font=("Arial", 12, "bold"))
                guardar.grid(row=9, column=0,columnspan=9,pady=10)
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
        fondo_lista = tk.Frame(ventana_listado, bg="#000000", padx=10, pady=10)
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
        ventana_ranking.config(bg="black")
        frame_ranking  = tk.Frame(ventana_ranking, bg="#000000", padx=10, pady=10)
        frame_ranking.pack()
        fila =1
        for banda in self.dinamica.ranking():
            etiqueta_tmp = tk.Label(frame_ranking, text=f"{fila}. {banda}", font=("Arial", 12, "bold"), bg="#000000", fg="#40E0D0")
            etiqueta_tmp.grid(row=fila, column=5, sticky="w")
            fila +=1



if __name__ == "__main__":
    ConcursoBandasApp()
