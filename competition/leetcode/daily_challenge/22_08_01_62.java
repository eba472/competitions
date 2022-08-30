package leetcode.daily_challenge;

class Solution {
    public static void main(String[] args) {
        int ans = uniquePaths(3,2);
        System.out.println(ans); 
    }
    private static int uniquePaths(int m, int n){
        int[][] a = new int[m+1][n+1];
        a[0][1] =1;
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++){
                a[i][j] = a[i-1][j] + a[i][j-1];
            }
        }
        return a[m][n];
    }
}
