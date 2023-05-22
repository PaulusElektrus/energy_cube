// Json
#include <ArduinoJson.h>
String url = "http://192.168.0.***/rpc/EM.GetStatus?id=0";

// W-Lan & Webserver
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#define WIFI_SSID "***"
#define WIFI_PASSWORD "***"

// InfluxDB
#include <InfluxDbClient.h>
#define INFLUXDB_URL "***"
#define INFLUXDB_DB_NAME "***"
#define INFLUXDB_USER "***"
#define INFLUXDB_PASSWORD "***"
InfluxDBClient client(INFLUXDB_URL, INFLUXDB_DB_NAME);

// Incoming Communication
boolean newData = false;
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];
char statusFromArduino[numChars] = {0};
float uNT = 0;
float uBatt = 0.0;
float uWR = 0.0;
float iBatt = 0.0;
float bsPower = 0.0;

// Outgoing Communication
String command = "Off";
float power = 0.0;
Point sensor("energy");


void setup() {
    Serial.begin(115200);
    Serial.println("Verbinden mit ");
    Serial.println(WIFI_SSID);

    // W-Lan Verbindung
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    // W-Lan prüfen 
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
        delay(500);
    }

    Serial.println("");
    Serial.println("WiFi verbunden!");
    Serial.print("IP= ");  Serial.println(WiFi.localIP());

    // InfluxDB V 1.0
    client.setConnectionParamsV1(INFLUXDB_URL, INFLUXDB_DB_NAME, INFLUXDB_USER, INFLUXDB_PASSWORD);
    sensor.addTag("device", "energy_cube");
}


void loop() {
    getPower();
    sendCommand();
    getMeasurements();
    sendToServer();
    delay(2000);
}


void getPower() {
// https://arduinojson.org/v6/api/jsonobject/begin_end/
    WiFiClient client;
    HTTPClient http;
    http.begin(client,url);
    int httpCode = http.GET();
    if (httpCode > 0) {
      String payload = http.getString();
      StaticJsonDocument<768> doc;
      deserializeJson(doc, payload);
      JsonObject root = doc.as<JsonObject>();
      int index = 18;
      JsonObject::iterator it = doc.as<JsonObject>().begin();
      it += index;
      power = it->value().as<float>();
    }
    else {
        Serial.print("Keine aktuellen Leistungsdaten verfuegbar");
        power = 0.0;
    }
    http.end();
}


void sendCommand() {
    String outgoingData = "<" + command + "," + String(power) + ">";
    Serial.print(outgoingData);
}


void getMeasurements() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
        parseData();
        showParsedData();
        newData = false;
    }
}


void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0';
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}


void parseData() {

    char * strtokIndx;

    strtokIndx = strtok(tempChars,",");
    strcpy(statusFromArduino, strtokIndx);
 
    strtokIndx = strtok(NULL, ",");
    uNT = atof(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    uBatt = atof(strtokIndx); 

    strtokIndx = strtok(NULL, ",");
    uWR = atof(strtokIndx);

    strtokIndx = strtok(NULL, ",");
    iBatt = atof(strtokIndx);
    
    strtokIndx = strtok(NULL, ",");
    bsPower = atof(strtokIndx);

}


void showParsedData() {
    Serial.print("Status: ");
    Serial.println(statusFromArduino);
    Serial.print("uNT: ");
    Serial.println(uNT);
    Serial.print("uBatt: ");
    Serial.println(uBatt);
    Serial.print("uWR: ");
    Serial.println(uWR);
    Serial.print("iBatt: ");
    Serial.println(iBatt);
    Serial.print("bsPower: ");
    Serial.println(bsPower);
}


void sendToServer() {
    sensor.clearFields();
    sensor.addField("Status", statusFromArduino);
    sensor.addField("uNT", uNT);
    sensor.addField("uBatt", uBatt);
    sensor.addField("uWR", uWR);
    sensor.addField("iBatt", iBatt);
    sensor.addField("bsPower", bsPower);
    client.pointToLineProtocol(sensor);
    if (!client.writePoint(sensor)) {
        Serial.print("InfluxDB write failed: ");
        Serial.println(client.getLastErrorMessage());
    }
}