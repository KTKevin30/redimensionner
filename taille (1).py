from PIL import Image
import glob

SAVE_PATH = "/home/kevin/DATA/DATA_TAILLE/"
IMAGE_PATH = "/home/kevin/DATA/DATA_PNG/*.png"


nombre1=int(input("Entrez la largeur de l'image : "))

nombre2=int(input("Entrez la hauteur de l'image : "))

Dimension = (nombre1, nombre2)

def taille_to_change (path_to_image, save_path):

    #recuperation de l'image à redimensionner
    image = Image.open(path_to_image)
    
    #redimensionnement de l'image recupéré
    image = image.resize(Dimension,Image.ANTIALIAS)

    #recuperation du nom de l'image qui est censé etre à la suite du dernier slash d'ou le -1
    path_to_image = path_to_image.split('/')[-1]

    #stoker l'image redimensionner dans la variable SAVE_PATH qui est le chemin d'acces du dossier des fichier converti
    image.save(fp = SAVE_PATH+path_to_image)

    

#creation d'une liste contenant les chemins et noms des images à redimensionner
images = glob.glob(IMAGE_PATH)

#convertion de tous les elements de la liste
for image in images:
	
	#appel de la fonction pour convertir image par image
	taille_to_change (image, SAVE_PATH)