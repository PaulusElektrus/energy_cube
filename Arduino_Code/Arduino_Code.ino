// Relais Pins
#define Relais_AC           6
#define Relais_AC_to_NT     7
#define Relais_NT_to_BT     8   
#define Relais_BT_to_DC     9
#define Relais_DC_to_WR     10
#define Relais_WR_to_AC     11

// ADS1115
#include<ADS1115_WE.h> 
#include<Wire.h>
#define I2C_ADDRESS 0x48
ADS1115_WE adc = ADS1115_WE(I2C_ADDRESS);

// PWM Output
#define PWM_NT 3
#define PWM_DC 5

// Incoming Communication
boolean newData = false;
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];
char commandFromESP[numChars] = {0};
float powerFromESP = 0.0;

// Outgoing Communication
String Status = "Off";
float uNT = 0.0;
float uBatt = 0.0;
float uWR = 0.0;
float iBatt = 0.0;
float bsPower = 0.0;


void setup(){
    Serial.begin(115200);
    Wire.begin();
    adc.init();
    adc.setVoltageRange_mV(ADS1115_RANGE_6144);
}


void loop(){
    getCommand();
    measurement();
    control();
    returnData();
    delay(2000);
}


void getCommand() {
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
    strcpy(commandFromESP, strtokIndx);     

    strtokIndx = strtok(NULL, ",");
    powerFromESP = atof(strtokIndx);

}


void showParsedData() {
    Serial.print("Control: ");
    Serial.println(commandFromESP);
    Serial.print("Power: ");
    Serial.println(powerFromESP);
}


void measurement() {
    uNT = readChannel(ADS1115_COMP_0_GND);
    uBatt = readChannel(ADS1115_COMP_1_GND);
    uWR = readChannel(ADS1115_COMP_2_GND);
    iBatt = readChannel(ADS1115_COMP_3_GND);
}


float readChannel(ADS1115_MUX channel) {
  float voltage = 0.0;
  adc.setCompareChannels(channel);
  adc.startSingleMeasurement();
  while(adc.isBusy()){}
  voltage = adc.getResult_mV();
  return voltage;
}


void control() {
    bsPower = uBatt * iBatt;
}


void returnData() {
    String outgoingData = "<" + Status + "," + String(uNT) + "," + String(uBatt) + "," + String(uWR) + "," + String(iBatt) + "," + String(bsPower) + ">";
    Serial.print(outgoingData);
}
