public class MergeStringsAlternately{
    public static String mergeAlternately(String word1, String word2) {
        String ret = "";
        int s1Count = word1.length();
        int s2Count = word2.length();
        int index = 0;
        for (int i = 0; i < Math.min(s1Count, s2Count); i++) {

            ret = ret + word1.charAt(i);
            ret = ret + word2.charAt(i);
            index = i;
        }
        if (s1Count > s2Count) {
            ret = ret + word1.substring(index + 1);
        } else {
            ret = ret + word2.substring(index + 1);
        }

        return ret;
    }

    public static void main(String[] args) {
        String word1 = "ab";
        String word2 = "pqrs";
        System.out.println(mergeAlternately(word1, word2));
    }
}