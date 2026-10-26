#include <stdio.h>
#include <stdlib.h>

void clr_trm() {
    // \x1b[2J clears the screen, \x1b[H moves cursor to the top-left corner
    printf("\x1b[2J\x1b[H");
}

char win_detection(char space[]) {
    if((space[0] == 'X' || space[0] == 'O') && space[0] == space[1] && space[1] == space[2]) {
        return space[0];
    }else if((space[3] == 'X' || space[3] == 'O') && space[3] == space[4] && space[4] == space[5]) {
        return space[3];
    }else if((space[6] == 'X' || space[6] == 'O') && space[6] == space[7] && space[7] == space[8]) {
        return space[6];
    }else if((space[0] == 'X' || space[0] == 'O') && space[0] == space[3] && space[3] == space[6]) {
        return space[0];
    }else if((space[1] == 'X' || space[1] == 'O') && space[1] == space[4] && space[4] == space[7]) {
        return space[1];
    }else if((space[2] == 'X' || space[2] == 'O') && space[2] == space[5] && space[5] == space[8]) {
        return space[2];
    }else if((space[0] == 'X' || space[0] == 'O') && space[0] == space[4] && space[4] == space[8]) {
        return space[0];
    }else if((space[2] == 'X' || space[2] == 'O') && space[2] == space[4] && space[4] == space[6]) {
        return space[2];
    }else {
        return 't';
    }
}

void show(char board[9]) {
    int i;
    for(i = 0; i < 9; i++) {
        printf("%c",board[i]);
        if(i == 2 || i == 5 || i == 8) {
            printf("\n");
        }
    }
}

int main() {
    char board[9] = "---------";
    int play = 1;
    int inp = -1;
    int running = 1;
    while(running) {
        clr_trm();
        show(board);
        printf("choose play location (1-9) Player:%c\n", (play==0)?'O':'X');
        scanf("%d", &inp);
        inp--;

        if(board[inp] != 'X' && board[inp] != 'O') {
            if(play == 1) {
                board[inp] = 'X';
            }else if(play == 0) {
                board[inp] = 'O';
            }
            play = 1-play;
        }
        
        char wd = win_detection(board);

        if (wd != 't') {
            clr_trm();
            show(board);
            printf("Player: %c wins \n", wd);
            running = 0;
            break;
        }else {
            int count = 0;
            int i;
            for(i = 0; i < 9; i++) {
                if(board[i] != 'X' && board[i] != 'O') {
                    continue;
                }else {
                    count++;
                }
            }
            if(count == 9) {
                clr_trm();
                show(board);
                printf("Its a Tie! \n");
                running = 0;
                break;
            }
        }
    }

    return 0;
} 