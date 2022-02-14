#include <iostream>
#define LOG std::cout << x << std::endl


/**
 * The difference between classes and structs NOTHING except 1 thing.
 * Members of a class are private by default, and in a struct are public by default.
 */
class Player {
    // By default, these variables are private.
public:
    int x, y;
    int speed;

    void move(int newX, int newY) {
        x += newX * speed;
        y += newY * speed;
    }
};

/**
 * Recommended use: for plain old data. Whenever you just need to group values together and access them without trouble.
 */
struct Vector2 {
    float x, y;
};


int main() {
    Player player;
    player.x = 5;
    player.move(1, -1);
}
