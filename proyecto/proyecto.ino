//DECLARAMOS LAS VARIABLES PARA LOS LEDS (no. pin)
byte redPin= 11;
byte greenPin= 10;
byte bluePin= 9;
 
//Para Guardarlos como cadena de caracteres diferentes.
String str1;

int dato1;

void setup() {
  Serial.begin(9600);
  //para inicializar el led
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

}

void loop() {
  // nos entrega un numero mayor que 0 
  if (Serial.available() > 0){
    // Leer cadena hasta ...
    str1 = Serial.readStringUntil('\n');
    dato1 = str1.toInt();

  }

  if (dato1 == 1){
    analogWrite(redPin,0);
    analogWrite(greenPin,0);
    analogWrite(bluePin,255);
  }else if (dato1 == 2){
    analogWrite(redPin,0);
    analogWrite(greenPin,255);
    analogWrite(bluePin,0);
  } else  if (dato1 == 3){
    analogWrite(redPin,255);
    analogWrite(greenPin,0);
    analogWrite(bluePin,0);
  }else if (dato1 == 4){
    analogWrite(redPin,255);
    analogWrite(greenPin,255);
    analogWrite(bluePin,0);
  }else if (dato1 == 5){
    analogWrite(redPin,0);
    analogWrite(greenPin,255);
    analogWrite(bluePin,255);
  } else{
    analogWrite(redPin,0);
    analogWrite(greenPin,0);
    analogWrite(bluePin,0);
  }
}
