#!/usr/bin/env python3

class Item():

    def __init__(self, id, peso, conflitos):
        self.id = id
        self.peso = int(peso)
        self.conflitos = conflitos
    
    def __str__(self):
        return f'ID: {self.id}  Peso: {self.peso} \nConflitos {self.conflitos} \n\n'

    def get_peso(self):
        return self.peso

    def get_id(self):
        return self.id

    def get_conflitos(self):
        return self.conflitos
                                                    