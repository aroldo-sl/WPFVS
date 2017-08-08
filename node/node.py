import socket
import sys
import os
import signal
import re
import array
import scraper #Scraper Klasse die es mit dem Arbeitspaket vorzubereiten gilt

distributor_ip = "192.168.56.102" #IP des Verteilers
distributor_port = 45678          #Port des Verteilprozesses

#Verbindung zum Verteiler aufbauen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((distributor_ip, distributor_port))

#Schleife 
while True:
    #Empfang des Arbeitsauftrags abhaengig vom Distributor aendern
    sig = s.recv()
    #WeckSignal empfangen
    if isinstance(sig, int):
        #Dem Verteiler die eigene IP und Portnummer senden
        s.send(s.getsockname()[0])
    #Wenn das Empfangene kein Integer Wert ist muss es das Arbetispaket sein
    else:
        """
        Dieser Teil muss noch komplett an die Scraper Klasse angepasst werden
        """
        #Scraper vorbereiten
        #Urls aus dem Arbeitspaket uebergeben
        scraper.setStartUrls(sig[0])
        #User Agent setzen
        scraper.setUserAgent(sig[1])
        #Scraper starten
        scraper.startScraper()
