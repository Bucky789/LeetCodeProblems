package CanPlaceFlowers;

import java.util.*;

public class CanPlaceFlowers {
    public static boolean soltion(int[] flowerbed, int n) {
    
        int flowers = 0;
        for(int i = 0; i < flowerbed.length ; i++){
            if (flowerbed[i] == 0) {
            boolean left = (i == 0) || (flowerbed[i - 1] == 0);
            boolean right = (i == flowerbed.length - 1) || (flowerbed[i + 1] == 0);

            if(left && right){
                flowerbed[i] = 1;
                flowers ++;
                if (flowers >= n) {
                        return true;
                    }
            }
            }
        }
        return flowers >= n;
    }

    public static void main(String[] args) {
        int[] flowerbed = {1, 0, 0, 0, 1};
        int n = 1;


        System.out.println(soltion(flowerbed,n));
    }
}
