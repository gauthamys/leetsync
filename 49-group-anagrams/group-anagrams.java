class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> m = new HashMap<>();
        for (String s: strs) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            String sortedS = new String(charArray);
            m.putIfAbsent(sortedS, new ArrayList<>());
            m.get(sortedS).add(s);
        }
        return new ArrayList<>(m.values());
    }
}