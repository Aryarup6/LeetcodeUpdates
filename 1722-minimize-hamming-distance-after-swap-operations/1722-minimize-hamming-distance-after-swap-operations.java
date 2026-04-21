class Solution {
    int[] parent, rank;
    public int find(int u){
        if(parent[u] == u) return u;

        return parent[u] = find(parent[u]);
    }

    public void union(int u, int v){
        int lu = find(u), lv = find(v);
        if( lu != lv){
            if( rank[lu]> rank[lv])
                parent[lv] = lu;
            else if( rank[lu] < rank[lv])
                parent[lu] = lv;
            else{
                parent[lv] = lu;
                rank[lu]++;
            }
        }
    } 

    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.length;
        parent = new int[n];
        rank = new int[n];
        for( int i = 0; i < n; i++) parent[i] = i;

        for( int[] swap : allowedSwaps){
            union(swap[0], swap[1]);
        }

        HashMap<Integer, Integer>[] maps = new HashMap[n];
        for( int i = 0; i < n; i++){
            int root = find(i);
            if( maps[root] == null) maps[root] = new HashMap<>();
            maps[root].put(source[i], maps[root].getOrDefault(source[i], 0)+1);
        }

        int hd = 0;
        for( int i = 0; i < n; i++){
            int root = find(i);
            if( maps[root].containsKey(target[i])){
                int freq = maps[root].get(target[i]);
                if( freq == 1)
                    maps[root].remove(target[i]);
                else
                    maps[root].put(target[i], freq-1);
            }else{
                hd++;
            }
        }
        return hd;
    }
}