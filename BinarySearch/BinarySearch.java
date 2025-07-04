package BinarySearch;

public class BinarySearch {
    public static int solution(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2; 

            if (nums[mid] == target) {
                return mid;
            } else if (target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1; 
    }

    public static void main(String[] args) {
        int[] nums = {-10, -3, 0, 5, 9, 12};
        int target = 9;

        System.out.println(solution(nums, target)); 
    }
}
