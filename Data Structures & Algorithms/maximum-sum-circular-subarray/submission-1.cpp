class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // first, calculate the max assuming solution subarray is non-circular
        int maxSum1 = nums[0];
        int runningSum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            runningSum = max(nums[i], runningSum + nums[i]);
            maxSum1 = max(maxSum1, runningSum);
        }

        if( maxSum1 < 0 ) return maxSum1;

        // second, assuming solution subarray is circular, then we calculate
        // the middle portion that we don't want - which is the longest subarray
        // that hurts the max sum
        int total = accumulate(nums.begin(), nums.end(), 0);
        int maxDeduction = nums[0];
        int runningDeduction = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            runningDeduction = min(nums[i], runningDeduction + nums[i]);
            maxDeduction = min(maxDeduction, runningDeduction);
        }

        int maxSum2 = total - maxDeduction;

        return max( maxSum1, maxSum2);
    }
};