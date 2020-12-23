/* Just to compare speed */

#include <stdio.h>

#define BASE 1000001
#define NROUNDS 10000000

int mod(int a, int b)
{
    int r = a % b;
    return r < 0 ? r + b : r;
}

void pickup(int *cups, int current, int *pc) {
    pc[0] = cups[current];
    pc[1] = cups[pc[0]];
    pc[2] = cups[pc[1]];
    cups[current] = cups[pc[2]];
}

void insert(int *cups, int dest, int *pc) {
    cups[pc[2]] = cups[dest];
    cups[dest] = pc[0];
    cups[pc[0]] = pc[1];
    cups[pc[1]] = pc[2];
}

void pp(int *cups, int current) {
    printf("cups: (%d) ", current);
    int cup = cups[current];
    while(cup != current) {
        printf("%d ", cup);
        cup = cups[cup];
    }
    printf("\n");
}


int play(int *cups, int current, int *pc) {
    pickup(cups, current, pc);

    int dest = mod(current-1, BASE);

    while(dest == pc[0] || dest == pc[1] || dest == pc[2] || dest == 0)
        dest = mod(dest-1, BASE);
        
    insert(cups, dest, pc);

    return cups[current];
}

int main(int argc, char **argv) {
    int cups[BASE];
    int current = 3;
    static int input[] = {3,1,8,9,4,6,5,7,2};
    
    int pc[] = {0,0,0};

    /* Build the list of cups */
    for(int i=0; i<8; i++) {
        cups[input[i]] = input[i+1];
    }
    cups[2] = 10;
    
    for(int i=10; i<BASE-1; i++) {
        cups[i] = i+1;
    }
    cups[BASE-1] = 3;

    for(int i=0; i<NROUNDS; i++) {    
        current = play(cups, current, pc);
    }
    int c1 = cups[1];
    int c2 = cups[c1];

    printf("%d %d %llu\n", c1, c2, (unsigned long long)c1*c2);

    return 0;
}