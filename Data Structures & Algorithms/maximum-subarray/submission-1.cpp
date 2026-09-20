class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int runningSum = nums[0];
        for( int i = 1; i < nums.size(); i++ ){
            int num = nums[i];
            if( runningSum <= 0){
                // case 1: runningSum is negative and
                // we have a number bigger than running sum (can be negative too)
                // start a new running sum
                if ( num > runningSum ){
                    runningSum = num;
                    maxSum = std::max(maxSum, runningSum);
                }
                // case 2: runningSum is negative and
                // our number is smaller; reset runningSum
                else {
                    runningSum = num;
                }
            }
            else {
                // case 3: runningSum is positive. adding this number does not make it negative
                if ( num + runningSum >= 0 ){
                    runningSum += num;
                    maxSum = std::max(maxSum, runningSum);
                }
                // case 4: adding this number makes runningSum negative; reset
                else {
                    runningSum = num;
                }
            }
        }
        return maxSum;
    }
};
