import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		Integer[] arr = new Integer[N]; //reverseOrder() 사용하고 싶어서 Integer배열 사용
    
		for(int i=0;i<N;i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr, Comparator.reverseOrder()); //내림차순으로 정렬했다. 최댓값을 가지려면 큰 수 - 작은 수
		
		long result = 0;        //int로 선언했더니 틀렸다고 나옴. 
		                        //문제에 저렇게 100,000이라고 했다는 것은 클 것이라는 건데 long하니까 통과됨.. 공부하자
    for(int i=0;i<N;i++) { 
			int temp = arr[i]-i;  //문제대로라면 돈 - (등수-1) 이지만 애초에 저장할 때 -1이된 상태로 배열에 저장했기에
			if(temp<0) break;     //break : 내림차순으로 정렬했는데 음수가 나오면 결국 다음 수들도 음수일 것! 시간복잡도를 줄이기 위해
			result += temp;
		}
		
		bw.write(result+"");
		bw.flush();
		bw.close();
			
	}
}
