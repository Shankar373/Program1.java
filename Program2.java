import java.util.Scanner;
public class Program2 {
    public static void generateOddSeries(int a) {
        for (int i = 0; i < a; i++) {
            System.out.print((2 * i + 1) + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer:");
        int a = sc.nextInt();
        generateOddSeries(a);
    }
}
