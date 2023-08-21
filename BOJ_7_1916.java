import java.util.*;
import java.io.*;

public class BOJ_7_1916 {
	private static final int infi = Integer.MAX_VALUE / 16;
    static int N;
    static int M;
    static int max = 1000 + 1;
    static int[][] graph = new int[max][max];
    static int[] dist = new int[max];

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        M = Integer.parseInt(bf.readLine());
        StringTokenizer st;
        graph = new int[N + 1][N + 1]; // 인덱스 1부터 사용하도록 수정

        for (int i = 0; i <= N; ++i) {
     	   for (int j = 0; j <= N; ++j) {
     		//자기 자신까지의 비용은 0
 			//if(i==j) graph[i][j]=0;
 			
 			//못가는 곳은 무한대의 비용
 			graph[i][j] = infi;
     	   }
        }
        for (int i = 0; i < M; ++i) {
            st = new StringTokenizer(bf.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
           
            graph[start][end] = cost;
        }

        st = new StringTokenizer(bf.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        System.out.println(dij(s, e));
    }

    static int dij(int s, int e) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        boolean[] visited = new boolean[max];
        
        for (int i = 0; i <= N; ++i) {
        	dist[i]=infi;
        }
        dist[s] = 0;
        
        // 최초 값은 start에서 start까지, 당연히 비용은 0
        pq.add(new int[]{0, s});

        while (!pq.isEmpty()) {
        	// 현재 위치의 int 배열[비용,정점]
    		int[] curr = pq.poll();
    		int u = curr[1];
    		
    		// 출발하려는 곳이 도착지가 되면 종료
    		if(u==e) return curr[0];
    		
           
    		// 방문배열 업데이트
            if (visited[u]) continue;
            
            visited[u] = true;
            
            // 현재 비용보다 더 최소 비용의 거리가 있으면 그 값으로 dist 배열 업데이트
            for (int v = 1; v <= N; ++v) {
                if (!visited[v] && dist[v] > dist[u] + graph[u][v]) {
                    dist[v] = dist[u] + graph[u][v];
                    pq.add(new int[]{dist[v], v});
                }
            }
        }
        return infi;
    }
}