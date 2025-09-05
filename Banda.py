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
    def __init__(self,ficha, nombre, institu,  puntajes):
        super().__init__(ficha, nombre, institu)
        self.__categoria = ""
        self.__puntajes = {} #Diccionario privado al que solo accede por su ficha
        self.total = 0
        self.promedio = 0

    categorias_validas = ["PRIMARIA", "BASICO", "DIVERSIFICADO"] #Categorias validas
    criterios = ["Ritmo", "Uniformidad", "Coreografía", "Alineación", "Puntualidad"]

    def set_categoria(self, asignar_categoria ):
        if asignar_categoria.upper() in self.categorias_validas:
            self.__categoria = asignar_categoria.capitalize()
        else:
            print(" Se requiere una categoría válida: Primaria, Básico o Diversificado")

    def registrar_puntajes(self):
        fin_registro =True
        while fin_registro:
            print()


