#include <stdio.h>
#include <stdlib.h>

void clr_trm() {
    // \x1b[2J clears the screen, \x1b[H moves cursor to the top-left corner
    printf("\x1b[2J\x1b[H");
}

int main() {
    
    int num;
    char hi[2] = "hi";
    
    while(1) {
        clr_trm();
        for(num = -10; num < 2; num++) {
            printf("%x ", hi[num]);
        }
    }
    
    return 0;
}