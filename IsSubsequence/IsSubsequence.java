package IsSubsequence;
public class IsSubsequence {
    public static void main(String[] args) {
        String s = "abc", t = "ahbgdc";
        System.out.println(solution(s,t));
    }
    public static boolean solution(String s, String t) {
        int i = 0, j = 0;

        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++; 
            }
            j++; 
        }

        return i == s.length();  
    }
}
