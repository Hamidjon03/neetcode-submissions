class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const map = {
            "+" : (a, b) => a + b,
            "-" : (a, b) => a - b,
            "*" : (a, b) => a * b,
            "/" : (a, b) => Math.trunc(a / b)
        }
        let stack = [];

        for(let char of tokens){

            if(this.isOperand(char)){
                let last = stack.pop();
                let preLast = stack.pop();
                let result = map[char](preLast, last)
                stack.push(result);
            } else {
                stack.push(parseInt(char))
            }

        }

        return stack[0]
    }

    isOperand(operand){
        return (
            operand === "+" ||
            operand === "-" ||
            operand === "/" ||
            operand === "*"
        )
    }
}
