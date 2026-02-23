class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x^y;
        int count = 0;
        while(xor!=0){
            int bit = xor & 1;
            count+=bit;
            xor = xor >> 1;
        }
        return count;
    }
}