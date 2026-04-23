class MyQueue {
    constructor() {
        this.arr1 = [];
        this.arr2 = [];
    }
    // [1, 2, 3]
    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        this.arr1.push(x);
    }

    /**
     * @return {number}
     */
    pop() {

        if(this.arr2.length === 0){
            while(this.arr1.length > 0){
                this.arr2.push(this.arr1.pop());
            }
        };

        return this.arr2.pop()

    }

    /**
     * @return {number}
     */
    peek() {
        if(this.arr2.length === 0){

            while(this.arr1.length > 0){
                this.arr2.push(this.arr1.pop());
            }
        } 
        return this.arr2[this.arr2.length - 1];

    }

    /**
     * @return {boolean}
     */
    empty() {
        return this.arr1.length === 0 && this.arr2.length === 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
