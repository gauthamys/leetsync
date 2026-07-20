class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Set<Character>> rowSet = new HashMap<>();
        HashMap<Integer, Set<Character>> colSet = new HashMap<>();
        HashMap<Integer, Set<Character>> subSet = new HashMap<>();

        for (int i=0; i<9; i++) {
            rowSet.put(i, new HashSet<>());
            colSet.put(i, new HashSet<>());
            subSet.put(i, new HashSet<>());
        }

        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                char ch = board[i][j];
                int subIndex = (3 * (j / 3)) + (i / 3);

                if (ch == '.') continue;
                if (rowSet.get(i).contains(ch)) return false;
                if (colSet.get(j).contains(ch)) return false;
                if (subSet.get(subIndex).contains(ch)) return false;

                rowSet.get(i).add(ch);
                colSet.get(j).add(ch);
                subSet.get(subIndex).add(ch);
            }
        }
        
        return true;
    }
}