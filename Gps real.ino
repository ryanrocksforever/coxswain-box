// TinyGPS - Version: Latest 
#include <TinyGPS.h>


// LiquidCrystal - Version: Latest 


// TinyGPS++ - Version: Latest 


#include <LiquidCrystal.h>
#include <SoftwareSerial.h>
#include <TinyGPS.h>
//long   lat,lon; // create variable for latitude and longitude object
float lat = 28,lon = 77; // create variable for latitude and longitude object 
float falt;
float fc ;
float fk ;
float fmph ;
float fmps; 
float fkmph ;
float stroke ;
float strokec ;
float split ;
float stime ; 
float hall ; 
int year ;
float count ;
int connection ;
/*
float day ;
float month ;
float hour ;
float minute ;
float second ;
float hundredths ;
 */

byte month, day, hour, minute, second, hundredths;
unsigned long fix_age;


#define STROKE_PIN = 5; 
SoftwareSerial gpsSerial(3,4);//rx,tx
LiquidCrystal lcd(A0,A1,A2,A3,A4,A5);
TinyGPS gps; // create gps object
void setup(){
Serial.begin(9600); // connect serial
//Serial.println("The GPS Received Signal:");
gpsSerial.begin(9600); // connect gps sensor
lcd.begin(16,2);

pinMode(5, INPUT);
digitalWrite(5, HIGH);
stroke = 0 ;
count = 0 ;
}
 
void loop(){
    count ++ ;
    if(digitalRead(5) >= 1){

        hall = LOW;

    }
    if(hall == LOW){
        strokec ++ ;

    }
    if(count >= 5){
        stroke = strokec * 12;
        count = 0 ;
        
    }
    
     split = 500/fmps ;

    while(gpsSerial.available()){ // check for gps data
    if(gps.encode(gpsSerial.read()))// encode gps data
    { 
     gps.f_get_position(&lat, &lon, &fix_age);
     lat = round(lat);
     lon = round(lon);
     falt = gps.f_altitude(); // +/- altitude in meters
     fc = gps.f_course(); // course in degrees
    fk = gps.f_speed_knots(); // speed in knots
    fmph = gps.f_speed_mph(); // speed in miles/hr
    fmps = gps.f_speed_mps(); // speed in m/sec
    fkmph = gps.f_speed_kmph(); // speed in km/hr
    connection = gps.satellites();
    gps.crack_datetime(&year, &month, &day,
  &hour, &minute, &second, &hundredths, &fix_age);
    // display position
    lcd.clear();
    lcd.setCursor(1,0);
    lcd.print("GPS Signal");
    //Serial.print("Position: ");
    //Serial.print("Latitude:");
    //Serial.print(lat,6);
    //Serial.print(";");
    //Serial.print("Longitude:");
    //Serial.println(lon,6); 
    lcd.setCursor(1,0);
    lcd.print("LAT:");
    lcd.setCursor(5,0);
    lcd.print(lat);
    //Serial.print(lat);
    //Serial.print(" ");
    
    lcd.setCursor(0,1);
    lcd.print(",LON:");
    lcd.setCursor(5,1);
    lcd.print(lon);
    
   }
  }
  


  String latitude = String(lat,6);
    String longitude = String(lon,6);

  Serial.print(latitude+longitude);
 
  Serial.print((String)"course"+fc);
  Serial.print((String)"knots"+fk);
  Serial.print((String)"altitude"+falt);
  Serial.print((String)"mph"+fmph);
  Serial.print((String)"mps"+fmps);
  Serial.print((String)"kmph"+fkmph);
  Serial.print((String)"stroke rate"+stroke);
  Serial.print((String)"No connection Satielites="+connection);
  Serial.print((String)"split"+split);

  Serial.print((String)"date"+year+month+day+"time ="+hour+":"+second+":"+hundredths);
  Serial.println(" ");
  delay(999);
  if(connection <= 1){

      
  }
  
   
}