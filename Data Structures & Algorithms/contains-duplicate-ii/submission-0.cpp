class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        std::set<int> seen;
        int left = 0;
        for( int i = 0; i < nums.size(); i++ ){
            if( seen.contains( nums[i] ) ){
                return true;
            }
            seen.insert( nums[i] );

            if( i - left >= k ){
                seen.erase( nums[left] );
                left++;
            }
        }
        return false;
    }
};