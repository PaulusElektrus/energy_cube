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

// Outgoing Communication
String command = "Off";
float power = 0.0;


void setup() {
    Serial.begin(115200);
}


void loop() {
    getPower();
    sendCommand();
    getMeasurements();
    sendToServer();
    delay(2000);
}


void getPower() {

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
}


void sendToServer() {

}