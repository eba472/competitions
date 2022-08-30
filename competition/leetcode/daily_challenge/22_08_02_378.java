package leetcode.daily_challenge;

import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public static void main(String[] args) {
        int[][] matrix = {{1,5,9},{10,11,13},{12,13,15}};
        int ans = kthSmallest(matrix,8);
        System.out.println(ans); 
    }
    public static int kthSmallest(int[][] matrix, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                System.out.println(heap.toString());
                heap.add(matrix[i][j]);
                if(heap.size() > k){
                    heap.poll();
                }

            }
        }
        System.out.println(heap.toString());
        return heap.peek();
    }
}
