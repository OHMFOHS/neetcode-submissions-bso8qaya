class Node {
    boolean isEnd;
    Node[] child;
    public Node() {
        isEnd = false;
        child = new Node[26];
    }
}

class WordDictionary {
    Node root;
    public WordDictionary() {
        root = new Node();
    }

    public void addWord(String word) {
        Node cur = root;
        for(int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (cur.child[c-'a'] == null) {
                cur.child[c-'a'] = new Node();
            }
            cur = cur.child[c-'a'];
        }
        cur.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(word, root, 0);
    }

    private boolean dfs(String word, Node cur, int i) {
        if (cur == null) return false;
        if(i == word.length()) {
            return cur.isEnd;
        }

        char c = word.charAt(i);
        boolean res = false;
        if(c != '.') {
            return dfs(word, cur.child[c-'a'], i+1);
        } else {
            for(int j = 0; j < 26; j++) {
                if (cur.child[j] != null ) {
                    if(dfs(word, cur.child[j], i+1)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}
