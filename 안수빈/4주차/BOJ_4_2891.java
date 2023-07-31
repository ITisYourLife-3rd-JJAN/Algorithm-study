import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken()); //팀의 수
		int S = Integer.parseInt(st.nextToken()); //손상된 팀의 수
		int R = Integer.parseInt(st.nextToken()); //카약 더있는 팀의 수
		int[] team = new int[N];
		int result = 0;
		
		Arrays.fill(team, 1); //팀이 보유한 카약 수 1로 초기화
		
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<S;i++) {
			int index = Integer.parseInt(st.nextToken())-1; 
			team[index]--;  //손상된 팀이면 1을 빼준다
		}
		
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<R;i++) {
			int index = Integer.parseInt(st.nextToken())-1;
			team[index]++; //여분 있는 팀이면 1을 더해준다
		}
		
		for(int i=0;i<N-1;i++) { //+-1 비교해서 빌려줄 수 있는지에대헤 판단해야함
			if(team[i] == 0 && team[i+1] == 2) { //손상된 팀이 앞번호
				team[i]++;
				team[i+1]--;
			}
			else if(team[i+1] == 0 && team[i] == 2) { //손상된 팀이 뒷번호
				team[i+1]++;
				team[i]--;
			}
		}
		
		for(int t:team) { //카약 수 0인 팀 수를 찾아서 출력값++
			if(t==0) result++;
		}
		
		bw.write(result+"");
		bw.flush();
		bw.close();
		
	}
}
