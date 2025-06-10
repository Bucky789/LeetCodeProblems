package ValidAnagram;

import java.util.*;

public class ValidAnagram {
    public static void main(String[] args) {
        String s = "racecar";
        String t = "carrace";
        System.out.println(solution(s,t));
    }

     public static boolean solution(String s, String t) {
        Map<Character, Integer> sA = new HashMap<>();
        Map<Character, Integer> sB = new HashMap<>();
        boolean check = false;

        int sizeA = s.length();
        int sizeB = t.length();

        for (char c : s.toCharArray()) {
            sA.put(c, sA.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            sB.put(c, sB.getOrDefault(c, 0) + 1);
        }

        if (sizeA < sizeB) {
            for (char key : sB.keySet()) {
                if (sA.containsKey(key)) {
                    if (!sA.get(key).equals(sB.get(key))) {
                        return false;
                    } else {
                        check = true;
                    }
                } else {
                    return false;
                }
            }
        } else {
            for (char key : sA.keySet()) {
                if (sB.containsKey(key)) {
                    if (!sA.get(key).equals(sB.get(key))) {
                        return false;
                    } else {
                        check = true;
                    }
                } else {
                    return false;
                }
            }
        }

        return check;
    }
}
