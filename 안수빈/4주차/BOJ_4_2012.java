import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		int[] predict = new int[N]; //예측등수
		long result = 0;
		
		for(int i=0;i<N;i++) {
			predict[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(predict); //오름차순 정렬
		
		for(int i=0;i<N;i++) {  //불만도가 적으려면 큰수-큰수 , 작은 수-작은 수 : 최대한 본인 등수와 가까운 등수를 줘야한다.
			result += Math.abs(predict[i]-(i+1));  // |예측등수 - (i+1 : 실제등수) |
		}
		
		bw.write(result+"");
		bw.flush();
		bw.close();
	}

}
