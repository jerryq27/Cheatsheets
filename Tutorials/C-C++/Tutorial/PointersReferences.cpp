#include <iostream>
#include <string.h>
#define LOG(x) std::cout << x << std::endl


/**
 * Pointers:
 *  - Basically just an integer that represents the memory address of a byte.
 *  - Each byte has a pointer.
 *  - Types DO NOT MATTER, they don't change the pointer's value at all, it is still an int representing a memory address.
 *    Types only matter reading and writing to that memory address. The compiler needs to know how much memory it is storing.
 *    Using Types helps the compiler determine that when manipulating the data.
 *  - Pointers only contain a memory address to the first byte of a block of memory, pointers don't know how big the
 *    block of memory is. It's just an address.
 *  - Don't complicate double pointers, it's just a memory address that points to a memory address, it's value is the address of the memory block.
 * References:
 *  - Are not variables, they are just referencing variables, they won't be created in memory.
 *  - They are just aliases for a variable.
 *  - Once a reference is set to a variable, it cannot be reset to another variable.
 *  - When references are created, they must be set to something, null references aren't possible since A REFERENCE IS NOT A REAL VARIABLE.
 */

void increment(int n) {
    n++;
}
void incrementByPtr(int* nPtr) {
    // If you don't dereference the pointer, you'll just increment the address, POINTERS ARE MEMORY ADDRESSES.
    (*nPtr)++; // Order of operations: de-referencing happens after the increment, so we don't want that, use ().
}
void incrementByRef(int& nRef) {
    // References only function is to make the source code look nicer, no need for de-referencing of pointers or anything.
    nRef++; // All we need to do, since it's a reference to a variable, not a variable.
}
int main() {
    /*
     * 0 is basically null for pointers.
     * You can also use nullptr, or NULL (Which is a #define)
     */
    void* ptr = nullptr;

    // Store an integer in memory.
    int var = 8;
    // Access its location with &.
    ptr = &var;
    // To get the value, you dereference the pointer with *
    // This doesn't work, since the compiler doesn't know to store an int, 10 could mean anything (char, int, long)
    // The compiler needs to know how much data to allocate before storing it. So Types help here.
    /* *ptr = 10; */
    int* intPtr = &var;
    *intPtr = 10;
    LOG(var);

    // Asking for 8 bytes of data, the pointer will only point to the first byte in that data block.
    char* buffer = new char[8];
    // memset fills a block in memory with data that we specify. (pointer to the block, data to use, bytes to fill)
    memset(buffer, 0, 8); // Fills 8 bytes with 0.
    // We used new (heap allocates data), so we should free the memory.
    // Since we used array notation to create the block in memory, we should use the array notation delete to delete it.

    // Using double pointers, don't complicate it, it's just a pointer that holds the memory address of the data block.
    char** bufferPtr = &buffer;

    delete[] buffer;

    /* References */
    int num = 8;
    // Create a reference (alias) to the num variable.
    int& ref = num;
    ref = 11;
    LOG(num); // num becomes 10!
    // We can try to increment num, but the default behavior is to pass by value, so a new variable is created in memory and incremented instead of incrementing num.
    increment(num); // Pass by value.
    LOG(num); // No change.
    incrementByPtr(&num); // Pass by reference/address.
    LOG(num); // num is incremented.
    incrementByRef(num); // Pass by reference.
    LOG(num); // num is incremented.

    // References may only be set once.
    int a = 1;
    int b = 2;
    int& aRef = a;
    aRef = b; // This will set a to be the value of b, instead of aRef referencing b.
    // If you want this behaviour, you would use Pointers!
    int* aPtr = &a;
    aPtr = &b;

    std::cin.get();
    return 0;
}

