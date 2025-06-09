package ContainsDuplicate;

import java.util.*;
public class ContainsDuplicate {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5};
        System.out.println(solution(nums));
    }

    public static boolean solution(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            } else {
                seen.add(num);
            }
        }
        return false;
    }
}
