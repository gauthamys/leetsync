class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> v = new HashSet<>();
        for (int i=0; i<nums.length; i++) {
            if (v.contains(nums[i])) {
                return true;
            }
            v.add(nums[i]);
        }
        return false;
    }
}