// Relais Pins
#define Relais_AC           6
#define Relais_AC_to_NT     7
#define Relais_NT_to_BT     8   
#define Relais_BT_to_DC     9
#define Relais_DC_to_WR     10
#define Relais_WR_to_AC     11

// ADS1115 Pins
#define ADS1115_SDA 18
#define ADS1115_SCL 19

// PWM Output
#define PWM_NT 3
#define PWM_DC 5

// Funktionsdefinitionen
void off(void); 


void setup(){
    Serial.begin(115200);
}


void loop(){
    delay(1000);
}


void off(){
    delay(1000);
}