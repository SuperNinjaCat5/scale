void setup() {
  Serial.begin(9600);
  Serial.println("Send 0 to Start Weighing");
  float x = 0;
}

void loop() {
  while (Serial.available() == 0) {}     //wait for data available
  String teststr = Serial.readString();  //read until timeout
  teststr.trim();                        // remove any \r \n whitespace at the end of the String
  if (teststr == "0") {
    //Serial.println("Starting To Weigh");
    float x = 0;
    x=random(0,100);
    //Serial.print(millis());
    //Serial.print(",");
    Serial.print(x);
    Serial.print(",");
    Serial.print("lbs");
    Serial.println(",");
  } else {
    Serial.println("Something Wrong");
  }
}
