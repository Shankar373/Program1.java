import java.util.Scanner;
public class Program3 {
    public static void generateModifiedOddSeries(int a) {
        for (int i = 0; i < (a + 1) / 2; i++) {
            System.out.print((2 * i + 1) + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer:");
        int a = sc.nextInt();
        generateModifiedOddSeries(a);
    }
}
