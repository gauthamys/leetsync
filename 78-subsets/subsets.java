class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> s = new ArrayList<>();
        s.add(new ArrayList<>());
        for(int i=0; i<nums.length; i++) {
            int sLen = s.size();
            for(int j=0; j<sLen; j++) {
                List<Integer> sub = s.get(j);
                List<Integer> newSubset = new ArrayList<>(sub);
                newSubset.add(nums[i]);
                s.add(newSubset);
            }
        }
        return s;
    }
}