class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0; i<nums.length; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int s = nums[i] + nums[l] + nums[r];
                if (s == 0) {
                    res.add(List.of(nums[i], nums[l], nums[r]));
                    l++;
                    while(l < r && nums[l] == nums[l - 1]) {
                        l++;
                    }
                } else if (s < 0){
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }
}