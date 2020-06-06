/** bigO = n i think
 * How to use unordered_map, a hash table with a key type and value type
 * how to use iterator for a map, it is a pointer object, bidirectional
 * */
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> map;
    vector<int> indices;
    for(int i = 0; i < nums.size(); i++)
    {
        int complement = target - nums[i];
        std::unordered_map<int, int>::iterator iterator = map.find(complement);
        if(iterator != map.end())
        {
            int index = iterator->second;
            indices.push_back(index);
            indices.push_back(i);
            return indices;
        }
        map[nums[i]] = i;   
    }
    return indices;
    }
};