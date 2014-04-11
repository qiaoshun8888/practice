package Leetcode;

/**
 * Created by xin on 3/9/14.
 */
public class PalindromeNumber {
    public boolean isPalindrome(int x) {
        // get the length
        if (x < 0) return false;
        long n = 10;
        while (x >= n) {
            n *= 10;
        }
        n /= 10;
        while (n  > 0) {
            if (x % 10 != (x / n) % 10) return false;
            x /= 10;
            n /= 100;
        }
        return true;
    }

    public static void main(String[] args) {
        PalindromeNumber s = new PalindromeNumber();
        System.out.println(s.isPalindrome(2147483647));//749947
    }
}
