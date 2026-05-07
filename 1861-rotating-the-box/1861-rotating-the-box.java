class Solution {
    public char[][] rotateTheBox(char[][] boxGrid) {
        int n = boxGrid.length;
        int m = boxGrid[0].length;

        for(int i = 0 ; i< n ; i++){
            for(int j = m-1 ; j>= 0 ;j--){
                if(boxGrid[i][j] == '#'){
                    int k = j+1;
                    while(k < m && boxGrid[i][k] == '.'){
                        k++;
                    }
                    if(k != j){
                        boxGrid[i][j] = '.';
                        boxGrid[i][k-1] = '#';
                    }
                }
            }
        }

        char[][] ans = new char[m][n];
        for(int i = 0 ; i <  n ; i++){
            for(int j = 0 ; j < m ; j++){
                ans[j][i] = boxGrid[i][j];
            }
        }

        for(int i = 0 ; i < m ; i++){
            int left = 0; int right = n-1;
            while(left < right){
                char temp = ans[i][left];
                ans[i][left] = ans[i][right];
                ans[i][right] = temp;
                left++;
                right--;
            }
        }

        return ans;
    }
}