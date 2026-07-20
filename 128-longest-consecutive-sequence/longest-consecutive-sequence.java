class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int n: nums) {
            s.add(n);
        }
        int res = 0;
        for (int n: s) {
            if (s.contains(n - 1)) continue;
            int cur = n;
            int curLen = 0;
            while (s.contains(cur)) {
                cur++;
                curLen++;
            }
            res = Math.max(res, curLen);
        }
        return res;
    }
}