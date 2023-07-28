import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
		int cnt=0; //결과
		int N = Integer.parseInt(br.readLine());
		int arr[] =new int[N]; // 추월했는지 확인하기 위한 출구쪽 입력을 담기위한 배열
    
		Map<String, Integer> car = new HashMap<>();
		for(int i=0;i<N;i++) {
			car.put(br.readLine(), i);
		}
    
		for(int i=0;i<N;i++) {
			String str = br.readLine();
			arr[i] = car.get(str); //출구쪽에서 나온 차가 입구에서는 몇번째로 들어갔는지 찾아서 배열에 넣어줌
		}
		for(int i=0;i<N-1;i++) {
			for(int j=i+1;j<N;j++) {
				if(arr[i]>arr[j]) { //출구쪽에서 i번째로 나온 차보다 늦게 나온 j번째 차가 사실은 입구 쪽에서 먼저 들어간 차였다면?! 
					cnt++; break;
				}
			}
		}
		
		bw.write(cnt+"");
		bw.flush();
		bw.close();
	}
}
