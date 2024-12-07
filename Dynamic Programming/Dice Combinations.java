
/*
Problem Link: https://cses.fi/problemset/task/1633/
 */
import java.util.*;

public class Solution {
    public static int countWays(int n) {
        int mod = 1000000007;
        int dp[] = new int[n + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= 6; j++) {
                if (i - j >= 0) {
                    dp[i] = (dp[i] + dp[i - j]) % mod;
                }
            }
        }
        return dp[n] % mod;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.println(countWays(n));
        scan.close();
    }
}
