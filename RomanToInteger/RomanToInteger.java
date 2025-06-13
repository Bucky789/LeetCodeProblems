package RomanToInteger;

import java.util.*;

public class RomanToInteger {
    public static void main(String[] args) {
        String s = "IV";
        System.out.println(solution(s));
    }

    public static int solution(String s) {
      Map<Character, Integer> map = new HashMap();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        int returnNum = 0;
        for(int i = 0; i < s.length()-1; i++){
            if(map.get(s.charAt(i)) < map.get(s.charAt(i+1))){
                returnNum -= map.get(s.charAt(i));
            }
            else{
                returnNum += map.get(s.charAt(i));
            } 
        }
        return returnNum + map.get(s.charAt(s.length()-1));
    }
}
