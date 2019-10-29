import processing.serial.*;
Serial myPort;
String ledStatus="LED: OFF";
String data ;
String loc;
String lat ;
String lon ;

 
int numbers0 ; 
 int numbers1 ; 

int numbers10 ; 
 int numbers11 ; 

String n0  ;
 String n1 ; 

String n2 ; 
 String n3 ; 



void setup(){
  size(450, 500);
  myPort = new Serial(this, Serial.list()[0], 38400); // Starts the serial communication
  myPort.bufferUntil('\n'); // Defines up to which character the data from the serial port will be read. The character '\n' or 'New Line'
}
void serialEvent (Serial myPort){ // Checks for available data in the Serial Port
  data = myPort.readStringUntil('\n'); //Reads the data sent from the Arduino (the String "LED: OFF/ON) and it puts into the "ledStatus" variable
  
}
void draw(){
  data = myPort.readStringUntil('\n');
  String n0 = str(numbers0) ;
 String n1 = str(numbers1); 

String n2 = str(numbers10); 
 String n3 = str(numbers11); 
  numbers0 = data.charAt(0);
  numbers1 = data.charAt(1);
  numbers10 = data.charAt(2);
  numbers11 = data.charAt(3);
  
  
  
  int[] numbers = new int[3]; 
numbers[0] = numbers0; 
numbers[1] = numbers1; 
 
String lat = join(nf(numbers, 0), ""); 
println(lat);  // Prints "8, 67, 5" 

int[] numbers1 = new int[3]; 
numbers[0] = numbers10; 
numbers[1] = numbers11; 

String lon = join(nf(numbers1, 0), ""); 
println(lon);  // Prints "8, 67, 5" 
  
  
   
  background(237, 240, 241);
  fill(20, 160, 133); // Green Color
  stroke(33);
  strokeWeight(1);
  rect(50, 100, 150, 50, 10);  // Turn ON Button
  rect(250, 100, 150, 50, 10); // Turn OFF Button
  fill(255);
  
  textSize(32);
  text("Turn ON",60, 135);
  text("Turn OFF", 255, 135);
  textSize(24);
  fill(33);
  text("Status:", 180, 200);
  textSize(30);
  textSize(16);
 
   
  
   
 

 
 
  text(data, 155, 240); // Prints the string comming from the Arduino
  
  // If the button "Turn ON" is pressed
  if(mousePressed && mouseX>50 && mouseX<200 && mouseY>100 && mouseY<150){
    myPort.write('1'); // Sends the character '1' and that will turn on the LED
    // Highlighs the buttons in red color when pressed
    stroke(255,0,0);
    strokeWeight(2);
    noFill();
    rect(50, 100, 150, 50, 10);
  }
  // If the button "Turn OFF" is pressed
  if(mousePressed && mouseX>250 && mouseX<400 && mouseY>100 && mouseY<150){
    myPort.write('0'); // Sends the character '0' and that will turn on the LED
    stroke(255,0,0);
    strokeWeight(2);
    noFill();
    rect(250, 100, 150, 50, 10);
  }
}
