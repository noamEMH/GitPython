print("Bienvenue au zoo")
class Animal:
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("L'animal fait du bruit")
    def sePresenter(self):
        print(f"Je m'appelle {self.nom} et je suis {self.espece}")
    def voir(self):
        print(f"{self.nom} est là")
    def presenter(self):
        self.voir()
        print("Que voulez vous faire avec lui ? 1. Lire son panneaux de présentation ? 2. L'écouter ? 3. Passer au prochain")
        reponse = int(input("Répondez avec juste le chiffre"))
        for i in range(1):
            if reponse == 1:
                self.sePresenter()
            elif reponse == 2:
                self.faireDuBruit()
            elif reponse == 3:
                print("On passe au suivant")
            else:
                print("Vous avez mis un mauvais chiffre ! Dommage") 
class Amphibien(Animal):
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("*Croassement*")
    def voir(self):
        print(f"{self.nom} est dans sa mare")

class Actinoptérygien(Animal):
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("*Bruit d'eau*")
    def voir(self):
        print(f"{self.nom} est dans son aquarium")
        
class Reptile(Animal):
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("*Sifflement*")
    def voir(self):
        print(f"{self.nom} est dans son vivarium")

class Mammifère(Animal):
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("*Cri animal*")
    def voir(self):
        print(f"{self.nom} est dans son enclos")

class Oiseau(Animal):
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("*Chant d'oiseau*")
        def voir(self):
            print(f"{self.nom} est dans sa volière")

class Insecte(Animal):
    def __init__(self, nom, espece):
        self.nom = nom
        self.espece = espece
    def faireDuBruit(self):
        print("*Bruit d'insecte*")
        def voir(self):
            print(f"{self.nom} est dans son terrarium")

nemo = Actinoptérygien("Nemo", "un poisson clown")
dolly = Mammifère("Dolly", "une brebis")
goku = Mammifère("Goku", "un macaque rhésus")
shenron = Reptile("Shenron", "un dragon de komodo")
zephir = Mammifère("Zéphir", "un Pangolin à écailles de Temminck")
opaline = Oiseau("Opaline", "un Cacatoès à huppe souffrée")
solstice = Amphibien("Solstice", "un Salamandre tachetée")
brume = Actinoptérygien("Brume", "un Poisson-globe à taches noires")
celian = Mammifère("Célian", "un Tamarin Empereur")
lysandre = Insecte("Lysandre", "une mante orchidée")
naeva = Mammifère("Naeva", "une Paresseux à trois doigts de Hoffmann")
orion = Insecte("Orion", "un Scarabée rhinocéros géant")
thelio = Oiseau("Thélio", " une Pie-grièche écorcheur")
ysee = Mammifère("Ysée", "un chat pêcheur")
alois = Amphibien("Aloïs", " une grenouille tomate")
eleonore = Oiseau("Eléonore", "un Martin-pêcheur pie")
gaspard = Mammifère("Gaspard", "un Aye-Aye")
isaure = Amphibien("Isaure", "Axolotl")
leandre = Reptile("Léandre", "un Serpent corail faux-roi de Sinaloa")
maelis = Actinoptérygien("Maëlis", "un poisson-coffre jaune")
octave = Insecte("Octave", "un Phasme géant de Lord Howe")
romane = Oiseau("Romane", "une Chouette effraie")
silas = Mammifère("Silas", "un Babiroussa des Célèbes")
print("Commençons par le premier")
nemo.presenter()
dolly.presenter()
goku.presenter()
shenron.presenter()
zephir.presenter()
opaline.presenter()
solstice.presenter()
brume.presenter()
celian.presenter()
lysandre.presenter()
naeva.presenter()
orion.presenter()
thelio.presenter()
ysee.presenter()
alois.presenter()
eleonore.presenter()
gaspard.presenter()
isaure.presenter()
leandre.presenter()
maelis.presenter()
octave.presenter()
romane.presenter()
silas.presenter()