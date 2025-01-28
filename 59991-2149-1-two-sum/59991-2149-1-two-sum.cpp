class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> potionMap; // Tracks {strength: index}

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (potionMap.count(complement)) {
                return {potionMap[complement], i}; // Found the pair!
            }
            potionMap[nums[i]] = i; // Store current potion in the map
        }
        return {}; // No solution (won't happen here)
    }
};