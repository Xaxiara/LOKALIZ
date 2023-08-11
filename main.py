import customtkinter as gui
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

gui.set_appearance_mode("dark")
gui.set_default_color_theme("dark-blue")

lokaliz =  gui.CTk
lokaliz.geometry("500x350")
print("Bienvenue sur LOKALIZ")

frame = gui.CTkFrame(master=lokaliz)
frame.pack(pady=25, padx=60, fill="both", expand=True)

label = gui.CTkLabel(master=frame, text="Entrez le numéro")
label.pack(pady=14, padx=12)

num = gui.CTkentry(master=frame, placeholder_text="+22900000000")
num.pack(pady=14)

#Trouver le pays du numéro
paysNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(paysNum, "fr")
print(localisation)

#Trouver l'opérrateur mobile
operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))

#Trouver les coordonnées GPS
cle = "9526960c7f1b41db925d5009cfdd657c"
coordonnees = OpenCageGeocode(cle)
requete = str(localisation)
reponse = coordonnees.geocode(requete)
lat = reponse[0]["geometry"]["latitude"]
lng = reponse[0]["geometry"]["longitude"]
print(lat, lng)

#Créaation du MAP
numMap = folium.map(localisation = [lat, lng], zoom_start=12)
folium.Marker([lat, lng], popup = localisation).add_to(numMap)
numMap.save("carte_numero_localiser.html")
lokaliz.mainLoop()