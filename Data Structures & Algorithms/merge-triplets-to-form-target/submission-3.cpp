class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        /*
        observation: if any triplet contain a no. greater than any no. in target, we cannot take it because the value cannot be reduced
        else, we can always take any triplet as any intermediate triplet will increase till we reach target
        */
        vector<int> v{0,0,0};
        
        for( int i = 0; i < triplets.size(); i++ ){
            vector<int>& curr = triplets[i];
            if( curr[0] > target[0] || curr[1] > target[1] || curr[2] > target[2])
                continue;
            v[0] = max({ v[0], curr[0]});
            v[1] = max({ v[1], curr[1]});
            v[2] = max({ v[2], curr[2]});
        }
        
        return v[0]==target[0] && v[1]==target[1] && v[2]==target[2];
    }
};
