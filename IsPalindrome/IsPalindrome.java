package IsPalindrome;

public class IsPalindrome {
    public static void main(String[] args) {
        String s = "abb";
        System.out.println(solution(s));
    }

    public static boolean solution(String s) {
        String sNoSpaces = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        boolean result = false;
        if (sNoSpaces.length() <= 1) {
            result = true;
        } else {
            int start = 0;
            int end = sNoSpaces.length() - 1;
            while (start <= end) {
                if (sNoSpaces.charAt(start) == sNoSpaces.charAt(end)) {
                    result = true;

                } else {
                    result = false;
                    break;
                }

                start++;
                end--;
            }
        }

        return result;
    }
}
