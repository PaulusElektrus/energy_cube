# Energiewürfel

## Masterarbeit Smart-Home Batteriespeicher für Balkonkraftwerke

- ### Architektur

    Es wird ein Kombiboard aus einem Arduino Uno und einem ESP8266 benutzt

    - Arduino (Arduino_Code)

        Der Arduino übernimmt die Steuerung der Hardware

    - ESP8266 (ESP_code)

        Der ESP8266 mit seinem W-LAN Modul übernimmt die Kommunikation mit dem Internet

- ### Kommunikation

    Die Kommunikation zwischen den Mikrocontrollern erfolgt über UART. 

    Ein Screenshot des Logic Analyzers welchen ich zur Überwachung der Kommunikation benutze:

    ![Screenshot](Arduino_ESP_Communication.png)

    Man erkennt in den < > geschweiften Klammern die jeweils übertragene Nachricht und danach als Empfangsbestätigung, Debug und zu Demonstrationszwecken die Ausgabe des jeweiligen Mikrocontrollers in schönem Format mit richtigem Dateiformat.

- ### Weitere Informationen folgen...