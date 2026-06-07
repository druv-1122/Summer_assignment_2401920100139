class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int l = 0;
        int r = 0;
        int n = nums.length;
        double maxAvg = Integer.MIN_VALUE;

        int sum = 0;
