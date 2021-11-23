import json
# Estoy usando una clase como una interfaz
# Si no sabes que significa, no te preocupes :3
class InterfazJSON:
    def __init__(self, id):
        self.id = id
    def crear_JSON(self):
        """
        Este metodo regresa el json
        del objeto en cuestion.
        """
        return str(self.id) + ': ' + json.dumps(self.hacer_crear_JSON())
    
    def mostrar(self):
        for i in self.__dict__:
            print(f"{i}: {self.__dict__[i]}")
    
    # Metodos abstractos:

    def convertir_JSON(self, id, json):
        """
        Dado un id y un archivo tipo json,
        este metodo regresa un objeto del tipo
        correspondiente.
        """
        pass
    def hacer_crear_JSON(self):
        """
        Debe regresar un JSON del objeto correspondiente
        """
        pass