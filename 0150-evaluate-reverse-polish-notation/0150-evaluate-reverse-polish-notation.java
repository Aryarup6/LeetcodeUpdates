class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();
        for (String st : tokens) {
            if (isOperand(st)) {
                s.push(Integer.parseInt(st));
            } else {
                int op2 = s.pop();
                int op1 = s.pop();
                switch (st) {
                    case "+":
                        s.push(op1+op2);
                        break;
                    case "-":
                        s.push(op1-op2);
                        break;
                    case "*":
                        s.push(op1*op2);
                        break;
                    case "/":
                        s.push(op1/op2);
                        break;
                }
            }
        }
        return s.pop();
    }
    private static boolean isOperand(String token) {
        return token.matches("-?\\d+");
    }
}