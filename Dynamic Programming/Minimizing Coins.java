
/*
Problem Link: https://cses.fi/problemset/task/1634
 */
import java.util.*;

public class Solution {

    public static int minCoins(int x, int[] coins) {
        int[] dp = new int[x + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i <= x; i++) {
            for (int coin : coins) {
                if (coin <= i && dp[i - coin] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[x] == Integer.MAX_VALUE ? -1 : dp[x];
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int x = scan.nextInt();
        int coins[] = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = scan.nextInt();
        }
        System.out.println(minCoins(x, coins));
        scan.close();
    }
}
