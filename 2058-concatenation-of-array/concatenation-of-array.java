class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] res = new int[2 * nums.length];
        for(int i=0; i<res.length; i++) {
            res[i] = nums[i % nums.length];
        }
        return res;
    }
}