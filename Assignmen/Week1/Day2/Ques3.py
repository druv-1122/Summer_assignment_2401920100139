class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int l = 0;
        int r = 0;
        int n = nums.length;
        double maxAvg = Integer.MIN_VALUE;

        int sum = 0;

        while(r < n) {
            sum = sum + nums[r];

            if( r >= k-1) {

                maxAvg = Math.max(maxAvg, sum);

                sum = sum - nums[l];
                l++;
            }

            r++;
        } 
        return maxAvg/k;
    }
}
