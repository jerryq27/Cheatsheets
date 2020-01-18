#include <iostream>

//extern int s_Variable; // extern, looks for the variable in another translation unit. 1 cpp file gets compiled into 1 translation unit

struct Entity {
    int x, y;

    void print() {
        std::cout << x << ", " << y << std::endl;
    }
};

int main() {
    //std::cout << s_Variable << std::endl;

    Entity e1;
    e1.x = 1;
    e1.y = 2;

    Entity e2 = {4, 4};

    e1.print();
    e2.print();
}