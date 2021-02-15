
class Solution {
public:
       //Using Brute Force
//     vector<int> twoSum(vector<int>& nums, int target) {
//         vector<int> out;
//         out.clear();
//         for(int i =0;i<nums.size();i++){
//             // cout<<nums[i]<<'\n';
//             for(int j = i+1;j<nums.size();j++){
//                 if(nums[i]+nums[j] == target){
//                     out.push_back(i);
//                     out.push_back(j);
//                     return out;
//                 }
//             }
//         }
        
//         return out;
        
//     }
    //Using hasmap : One pass
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> h;
        for(int i = 0;i<nums.size();i++){
            auto item = h.find(target - nums[i]);
            if( item != h.end()){
                return{item->second,i};
            }
            h[nums[i]] = i;
        }
        return{};
    }
};

