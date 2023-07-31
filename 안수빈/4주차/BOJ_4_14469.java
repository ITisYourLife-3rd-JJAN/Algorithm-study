import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException  {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int endTime = 0;
        int cowArr[][] = new int[N][2]; //[n][0] 도착시간, [n][1] 검문시간

        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            cowArr[i][0] = Integer.parseInt(st.nextToken()); //도착시간
            cowArr[i][1] = Integer.parseInt(st.nextToken());  //검문시간
        }

        Arrays.sort(cowArr, (o1,o2)-> o1[0]-o2[0]);
        
        for(int i=0;i<N;i++){
            if(endTime < cowArr[i][0]){  //이전 끝난시간이 다음 소 도착시간보다 작다면
                endTime=cowArr[i][0]+cowArr[i][1];
            }
            else //이전 끝난시간이 다음 소 도착시간보다 크다면
                endTime += cowArr[i][1];
        }
        bw.write(endTime+"");
        bw.flush();
        bw.close();
    }
}
