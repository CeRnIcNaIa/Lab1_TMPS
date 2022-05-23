from enum import Enum

class CocktailType(Enum):
    Mohito= 0,
    PinoColada = 1,
    Margarita = 2,
    BloodyMary = 3,
    Cosmopoliten = 4

class Cocktail:
    def __init__(self, ingridients: str):
        self.__ingridients = ingridients

    def get_ingridients(self) -> str:
        return self.__ingridients

class CocktailMohito(Cocktail):
    def __init__(self):
        super().__init__("mint, lime")

class CocktailPinoColada(Cocktail):
    def __init__(self):
        super().__init__("pineapple, coconut, cream")

class CocktailMargarita(Cocktail):
    def __init__(self):
        super().__init__("syrop, lime")

class CocktailBloodyMary(Cocktail):
    def __init__(self):
        super().__init__("tomato, lemon")

class CocktailCosmopoliten(Cocktail):
    def __init__(self):
        super().__init__("lime, orange, cranberry")    

def create_cocktail(cocktail_type: CocktailType) -> Cocktail:
    factory_dict = {
        CocktailType.Mohito: CocktailMohito,
        CocktailType.PinoColada: CocktailPinoColada,
        CocktailType.Margarita: CocktailMargarita,
        CocktailType.BloodyMary: CocktailBloodyMary,
        CocktailType.Cosmopoliten: CocktailCosmopoliten
    }
    return factory_dict[cocktail_type]()

if __name__ == '__main__':
    for cocktail in CocktailType:
        my_cocktail = create_cocktail(cocktail)
        print(f'Cocktail type: {cocktail} from {my_cocktail.get_ingridients()}')
