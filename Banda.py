from functools import partial
from unicodedata import unidata_version
from apport.fileutils import core_dir
class Participante:
    def __init__(self, ficha,nombre, institu):
        self.__ficha = ficha
        self.__nombre = nombre
        self.__institu = institu

    def get_ficha(self):
        return self.__ficha
    def get_nombre(self):
        return self.__nombre
    def get_instuticion(self):
        return self.__institu

    def __str__(self): #devuelve un texto para pode imprimir
        return f"Ficha: {self.get_ficha()} | Banda: {self.get_nombre()} | Institución: {self.get_instuticion()}"

class BandaEscolar(Participante):
    def __init__(self,ficha, nombre, institu):
        super().__init__(ficha, nombre, institu)
        self.__categoria = ""
        self.__puntajes = {
            "ritmo":0,
            "uniformidad": 0,
            "coreografia":0,
            "alineacion": 0,
            "puntualidad":0
        } #Diccionario privado al que solo accede por su ficha
        self.total = 0
        self.promedio = 0
    def get_categoria(self):
        return self.__categoria
    def get_puntajes(self):
        return  self.__puntajes
    def set_puntajes(self, ritmo, uniformidad,coreografia, alineacion, puntualidad):
        self.__puntajes["ritmo"] = ritmo
        self.__puntajes["uniformidad"] = uniformidad
        self.__puntajes["coreografia"] = coreografia
        self.__puntajes["alineacion"] = alineacion
        self.__puntajes["puntualidad"]=puntualidad
        self.total = sum(self.__puntajes.values()) #Se calcula el total de puntos que obtuvo la banda
        self.promedio = self.total / len(self.__puntajes) #Promedio de puntos y este dato es el que ordena el ranking


    categorias_validas = ["PRIMARIA", "BASICO", "DIVERSIFICADO"] #Categorias validas
    criterios = ["Ritmo", "Uniformidad", "Coreografía", "Alineación", "Puntualidad"]

    def set_categoria(self, asignar_categoria ):
        if asignar_categoria.upper() in self.categorias_validas:
            self.__categoria = asignar_categoria.capitalize()
        else:
            print(" Se requiere una categoría válida: Primaria, Básico o Diversificado")

    def registrar_puntajes(self,ritmo, uniformidad, coreografia, alineacion, puntualidad):
        self.set_puntajes(ritmo, uniformidad, coreografia, alineacion, puntualidad)
        print('Registro actualizado')

    def __str__(self):
        return (
            f"Ficha: {self.get_ficha()} | "
            f"Banda: {self.get_nombre()} | "
            f"Institución: {self.get_instuticion()} | "
            f"Categoría: {self.get_categoria()} | "
            f"Total: {self.total} | Promedio: {self.promedio:.2f}"
            )

    def msotrar(self):
        puntajes_texto = ", ".join([f"{k.capitalize()}: {v}" for k, v in self.__puntajes.items()])
        return (
            f"Ficha: {self.get_ficha()} | Banda: {self.get_nombre()} | Categoría: {self.get_categoria()} | Total: {self.total} | Promedio: {self.promedio:.2f} "
            f"\nPuntajes: [{puntajes_texto}] | "
        )

def quicksort_descendente(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        mayores = [x for x in lista[1:] if x.promedio >= pivote.promedio]
        menores = [x for x in lista[1:] if x.promedio < pivote.promedio]
        return quicksort_descendente(mayores) + [pivote] + quicksort_descendente(menores)


class Concurso:

    def __init__(self):
        self.participantes = {} #Diccionario vacio de participantes
        self.cargar_bandas()
        self.cargar_puntajes()

    def cargar_bandas(self):
        try:
            with open("Bandas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split(",")
                    if len(partes) == 4:
                        ficha, nombre, instituto, categoria = partes
                        self.inscribir_banda(ficha, nombre, instituto, categoria)
                    else:
                        print(f"Línea mal formada: {linea}")
            print("Bandas cargadas correctamente")
        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print(f"Error al cargar bandas: {e}")

    def cargar_puntajes(self):
        try:
            with open("Puntajes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split(",")
                    if len(partes) == 6:
                        ficha = partes[0] #El Id es el primer dato
                        puntajes = list(map(int, partes[1:])) #Se elimina y los demas ya son puntajes
                        if ficha in self.participantes:
                            self.participantes[ficha].set_puntajes(*puntajes)
                        else:
                            print(f"Ficha no encontrada: {ficha}")
                    else:
                        print(f"Línea mal formada: {linea}")
            print("Puntajes cargados correctamente")
        except FileNotFoundError:
            print("Archivo de puntajes no encontrado")
        except Exception as e:
            print(f"Error al cargar puntajes: {e}")

    def guardar_puntajes(self):
        with open("Puntajes.txt", "w", encoding="utf-8") as archivo:
            for ficha, banda in self.participantes.items():
                p = banda.get_puntajes()
                linea = f"{ficha},{p['ritmo']},{p['uniformidad']},{p['coreografia']},{p['alineacion']},{p['puntualidad']}\n"
                archivo.write(linea)
        print("Puntajes guardados en archivo")

    def guardar_bandas(self):
        with open("Bandas.txt", "w", encoding="utf-8") as archivo:
            for banda in self.participantes.values():
                linea = f"{banda.get_ficha()},{banda.get_nombre()},{banda.get_instuticion()},{banda.get_categoria()}\n"
                archivo.write(linea)
        print("Bandas guardadas en archivo")

    def inscribir_banda(self, ficha, nombre, instituto, categoria):
        datos = [ficha, nombre, instituto, categoria]
        if not all(str(dato).strip()!="" for dato in datos):
           return False
        # Evitar fichas duplicadas
        if ficha in self.participantes:
            print("Ficha ya registrada")
            return False
        # Evitar nombres duplicados
        for banda in self.participantes.values():
            if banda.get_nombre().lower() == nombre.lower():
                print("Nombre de banda ya inscrito")
                return False

        nueva_banda = BandaEscolar(ficha, nombre, instituto)
        nueva_banda.set_categoria(categoria)
        self.participantes[ficha] = nueva_banda
        print("Banda inscrita con éxito")
        self.guardar_bandas() #Esto sirve para llamar al metodo y escribir las bandas inscritas
        return True

    def exitencia(self, ficha):
        if ficha in self.participantes:
            return True
        else:
            return False

    def nombre_banda(self, id):
        return self.participantes[id].get_nombre()

    def ranking(self):
        lista_banda = list(self.participantes.values())
        bandas_ordenadas_prom = quicksort_descendente(lista_banda)
        return bandas_ordenadas_prom #retorna el listado de bandas segun su promedio

