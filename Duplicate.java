import java.util.*;

public class Duplicate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcases = sc.nextInt();
        for (int i = 0; i < testcases; i++) {
            int size = sc.nextInt();
            int arr[] = new int[size];
            for (int j = 0; j < size; j++) {
                arr[j] = sc.nextInt();
            }
            Set<Integer> number = new HashSet<>();
            boolean isNumber = false;
            for (int k = 0; k < arr.length; k++) {
                if (number.contains(arr[k])) {
                    isNumber = true;
                    System.out.println(arr[k]);
                } else {
                    number.add(arr[k]);
                }
            }
            if (!isNumber) {
                System.out.println("no duplicates");
            }

        }
        sc.close();

    }
}