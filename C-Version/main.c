#define F_CPU 16000000
#include <avr/io.h>
#include <util/delay.h>

int main(){
	DDRC = 0b11111111;
	PORTC = 0b11111111;
	while(1){
		PORTC = 0b11111111;
	}
}
