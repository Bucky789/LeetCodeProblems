import java.util.*;



class TwoSum{
    public static void main(String args[]){
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        System.out.println(solution(nums, target));
    }

    public static List<Integer> solution(int[] nums, int target) {
        List<Integer> match = new ArrayList<>();
        Map<Integer, Integer> remainders = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (remainders.containsKey(complement)) {
                match.add(remainders.get(complement));
                match.add(i);
                break;
            } else {
                remainders.put(nums[i], i);
            }
        }

        return match;
    }
}
