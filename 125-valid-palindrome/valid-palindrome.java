class Solution {
    public boolean isPalindrome(String s) {
        char[] charArray = s.toCharArray();
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            char leftChar = s.charAt(l);
            char rightChar = s.charAt(r);
            if (l < r && !Character.isLetterOrDigit(leftChar)) {
                l++;
                continue;
            }
            if(l < r && !Character.isLetterOrDigit(rightChar)) {
                r--;
                continue;
            }
            if(Character.toLowerCase(leftChar) != Character.toLowerCase(rightChar)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}