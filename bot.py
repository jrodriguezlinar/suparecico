# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import urllib
 
TOKEN = '214770447:AAHgnFcmFyP42jhcHiMO6zp6c4kX26--71I' # Nuestro tokken del bot (el que @BotFather nos dió).
usuarios = [line.rstrip('\n') for line in open('usuarios.txt')] # Cargamos la lista de usuarios.
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages):
    for m in messages:
        cid = m.chat.id
        if cid > 0:
            print str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre
        else:
            print str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre 
        bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.
#############################################
#Funciones
@bot.message_handler(commands=['roto2']) # Indicamos que lo siguiente va a controlar el comando '/roto2'.
def command_roto2(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_photo( cid, open( 'roto2.png', 'rb')) # Con la función 'send_photo()' del bot, enviamos al ID de la conversación que hemos almacenado previamente la foto de nuestro querido :roto2:

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if not str(cid) in usuarios: # Con esta sentencia, hacemos que solo se ejecute lo de abajo cuando un usuario hace uso del bot por primera vez.
        usuarios.append(str(cid)) # En caso de no estar en la lista de usuarios, lo añadimos.
        aux = open( 'usuarios.txt', 'a') # Y lo insertamos en el fichero 'usuarios.txt'
        aux.write( str(cid) + "\n")
        aux.close()
        bot.send_message( cid, "Bienvenido del primi!!!")
 
@bot.message_handler(commands=['laja']) # Indicamos que lo siguiente va a controlar el comando '/laja'
def command_laja(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'Persona non grata') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

@bot.message_handler(commands=['ruina']) # Indicamos que lo siguiente va a controlar el comando '/ruina'
def command_ruina(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    bot.send_message( cid, 'no ombe no!!') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
#############################################
#Peticiones

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.