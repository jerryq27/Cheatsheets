class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }
    /**
     * Adds a value to the end of the list.
     * @param {*} val 
     * @returns the list.
     */
    push(val) {
        let newNode = new Node(val);
        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;

        return this;
    }
    /**
     * This methods removes the last value, resets the tail, and returns the value removed.
     * @returns the value that was removed.
     */
    pop() {
        if(!this.head) return undefined;

        let curr = this.head;
        let prev = null;
        // while(curr) {
        //     if(curr.next) {
        //         prev = curr;
        //         curr = curr.next;
        //     }
        //     else {
        //         prev.next = null;
        //         this.tail = prev;
        //         this.length--;
        //         return curr.val;
        //     }
        // }
        while(curr.next) {
            prev = curr;
            curr = curr.next;
        }
        prev.next = null;
        this.tail = prev;
        this.length--;
        if(this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return curr.val;
    }
    /**
     * This method removes the value at the head of the list and sets the next value as the head.
     * @returns The removed previous head value.
     */
    shift() {
        if(!this.head) return undefined;
        
        let curr = this.head;
        this.head = curr.next;
        this.length--;
        if(this.length === 0) {
            this.tail = null;
        }
        return curr.val;
    }
    /**
     * This method adds a new value to the beginning of the list.
     * @param {*} val 
     * @returns the list.
     */
    unshift(val) {
        let newNode = new Node(val);
        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return this;
    }
    /**
     * Takes an index and returns the value at that position.
     * @param {*} index
     * @returns the value at the position.
     */
    get(index) {
        if(index < 0 || index >= this.length) return undefined;

        let curr = this.head;

        for(let i = 0; i <= index; i++) {
            if(i === index) {
                return curr;
            }
            curr = curr.next;
        }
    }

    /**
     * Replaces the value at the index with the new value.
     * @param {*} index 
     * @param {*} val
     * @returns whether the value was replaced or not.
     */
    set(index, val) {
        let node = get(index);
        if(node) {
            node.val = val;
            return true;
        }
        return false;
    }
    /**
     * Adds the value at the specified index.
     * @param {*} index 
     * @param {*} val 
     */
    insert(index, val) {
        if(index < 0 || index > this.length) return false;
        if(index === 0) {
            this.unshift(val);
        }
        else if(index === this.length) {
            this.push(val);
        }
        else {
            let newNode = new Node(val);
            let prev = this.get(index - 1);

            newNode.next = prev.next;
            prev.next = newNode;
            this.length++;
        }
        return true;
    }
    /**
     * Removes the value at the specified index.
     * @param {*} index 
     */
    remove(index) {
        if(index < 0 || index >= this.length) return undefined;
        if(index === this.length - 1) return this.pop();
        if(index === 0) return this.shift();

        let prevNode = this.get(index - 1);
        let removedNode = prevNode.next;
        prevNode.next = removedNode.next;
        this.length--;
        return removedNode;
    }
    /**
     * COMMON INTERVIEW QUESTION: Can you reverse a linked list in place?
     * Thie method reverses the list in place (doesn't make a copy).
     * 
     * 1. Track prev, next, and curr nodes. Prev is null, Curr starts at the head, and next at the head's next.
     * 2. Swap head and tail
     * 3. Loop through the list.
     * 4. Set next to the next node from curr.
     * 5. Update curr's next to prev.
     * 6. Set prev to curr.
     * 7. Set curr to next.
     * 8. Repeat until list is reversed.
     */
    myReverse() {
        let prev = null;
        let curr = this.head;
        let next = this.head.next;

        // Swap head and tail.
        this.head = this.tail;
        this.tail = curr;

        // 1 -> 2 -> 3 -> 4
        // p    c    n
        // 1 <- 2 -> 3 -> 4
        //      p    c    n
        // 1 <- 2 <- 3 -> 4
        //           p    c    n
        // 1 <- 2 <- 3 <- 4
        //                p    c    n
        // t              h
        while(curr) {
            next = curr.next;
            curr.next = prev;
            
            prev = curr;
            curr = next;
        }
    }
    reverse() {
        let curr = this.head;
        this.head = this.tail;
        this.tail = curr;

        let prev = null;
        let next;
        for(let i = 0; i < this.length; i++) {
            next = curr.next;
            curr.next = prev;
            
            prev = curr;
            curr = next;
        }
    }

    print() {
        let curr = this.head;
        let vals = []
        while(curr) {
            vals.push(curr.val);
            curr = curr.next;
        }
        console.log(vals.join(' -> '));
    }
}

let list = new SinglyLinkedList();
list.push(1);
list.push(2);
list.push(3);
list.push(4);
list.push(5);

list.print();
list.myReverse();
list.print();
