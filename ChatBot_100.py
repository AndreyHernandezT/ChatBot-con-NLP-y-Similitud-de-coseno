import pymongo
import nltk
import random
import string
import warnings

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from passlib.hash import sha256_crypt
from tkinter import *
from pandastable import Table
from tkinter import messagebox as ms
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
from nltk.corpus import stopwords
import seaborn as sns
from pymongo import MongoClient

#Se ignoran los mensajes de advertencia
warnings.filterwarnings('ignore')

client = MongoClient('mongodb://localhost:27017/')

db = client['DataFrame']

#Se crea la colección Col_usu, en ella se ingresarán todos los usuarios (id's) con las contraseñas
col_usu = db['usuarios']
col_pregunta_sin_resp = db['pregunta_sin_resp']
col_pregunta_respuesta = db['pregunta_respuesta']


#Se conecta la base de datos al servidor
client = MongoClient('mongodb://localhost:27017/')

#Se crea la base de datos
database = client['ChatBot_DB']

col_respuestas = database['Datos']

col_Saludos = database['Saludos']



#Se buscan las respuestas de las colecciones
corpus_1 = col_respuestas.find_one({"id":"1"})["Respuesta_1"]
corpus_2 = col_respuestas.find_one({"id":"2"})["Respuesta_2"]
corpus_3 = col_respuestas.find_one({"id":"3"})["Respuesta_3"]
corpus_4 = col_respuestas.find_one({"id":"4"})["Respuesta_4"]
corpus_5 = col_respuestas.find_one({"id":"5"})["Respuesta_5"]
corpus_6 = col_respuestas.find_one({"id":"6"})["Respuesta_6"]
corpus_7 = col_respuestas.find_one({"id":"7"})["Respuesta_7"]
corpus_8 = col_respuestas.find_one({"id":"8"})["Respuesta_8"]
corpus_9 = col_respuestas.find_one({"id":"9"})["Respuesta_9"]
corpus_10 = col_respuestas.find_one({"id":"10"})["Respuesta_10"]
corpus_11 = col_respuestas.find_one({"id":"11"})["Respuesta_11"]
corpus_12 = col_respuestas.find_one({"id":"12"})["Respuesta_12"]
corpus_13 = col_respuestas.find_one({"id":"13"})["Respuesta_13"]
corpus_14 = col_respuestas.find_one({"id":"14"})["Respuesta_14"]
corpus_15 = col_respuestas.find_one({"id":"15"})["Respuesta_15"]
corpus_16 = col_respuestas.find_one({"id":"16"})["Respuesta_16"]
corpus_17 = col_respuestas.find_one({"id":"17"})["Respuesta_17"]
corpus_18 = col_respuestas.find_one({"id":"18"})["Respuesta_18"]
corpus_19 = col_respuestas.find_one({"id":"19"})["Respuesta_19"]
corpus_20 = col_respuestas.find_one({"id":"20"})["Respuesta_20"]
corpus_21 = col_respuestas.find_one({"id":"21"})["Respuesta_21"]
corpus_22 = col_respuestas.find_one({"id":"22"})["Respuesta_22"]
corpus_23 = col_respuestas.find_one({"id":"23"})["Respuesta_23"]
corpus_24 = col_respuestas.find_one({"id":"24"})["Respuesta_24"]
corpus_25 = col_respuestas.find_one({"id":"25"})["Respuesta_25"]
corpus_26 = col_respuestas.find_one({"id":"26"})["Respuesta_26"]
corpus_27 = col_respuestas.find_one({"id":"27"})["Respuesta_27"]
corpus_28 = col_respuestas.find_one({"id":"28"})["Respuesta_28"]
corpus_29 = col_respuestas.find_one({"id":"29"})["Respuesta_29"]
corpus_30 = col_respuestas.find_one({"id":"30"})["Respuesta_30"]
corpus_31 = col_respuestas.find_one({"id":"31"})["Respuesta_31"]
corpus_32 = col_respuestas.find_one({"id":"32"})["Respuesta_32"]
corpus_33 = col_respuestas.find_one({"id":"33"})["Respuesta_33"]
corpus_34 = col_respuestas.find_one({"id":"34"})["Respuesta_34"]
corpus_35 = col_respuestas.find_one({"id":"35"})["Respuesta_35"]
corpus_36 = col_respuestas.find_one({"id":"36"})["Respuesta_36"]
corpus_37 = col_respuestas.find_one({"id":"37"})["Respuesta_37"]
corpus_38 = col_respuestas.find_one({"id":"38"})["Respuesta_38"]
corpus_39 = col_respuestas.find_one({"id":"39"})["Respuesta_39"]
corpus_40 = col_respuestas.find_one({"id":"40"})["Respuesta_40"]
corpus_41 = col_respuestas.find_one({"id":"41"})["Respuesta_41"]
corpus_42 = col_respuestas.find_one({"id":"42"})["Respuesta_42"]
corpus_43 = col_respuestas.find_one({"id":"43"})["Respuesta_43"]
corpus_44 = col_respuestas.find_one({"id":"44"})["Respuesta_44"]
corpus_45 = col_respuestas.find_one({"id":"45"})["Respuesta_45"]
corpus_46 = col_respuestas.find_one({"id":"46"})["Respuesta_46"]
corpus_47 = col_respuestas.find_one({"id":"47"})["Respuesta_47"]
corpus_48 = col_respuestas.find_one({"id":"48"})["Respuesta_48"]
corpus_49 = col_respuestas.find_one({"id":"49"})["Respuesta_49"]
corpus_50 = col_respuestas.find_one({"id":"50"})["Respuesta_50"]
corpus_51 = col_respuestas.find_one({"id":"51"})["Respuesta_51"]
corpus_52 = col_respuestas.find_one({"id":"52"})["Respuesta_52"]
corpus_53 = col_respuestas.find_one({"id":"53"})["Respuesta_53"]
corpus_54 = col_respuestas.find_one({"id":"54"})["Respuesta_54"]
corpus_55 = col_respuestas.find_one({"id":"55"})["Respuesta_55"]
corpus_56 = col_respuestas.find_one({"id":"56"})["Respuesta_56"]
corpus_57 = col_respuestas.find_one({"id":"57"})["Respuesta_57"]
corpus_58 = col_respuestas.find_one({"id":"58"})["Respuesta_58"]
corpus_59 = col_respuestas.find_one({"id":"59"})["Respuesta_59"]
corpus_60 = col_respuestas.find_one({"id":"60"})["Respuesta_60"]
corpus_61 = col_respuestas.find_one({"id":"61"})["Respuesta_61"]
corpus_62 = col_respuestas.find_one({"id":"62"})["Respuesta_62"]
corpus_63 = col_respuestas.find_one({"id":"63"})["Respuesta_63"]
corpus_64 = col_respuestas.find_one({"id":"64"})["Respuesta_64"]
corpus_65 = col_respuestas.find_one({"id":"65"})["Respuesta_65"]
corpus_66 = col_respuestas.find_one({"id":"66"})["Respuesta_66"]
corpus_67 = col_respuestas.find_one({"id":"67"})["Respuesta_67"]
corpus_68 = col_respuestas.find_one({"id":"68"})["Respuesta_68"]
corpus_69 = col_respuestas.find_one({"id":"69"})["Respuesta_69"]
corpus_70 = col_respuestas.find_one({"id":"70"})["Respuesta_70"]

#Se concatenan las respuestas
texto = corpus_1 + corpus_2 +corpus_3 + corpus_4 + corpus_5 + corpus_6 + corpus_7 + corpus_8 + corpus_9 + corpus_10 + corpus_10 + corpus_11 + corpus_12 + corpus_13 + corpus_14 + corpus_15 + corpus_16 + corpus_17 + corpus_18 + corpus_19 + corpus_20 + corpus_21 + corpus_22 + corpus_23 + corpus_24 + corpus_25 + corpus_26 + corpus_27 + corpus_28 + corpus_29 + corpus_30 + corpus_31 + corpus_32 + corpus_33 + corpus_34 + corpus_35 + corpus_36 + corpus_37 + corpus_38 + corpus_39 + corpus_40 + corpus_41 + corpus_42 + corpus_43 + corpus_44 + corpus_45 + corpus_46 + corpus_47 + corpus_48 + corpus_49 + corpus_50 + corpus_51 + corpus_52 + corpus_53 + corpus_54 + corpus_55 + corpus_56 + corpus_57 + corpus_58 + corpus_59 + corpus_60 + corpus_61 + corpus_62 + corpus_63 + corpus_64 + corpus_65 + corpus_66 + corpus_67 + corpus_68 + corpus_69 + corpus_70
#print(texto)

#Tokenizando las colecciones de la base de datos
oraciones_token = nltk.sent_tokenize(texto)  #Se convierte en una lista de oraciones
print(oraciones_token)

#Se crea un diccionario (key/Signo de puntuacón:value/None) para remover los signos de puntiacion
remov_puntu = dict( ( ord(puntuacion), None) for puntuacion in string.punctuation) 

#Tansforma las vocales con tildes en palabras sin tildes
a = 'áéíóúüÁÉÍÓÚÜ'
b = 'aeiouuAEIOUU'
trans = str.maketrans(a,b)

##Imprime el diccionario
#print(remov_puntu)

#Se crea una función que devuelva una lista de palabras en minuscula. También las lematizamos después de eliminar los signos de puntuación 
def Lematizar(texto):
    return nltk.word_tokenize(texto.lower().translate(remov_puntu).translate(trans))
#print(Lematizar(texto))

'''
#Se ignoran las stop words
stop_words = set(stopwords.words("spanish"))
sin_stopword = []
words = Lematizar(texto) 
for word in words:
    if word  not in stop_words:
        sin_stopword.append(word)

nube_palabras = " ".join(sin_stopword)

###Se genera la nube de palabras, ignorando las que no son stop words
wordcloud = WordCloud(max_font_size=100, max_words= 100, background_color="white", width=800, height=400).generate(nube_palabras)
plt.figure(figsize=(18,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
'''

##Función para devolver saludos
def Saludo(pregunta):
    for palabra in pregunta.split(): # Hols buen dia 
        if palabra.lower() in col_Saludos.find_one({'id':'0'})["patrones"]:
            return random.choice(col_Saludos.find_one({'id':'0'})["respuestas"])


stopWords = set(stopwords.words('spanish'))
def RespuestaCh(pregunta_usuario):    
    global resp
    pregunta_usuario = pregunta_usuario.lower()


    #Se instancia la respuesta del chat
    respuesta_chat = ""
    #Se agrega la pregunta del usuario a la lista de oraciones
    oraciones_token.append(pregunta_usuario)
    #Se crea un objeto TfidfVectorizer 
    TfidfVec = TfidfVectorizer(tokenizer = Lematizar, stop_words = stopWords)   # [hola buen dia]   [Hola buena tarde]
    #Convierte el texto a una matriz TF-IDF
    tfidf = TfidfVec.fit_transform(oraciones_token)
    #Medidas de similitud 
    vals = cosine_similarity(tfidf[-1], tfidf)
    #Se obtiene el índice del texto / frase más similar a la respuesta de los usuarios
    idx = vals.argsort()[0][-2]
    #Se reduce la dimension de los valores 
    flat = vals.flatten()
    #Ordena la lista de manera mayor a menor
    flat.sort()
    #Se obtiene el mayor puntaje similitud 
    score = flat[-2]
    #Imprime el puntaje de similitud
    print(score)
    #Si la el puntaje de similitud es 0, significa que la entrada del usuario.
    if(score == 0):
        resp = "Lo siento, no pude entenderte bien.\nPor favor intentalo nuevamente, pero un poco más específico, ó visita nuestra página web: https://www.upb.edu.co/es/proyeccionsocial/evangelizacion."
        respuesta_chat = respuesta_chat+resp
        col_pregunta_sin_resp.insert_one({"pregunta_sin_resp":oraciones_token[-1]})
        #print(oraciones_token[-1])
    else:
        respuesta_chat = respuesta_chat+oraciones_token[idx]
        resp = respuesta_chat+oraciones_token[idx]   
    #print(robo_response)
    #Remueve la pregunta del usuario a la lista de oraciones
    oraciones_token.remove(pregunta_usuario)
    return respuesta_chat
'''
seguir = True
print("ANMI: Hola, me llamo AnMi, espero poder responder todas tus dudas.\nSi quieres salir escribe 'ADIOS'")

while seguir == True:
    pregunta_usuario = None
    pregunta_usuario  = input("Tú> ")
    pregunta_usuario = pregunta_usuario.lower()
    if pregunta_usuario != 'adios':
        if (Saludo(pregunta_usuario) != None):
            print("ANMI: "+Saludo(pregunta_usuario))
        else:
            print("ANMI: ",end="")
            print(RespuestaCh(pregunta_usuario))
    else:
        seguir = False
        print("Adios, ten un buen día")
    '''

    ############################################################################### GUI ########################################################

def registrarUsu():
    username_info = username.get()  # Maria
    password_info = password.get()  # 123
    gener_rad_info = gener_rad.get() # 2
    muni_comb_info = muni_comb.get() #FLo

    username_entradaReg.delete(0, END)
    password_entradaReg.delete(0, END)

    global password_encr 
    password_encr = sha256_crypt.encrypt(password_info) # $5$rounds=535000$phuDOa8PEx6lu.nb$YgrAnlbQhbm.zv3958B.6IRQCHz8uyctPowgG6pt7G5
    print(password_encr)

    if (username_info == " " or password_info == " "):
        ms.showerror("Error","No has completado")

    elif (username_info == "" or password_info == ""):
        ms.showerror("Error","No has completado")
    
    elif (len(username_info) < 6):
        ms.showerror("Error","El usuario debe tener al menos 6 caracteres")

    elif (gener_rad_info == 0):
        ms.showerror("Error","No has completado el género")

    elif (muni_comb_info == 0):
        ms.showerror("Error","No has completado")

    else:
        exist_user = col_usu.find_one({"username":username_info}) # Maria
        if exist_user:
            ms.showerror("Error","El usuario ya existe")
        else:
            if (gener_rad_info == 1):
                    gener_rad_info = "Hombre"
            elif (gener_rad_info == 2):
                    gener_rad_info = "Mujer"
            ms.showinfo("Información","La cuenta ha sido creada correctamente")
            col_usu.insert_one({"username":username_info, "password":password_encr, "genero":gener_rad_info, "municipio":muni_comb_info})
            


def LoginUsu():
    global usernameLog

    usernameLog = verificar_username.get()
    passwordLog = verificar_password.get()

    username_entradaLog.delete(0, END)
    password_entradaLog.delete(0, END)


    login_user = col_usu.find_one({"username":usernameLog}) # Mafe


    if login_user:
        password_encr2 = col_usu.find_one({"username":usernameLog})["password"]# $5$rounds=535000$phuDOa8PEx6lu.nb$YgrAnlbQhbm.zv3958B.6IRQCHz8uyctPowgG6pt7G5
        if (sha256_crypt.verify(passwordLog, password_encr2)):
            if usernameLog == "/admin":
                Entrada_admin()
            else:
                Entrada()
        else:
            ms.showerror("Error","Contraseña incorrecta")
    else:
        ms.showerror("Error", "Usuario incorrecto")    



def scRegistrar():
    global screenR
    screen.withdraw()
    screenR = Toplevel(screen)
    screenR.config(bg="#263b54")
    screenR.title("Registrar")
    screenR.geometry("500x600+20+20")


    global username
    global password
    global gener_rad
    global muni_comb

    global username_entradaReg
    global password_entradaReg

    username = StringVar()
    password = StringVar()
    gener_rad = IntVar()
    muni_comb = StringVar()
    list1 = ['Bucaramanga','Floridablanca','Piedecuesta','Socorro','Girón','San Gil']


    #image2 = PhotoImage(file="C:/Users/ANDREY/Desktop/Andrey/Universidad/Matemáticas Discretas II/Proyecto/logoUPB.gif")
    Label2 = Label(screenR, image=image, width=300, height=110,bg="#263b54")
    Label2.place(x=80,y=20)

    Label(screenR,text="Usuario:",font = ('freesansbold',20),padx=5,pady=5,fg="white",bg="#263b54").place(x=10,y=162)
    username_entradaReg = Entry(screenR, textvariable = username,bd=5,font=('calibri',15,'bold'))
    username_entradaReg.place(x=190,y=170)
    Label(screenR,text="Contraseña:",font = ('freesansbold',20),padx=5,pady=5,fg="white",bg="#263b54").place(x=10,y=222)
    password_entradaReg =  Entry(screenR, textvariable = password,bd=5,font=('calibri',15,'bold'),show="*")
    password_entradaReg.place(x=190,y=230)
    Label(screenR,text="Género:",font = ('freesansbold',20),padx=5,pady=5,fg="white",bg="#263b54").place(x=10,y=295)
    Radiobutton(screenR, text="Hombre",padx = 5, font = ('freesansbold',17), fg="white",bg="#263b54", variable=gener_rad, value=1, activebackground="#1c2e44").place(x=185,y=300)
    Radiobutton(screenR, text="Mujer",padx = 5, variable=gener_rad, value=2,font = ('freesansbold',17), fg="white",bg="#263b54").place(x=310,y=300)
    droplist=OptionMenu(screenR,muni_comb, *list1)
    droplist.config(width=20,font = ('freesansbold',12))
    Label(screenR,text="Municipio:",font = ('freesansbold',20),padx=5,pady=5,fg="white",bg="#263b54").place(x=10,y=350)
    muni_comb.set('Selecciona tu municipio') 
    droplist.place(x=190,y=360)
    Button(screenR,text=" Registrarme ",bd=7, font = ("monaco",15,"bold"),padx=5,pady=5,fg="#263b54", command = registrarUsu, activebackground="#1c2e44", activeforeground="#FFFFFF").place(x=255,y=500)
    Button(screenR,text="Inicia Sesión",bd=7, font = ("monaco",15,"bold"),padx=5,pady=5,fg="#263b54", command = lambda : [scLogin(),destruirScreenR()], activebackground="#1c2e44", activeforeground="#FFFFFF").place(x=30,y=500)

def scLogin():    
    global screenL
    screen.withdraw()
    screenL = Toplevel(screen)
    screenL.title("ingresar")
    screenL.config(bg="#263b54")
    screenL.geometry("500x500+20+20")
    Label(screenL)
    
    global verificar_username
    global verificar_password

    verificar_username = StringVar()
    verificar_password = StringVar()

    global username_entradaLog
    global password_entradaLog

    Label2 = Label(screenL, image=image, width=300, height=110,bg="#263b54")
    Label2.place(x=80,y=20)

    Label(screenL,text="Usuario:",font = ('freesansbold',20),padx=5,pady=5,fg="white",bg="#263b54").place(x=10,y=162)
    username_entradaLog = Entry(screenL, textvariable = verificar_username,bd=5,font=('calibri',15,'bold'))
    username_entradaLog.place(x=190,y=170)
    Label(screenL,text="Contraseña:",font = ('freesansbold',20),padx=5,pady=5,fg="white",bg="#263b54").place(x=10,y=222)
    password_entradaLog = Entry(screenL, textvariable = verificar_password,bd=5,font=('calibri',15,'bold'),show="*")
    password_entradaLog.place(x=190,y=230)
    Button(screenL,text=" Entrar ",bd=7, font = ("monaco",15,"bold"),padx=5,pady=5,fg="#263b54", command =  LoginUsu , activebackground="#1c2e44", activeforeground="#FFFFFF").place(x=255,y=400)
    Button(screenL,text=" Registrarse ",bd=7, font = ("monaco",15,"bold"),padx=5,pady=5,fg="#263b54", command = lambda : [scRegistrar(),destruirScreenL()], activebackground="#1c2e44", activeforeground="#FFFFFF").place(x=30,y=400)

def enviar():
    global calif_rad_info
    calif_rad_info = calif_rad.get()
    col_pregunta_respuesta.insert_one({"usuario": usernameLog,"pregunta":pregunta_usuario,"respuesta":resp,"calificacion":calif_rad_info})



def validar():
    ChatBot()

def destruirScreen():
    screen.destroy()
def destruirScreenC():
    screenC.destroy()
def destruirScreenR():
    screenR.destroy()
def destruirScreenL():
    screenL.destroy()
def destruirScreenE():
    screenE.destroy()
def destruirScreenEA():
    screenEA.destroy()


def calificar():
    if(resp != "Lo siento, no pude entenderte bien.\nPor favor intentalo nuevamente, pero un poco más específico, ó visita nuestra página web: https://www.upb.edu.co/es/proyeccionsocial/evangelizacion." or resp=="" or resp==" "):
        global screenC
        screenC = Toplevel(window)
        screenC.config(bg="#263b54")
        screenC.title("Calificar")
        screenC.geometry("300x107")

        global calif_rad

        calif_rad = IntVar()

        Label(screenC, text = "Califica la respuesta" , font =  ("monaco",13,"bold"),fg="white",bg="#263b54").place(x=52,y=0)
        Radiobutton(screenC, text="1",padx = 10, font = ('freesansbold',10), fg="white",bg="#263b54", variable=calif_rad, value=1).place(x=20,y=30)
        Radiobutton(screenC, text="2",padx = 10, variable=calif_rad, value=2,font = ('freesansbold',10), fg="white",bg="#263b54").place(x=70,y=30)
        Radiobutton(screenC, text="3",padx = 10, variable=calif_rad, value=3,font = ('freesansbold',10), fg="white",bg="#263b54").place(x=120,y=30)
        Radiobutton(screenC, text="4",padx = 10, variable=calif_rad, value=4,font = ('freesansbold',10), fg="white",bg="#263b54").place(x=170,y=30)
        Radiobutton(screenC, text="5",padx = 10, variable=calif_rad, value=5,font = ('freesansbold',10), fg="white",bg="#263b54").place(x=220,y=30)
        Button(screenC,text=" Enviar ",bd=7, font = ("monaco",10,"bold"),padx=3,pady=3,fg="#263b54", command = lambda : [enviar(), destruirScreenC()], activeforeground="#1c2e44").place(x=98,y=55)
    else:
        pass


def Entrada():
    global screenE
    screenL.withdraw()
    screenE = Toplevel(screen)
    screenE.config(bg="#263b54")
    screenE.title("Entrada")
    screenE.geometry("500x300")

    label1 = tk.Label(screenE, text="Bienvenid@", bg="dark turquoise",font = ("Lanksaman",17))
    label1.pack(fill=tk.X, padx=5,pady=5,ipadx=5, ipady=5)
    #label1.place(x=7,y=7)
    Label(screenE, text = usernameLog , font = ('freesansbold',33),fg="white",bg="#263b54").place(x=180,y=50)
    Button(screenE,text="  ChatBot ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = lambda : [destruirScreen(), validar()], activeforeground="#1c2e44").place(x=75,y=163)
    Button(screenE,text=" Cerrar\n Sesión ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = lambda : [destruirScreenE(), scLogin()], activeforeground="#1c2e44").place(x=295,y=150)


def Entrada_admin():
    global screenEA
    screenL.withdraw()
    screenEA = Toplevel(screen)
    screenEA.config(bg="#263b54")
    screenEA.title("Entrada")
    screenEA.geometry("500x300")

    label1 = tk.Label(screenEA, text="Bienvenido", bg="dark turquoise",font = ("Lanksaman",17))
    label1.pack(fill=tk.X, padx=5,pady=5,ipadx=5, ipady=5)
    #label1.place(x=7,y=7)
    Label(screenEA, text = "Administrador" , font = ('freesansbold',33),fg="white",bg="#263b54").place(x=130,y=50)
    Button(screenEA,text=" ChatBot ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = lambda : [destruirScreen(), validar()], activeforeground="#1c2e44").place(x=75,y=133)
    Button(screenEA,text=" Cerrar\n Sesión ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = lambda : [destruirScreenEA(), scLogin()], activeforeground="#1c2e44").place(x=295,y=120)
    Button(screenEA,text=" Estadísticos ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = Estadisticos, activeforeground="#1c2e44").place(x=160,y=230)


def Estadisticos():
	global screenEst
	screenEst = Toplevel(screen)
	screenEst.config(bg="#263b54")
	screenEst.title("Entrada")
	screenEst.geometry("470x330")
	
	Button(screenEst,text="Estadísticos\nUsuarios",bd=7, font = ("monaco",13,"bold"),padx=4,pady=4,fg="#263b54", command = EstadisticosUsu, activeforeground="#1c2e44").place(x=145,y=30)
	Button(screenEst,text="Estadísticos\nPreguntas Respuesta",bd=7, font = ("monaco",13,"bold"),padx=4,pady=4,fg="#263b54", command = EstadisticosPregRes, activeforeground="#1c2e44").place(x=110,y=130)
	Button(screenEst,text="Estadísticos\nPreguntas Sin Respuesta",bd=7, font = ("monaco",13,"bold"),padx=4,pady=4,fg="#263b54", command = EstadisticosPregSinRes, activeforeground="#1c2e44").place(x=100,y=230)

######
##### Estádisticos usuarios
def EstadisticosUsu():
	global root2
	#screenEA.withdraw()
	root2 = Toplevel(screen)
	root2.title('PandasTable Example')
	root2.geometry('900x500')

	global dataU
	dataU = pd.DataFrame(list(col_usu.find()))
	dataU = pd.DataFrame(dataU)
	del dataU['_id']
	dataU = dataU[dataU['municipio'].notna()]

	frame = tk.Frame(root2)
	frame.pack(fill='both', expand=True)
	pt = Table(frame, dataframe=dataU)
	pt.show()
	buttonMuni = tk.Button(root2, text='Usuarios\nPor Municipio',bd=7, font = ("monaco",10,"bold"),padx=4,pady=4,fg="#263b54",  command = GraficaUsu_Municipio,activeforeground="#1c2e44")
	buttonGene = tk.Button(root2, text='Usuarios\nPor Género',bd=7, font = ("monaco",10,"bold"),padx=4,pady=4,fg="#263b54",  command = GraficaUsu_Genero,activeforeground="#1c2e44")
	buttonMuni.place(x=200,y=400)
	buttonGene.place(x=600,y=400)

## Gráfica usuarios-municipios
def GraficaUsu_Municipio():
  plt.figure(figsize=(9,3))
  sns.barplot(x=dataU['municipio'].value_counts().index,y=dataU['municipio'].value_counts())
  plt.xlabel('Municipios')
  plt.ylabel('Numero de usuarios')
  plt.title('Numero de usuarios por municipios')
  plt.show()

## Gráfica usuarios-géneros
def GraficaUsu_Genero():
  plt.figure(figsize=(9,3))
  sns.barplot(x=dataU['genero'].value_counts().index,y=dataU['genero'].value_counts())
  plt.xlabel('Generos')
  plt.ylabel('Numero de usuarios')
  plt.title('Numero de usuarios por género')
  plt.show()

######
### Estadísticos preguntas con Respuesta
def EstadisticosPregRes():
	global root
	#screenEA.withdraw()
	root = Toplevel(screen)
	root.title('PandasTable Example')
	root.geometry('900x400')

	global dataPreg
	dataPreg = pd.DataFrame(list(col_pregunta_respuesta.find()))
	dataPreg = pd.DataFrame(dataPreg)
	del dataPreg['_id']
	print(dataPreg.isnull().sum())

	dataPreg = dataPreg[dataPreg['calificacion'].notna()]

	frame = tk.Frame(root)
	frame.pack(fill='both', expand=True)
	pt = Table(frame, dataframe=dataPreg)
	pt.show()
	buttonCali = tk.Button(root, text='Preguntas\nPor calificación',bd=7, font = ("monaco",10,"bold"),padx=4,pady=4,fg="#263b54",  command = GraficaPreg_Calif,activeforeground="#1c2e44")
	buttonCali.place(x=30,y=342)
	buttonUsu = tk.Button(root, text='NPQRS\nPor Usuario',bd=7, font = ("monaco",10,"bold"),padx=4,pady=4,fg="#263b54",  command = GraficaPreg_Usu,activeforeground="#1c2e44")
	buttonUsu.pack()
	buttonEs = tk.Button(root, text='Frecuencia\nCalificación',bd=7, font = ("monaco",10,"bold"),padx=4,pady=4,fg="#263b54",  command = GraficaPreg_FrecEs,activeforeground="#1c2e44")
	buttonEs.place(x=720,y=342)

## Gráfica pregunta-calificación
def GraficaPreg_Calif():
  dataPreg.groupby('pregunta')['calificacion'].sum().plot(kind='bar')
  plt.xlabel('Pregunta')
  plt.ylabel('Calificacion')
  plt.show()

## Gráfica preguta por usuarios
def GraficaPreg_Usu():
  plt.figure(figsize=(8,3))
  sns.barplot(x=dataPreg['usuario'].value_counts().index,y=dataPreg['usuario'].value_counts())
  plt.xlabel('Usuarios')
  plt.ylabel('N° PQRS')
  plt.title('N° PQRS por usuario')
  plt.show()

## Gráfica Frecuencia estrellas
def GraficaPreg_FrecEs():
	plt.figure(figsize=(8,3))
	sns.barplot(x=dataPreg['calificacion'].value_counts().index,y=dataPreg['calificacion'].value_counts())
	plt.xlabel('Calificación')
	plt.ylabel('Frecuencia')
	plt.title('Calificación estrellas por Frecuencia')
	plt.show()


def EstadisticosPregSinRes():
	global root
	#screenEA.withdraw()
	root = Toplevel(screen)
	root.title('PandasTable Example')
	root.geometry('900x400')

	global dataPregSR
	dataPregSR = pd.DataFrame(list(col_pregunta_sin_resp.find()))
	dataPregSR = pd.DataFrame(dataPregSR)
	del dataPregSR['_id']

	frame = tk.Frame(root)
	frame.pack(fill='both', expand=True)
	pt = Table(frame, dataframe=dataPregSR)
	pt.show()
	buttonCali = tk.Button(root, text='Preguntas\nPor calificación',bd=7, font = ("monaco",10,"bold"),padx=4,pady=4,fg="#263b54",  command = GraficaPregSR,activeforeground="#1c2e44")
	buttonCali.pack()

## Gráfica Frecuencia estrellas
def GraficaPregSR():
	plt.figure(figsize=(8,3))
	sns.barplot(x=dataPregSR['pregunta_sin_resp'].value_counts().index,y=dataPregSR['pregunta_sin_resp'].value_counts())
	plt.xlabel('Pregunta')
	plt.ylabel('Frecuencia')
	plt.title('Calificación estrellas por Frecuencia')
	plt.show()


def Imprimir(mw,st,imsg):
    global pregunta_usuario
    message_send_by_bot=''
    pregunta_usuario=''
    if(imsg.get().strip()==''):
        pass
    else:
        pregunta_usuario = imsg.get()
        pregunta_usuario = pregunta_usuario.lower()
        if (Saludo(pregunta_usuario) != None):
            message_send_by_bot='AnMi >>   '+Saludo(pregunta_usuario)+'\n\n' 
        else:
            message_send_by_bot='AnMi >>   '+RespuestaCh(pregunta_usuario)+'\n\n'

        pregunta_usuario_print ='Tú >>   '+imsg.get()+'\n'
        mw.config(state='normal')
        mw.insert('end',pregunta_usuario_print)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')



def ChatBot():
    global window
    window = Tk()

    input_message=tk.StringVar(window)
    input_message.set("")
#

    window.bind('<Return>',lambda x: [Imprimir(message_window,input_entry,input_message), calificar()])
    window.title('AI Chatbot')
    window.geometry('600x600+15+15')
    window.config(bg="#0099FF")

    fram2 = tk.Frame(height=400, width=100, bg='#263b54', bd=10)
    fram3 = tk.Frame(height=80, width=100, bg='#263b54', bd=10)

    #Entrada
    input_entry=tk.Entry(fram3,width=10, bg='#CCCCCC', font="Times 12", bd=1, justify=LEFT, textvariable=input_message)
    input_entry.pack(fill=X, padx=6, pady=6, ipady=3)
    
    #Texto
    message_window=tk.Text(fram2,bg='#CCCCCC',yscrollcommand='YES', font="Times 12")
    message_window.insert('end','ChatBot:        '+'Hola, me llamo AnMi, espero poder responder todas tus dudas\n\n')
    message_window.config(state='disabled')
    message_window.pack(side='top',expand='YES',fill='both')
#
    send_button = tk.Button(fram3,text=' Enviar ', width=5, relief=GROOVE, height=2, bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF", command = lambda : [Imprimir(message_window,input_entry,input_message), calificar()] )
    send_button.pack(fill =BOTH)

    fram2.pack(fill='both', expand='YES')
    fram3.pack(fill='x', side='bottom')
    #window.mainloop()
#ChatBot()



def main_screen():
    global screen
    screen =tk.Tk()
    screen.geometry("520x300+15+15")
    screen.config(bg="#263b54")
    
    global image  

    image = PhotoImage(file="C:/Users/ANDREY/Desktop/Andrey/Universidad/Matemáticas Discretas II/Proyecto/logoUPB.gif")
    Label1 = Label(screen, image=image, width=300, height=110,bg="#263b54")
    Label1.place(x=100,y=20)

    
    Button(text=" Iniciar Sesión ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = scLogin, activeforeground="#1c2e44").place(x=45,y=200)
    Button(text=" Registrarse ",bd=7, font = ("monaco",15,"bold"),padx=4,pady=4,fg="#263b54", command = scRegistrar, activeforeground="#1c2e44").place(x=300,y=200)
   
    screen.mainloop()
main_screen()