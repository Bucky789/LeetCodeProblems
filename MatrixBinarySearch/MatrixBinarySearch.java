package MatrixBinarySearch;

public class MatrixBinarySearch {
     public static boolean solution(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int top = 0, bottom = rows - 1;
        while (top <= bottom) {
            int row = (top + bottom) / 2;
            if (target > matrix[row][cols - 1]) {
                top = row + 1;
            } else if (target < matrix[row][0]) {
                bottom = row - 1;
            } else {
                break;
            }
        }

        if (!(top <= bottom)) {
            return false;
        }
        int row = (top + bottom) / 2;
        int l = 0, r = cols - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (target > matrix[row][m]) {
                l = m + 1;
            } else if (target < matrix[row][m]) {
                r = m - 1;
            } else {
                return true;
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 4, 8},
            {10, 11, 12, 13},
            {14, 20, 30, 40}
        };
        int target = 10;

        System.out.println(solution(matrix, target));
    }
}
