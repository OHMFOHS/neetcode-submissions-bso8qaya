class Node {
    boolean isEnd;
    Node[] child;
    public Node() {
        isEnd = false;
        child = new Node[26];
    }
}

class PrefixTree {
    private Node root;
    public PrefixTree() {
        root = new Node();
    }

    public void insert(String word) {
        Node cur = root;
        for(int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if(cur.child[c-'a'] == null) {
                cur.child[c-'a'] = new Node();
            }
            cur = cur.child[c - 'a'];
        }
        cur.isEnd = true;
    }

    public boolean search(String word) {
        Node cur = root;
        for(int i = 0; i < word.length(); i++ ) {
            char c = word.charAt(i);
            if(cur.child[c-'a'] == null) {
                return false;
            }
            cur = cur.child[c-'a'];
        }
        if (!cur.isEnd) return false;
        return true;
    }

    public boolean startsWith(String prefix) {
        Node cur = root;
        for(int i = 0; i < prefix.length(); i++ ) {
            char c = prefix.charAt(i);
            if(cur.child[c-'a'] == null) {
                return false;
            }
            cur = cur.child[c-'a'];
        }
        return true;
    }
}
