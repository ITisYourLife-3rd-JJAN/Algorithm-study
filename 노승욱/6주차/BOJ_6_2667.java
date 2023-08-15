import java.util.*;
import java.io.*;

public class BOJ_6_2667 {
    final static int MAX = 30;
    static boolean[][] graph;
    static boolean[][] visited;
    static int cnt;
    static int dirY[] = { 1, -1, 0, 0 };
    static int dirX[] = { 0, 0, 1, -1 };

    static void dfs(int y, int x) {
        visited[y][x] = true;
        cnt++;

        for (int i = 0; i < 4; i++) {
            int newY = y + dirY[i];
            int newX = x + dirX[i];
            if (!visited[newY][newX] && graph[newY][newX])
                dfs(newY, newX);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());

        graph = new boolean[MAX][MAX];
        visited = new boolean[MAX][MAX];

        for (int i = 1; i <= N; i++) {
            String s = bf.readLine();
            for (int j = 1; j <= N; j++)
                graph[i][j] = s.charAt(j - 1) == '1';
        }

        ArrayList<Integer> countList = new ArrayList<>();
        for (int i = 1; i <= N; i++)
            for (int j = 1; j <= N; j++)
                if (graph[i][j] && !visited[i][j]) {
                    cnt = 0;
                    dfs(i, j);
                    countList.add(cnt);
                }

        System.out.println(countList.size());
        Collections.sort(countList);
        for (int i = 0; i < countList.size(); i++)
            System.out.println(countList.get(i));
    }
}