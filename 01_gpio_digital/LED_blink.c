#include <wiringPi.h>
#define LED_PIN 23
#define LED_PIN2 24
#define LED_PIN3 25
int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio();
  pinMode (LED_PIN, OUTPUT) ;
  //pinMode (LED_PIN2, OUTPUT) ;
  //pinMode (LED_PIN3, OUTPUT) ;
  for (int i=0 ;i<1;i++)
  {
    digitalWrite (LED_PIN, HIGH) ; delay (2000) ;
    digitalWrite (LED_PIN,  LOW) ;
    //digitalWrite (LED_PIN2, HIGH) ; delay (2000) ;
    //digitalWrite (LED_PIN2,  LOW) ;
    //digitalWrite (LED_PIN3, HIGH) ; delay (2000) ;
    //digitalWrite (LED_PIN3,  LOW) ;
  }
  pinMode (LED_PIN, INPUT) ;
  //pinMode (LED_PIN2, INPUT) ;
  //pinMode (LED_PIN3, INPUT) ;
  return 0 ;
}