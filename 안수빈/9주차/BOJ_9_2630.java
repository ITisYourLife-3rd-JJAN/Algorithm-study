import java.util.*;
import java.io.*;

public class Main {
	
	static int paperMap[][];
	static int white = 0; //하얀색
	static int blue = 0; //파란색
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		//2의 제곱(2~128 중 하나)
		
		paperMap = new int[N][N];
		
		for(int i=0;i<N;i++) { //입력 받고
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<N;j++) {
				paperMap[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		countPaper(0,0,N);
		
		bw.write(white+"\n"+blue);
		bw.flush();
		bw.close();
	}
	
	
	public static void countPaper(int row, int col, int size) {
		if(checkPaper(row, col, size)) { //색 확인하기
			if(paperMap[row][col] == 1) blue++;
			else white++;
			return; 
		}

    //checkPaper가 false가 나와서 여기 도달했음
    //true면 return 만나서 여기 안왔을거
		
		int cutSize = size/2; //2의 제곱이니까 
		
		countPaper(row, col, cutSize); // 제2사분면
		countPaper(row, col+cutSize, cutSize); //제 1사분면
		countPaper(row+cutSize, col, cutSize); // 제 3사분면
		countPaper(row+cutSize, col+cutSize, cutSize);//제 4사분면
	}
	
	public static boolean checkPaper(int row, int col, int size) {
		for(int i=row;i<row+size;i++) { //(0,0)에서 시작하면 (2,2)전까지만
			for(int j=col;j<col+size;j++) {
				if(paperMap[i][j] != paperMap[row][col])
					return false;
			}
		}
		return true;
	}
}
