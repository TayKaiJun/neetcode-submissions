class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int runningSum = nums[0];
        for( int i = 1; i < nums.size(); i++ ){
            // simplification - there's only 2 meaningful choices at each num
            // extend the running sum, or start a new one
            runningSum = max(nums[i], runningSum + nums[i]);
            maxSum = max(maxSum, runningSum);
        }
        return maxSum;
    }
};
