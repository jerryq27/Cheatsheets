class Node {
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class DoublyLinkedLIst {
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
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;

        return this;
    }
}

let dll = new DoublyLinkedLIst();
dll.push(1);
dll.push(7);
dll.push(12);
dll.push(20);
console.log(dll);