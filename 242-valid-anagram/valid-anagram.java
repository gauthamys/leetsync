class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sm = new HashMap<>();
        HashMap<Character, Integer> tm = new HashMap<>();

        for (int i=0; i<s.length(); i++) {
            char sc = s.charAt(i);
            sm.put(sc, sm.getOrDefault(sc, 0) + 1);
        }
        for (int j=0; j<t.length(); j++) {
            char tc = t.charAt(j);
            tm.put(tc, tm.getOrDefault(tc, 0) + 1);
        }

        return sm.equals(tm);
    }
}