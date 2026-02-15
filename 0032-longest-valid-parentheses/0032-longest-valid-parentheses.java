class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        Stack<Integer> sk = new Stack<>();
        sk.push(-1);
        int res = 0;
        for(int i=0; i<n; i++){
            if(s.charAt(i) == '('){
                sk.push(i);
            }
            else {
                if(!sk.empty()){
                    sk.pop();
                } 
                if(!sk.empty()){
                    res = Math.max(res, i-sk.peek());
                } else {
                    sk.push(i);
                }
            }
        }
        return res;
    }
}