import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_9_2630 {
	public static int[][] map;
	public static int white;
	public static int blue;
	
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        map = new int[N][N];
        StringTokenizer st;
        
        for (int i = 0; i < N; i++) {
        	st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        divide(0, 0, N);
        System.out.println(white);
        System.out.println(blue);
    }
    
    public static void divide(int row, int col, int size) {
    	if(colorCheck(row, col, size)) {
    		if(map[row][col]==0) white++;
    		else blue++;
    		
    		return;
    	}
    	
    	int newSize = size/2;
    	
    	divide(row, col, newSize); // 2사분면
    	divide(row, col+newSize, newSize); // 1사분면
    	divide(row+newSize, col, newSize); // 3사분면
    	divide(row+newSize, col+newSize, newSize); // 4사분면
    	
    }
    
    public static boolean colorCheck(int row, int col, int size) {
    	int color = map[row][col]; // 시작점(원점)의 색
    	
    	for(int i=row; i<row+size; i++) {
    		for (int j = col; j < col+size; j++) {
    			if(map[i][j]!=color) return false; // 시작점의 색이 무엇이든, 같지 않다면 false
			}
    	}
    	
    	return true;
    }
    
}