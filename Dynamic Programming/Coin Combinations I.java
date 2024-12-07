/*
Problem Link: https://cses.fi/problemset/task/1635
*/

import java.util.*;

public class Solution {
    public static int countWays(int x, int[] coins) {
        int dp[] = new int[x + 1];
        Arrays.fill(dp, 0);

        dp[0] = 1;

        return dp[x];

    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int x = scan.nextInt();
        int coins[] = new int[x];
        for (int i = 0; i < x; i++) {
            coins[i] = scan.nextInt();
        }
        System.out.println(countWays(x, coins));
        scan.close();
    }
}
