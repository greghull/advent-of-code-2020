/* Just to compare speed */

#include <stdio.h>
#include <stdint.h>

#define BASE 1000001
#define NROUNDS 10000000

int mod(int a, int b)
{
    int r = a % b;
    return r < 0 ? r + b : r;
}

void pickup(int_fast32_t *cups, int_fast32_t current, int_fast32_t *pc) {
    pc[0] = cups[current];
    pc[1] = cups[pc[0]];
    pc[2] = cups[pc[1]];
    cups[current] = cups[pc[2]];
}

void insert(int_fast32_t *cups, int_fast32_t dest, int_fast32_t *pc) {
    cups[pc[2]] = cups[dest];
    cups[dest] = pc[0];
    cups[pc[0]] = pc[1];
    cups[pc[1]] = pc[2];
}

void pp(int_fast32_t *cups, int_fast32_t current) {
    printf("cups: (%d) ", current);
    int cup = cups[current];
    while(cup != current) {
        printf("%d ", cup);
        cup = cups[cup];
    }
    printf("\n");
}


int_fast32_t play(int_fast32_t *cups, int_fast32_t current, int_fast32_t *pc) {
    pickup(cups, current, pc);

    int_fast32_t dest = mod(current-1, BASE);

    while(dest == pc[0] || dest == pc[1] || dest == pc[2] || dest == 0)
        dest = mod(dest-1, BASE);
        
    insert(cups, dest, pc);

    return cups[current];
}

int_fast32_t main(int_fast32_t argc, char **argv) {
    int_fast32_t cups[BASE];
    int_fast32_t current = 3;
    static int_fast32_t input[] = {3,1,8,9,4,6,5,7,2};
    
    int_fast32_t pc[] = {0,0,0};

    /* Build the list of cups */
    for(int_fast32_t i=0; i<8; i++) {
        cups[input[i]] = input[i+1];
    }
    cups[2] = 10;
    
    for(int_fast32_t i=10; i<BASE-1; i++) {
        cups[i] = i+1;
    }
    cups[BASE-1] = 3;



    for(int_fast32_t i=0; i<NROUNDS; i++) {    
        current = play(cups, current, pc);
    }
    int_fast32_t c1 = cups[1];
    int_fast32_t c2 = cups[c1];

    printf("%d %d %llu\n", c1, c2, (unsigned long long)c1*c2);

    return 0;
}