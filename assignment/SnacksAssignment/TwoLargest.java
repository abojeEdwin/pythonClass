import java.util.Scanner;
public class TwoLargest{
		public static void main(String[] args){
	Scanner input = new Scanner(System.in);
int largest = Integer.MIN_VALUE;
int secondlargest = integer.MIN_VALUE;

System.out.println("Enter 10 numbers:");
for (int i = ; i< 10; i++) {
int number = input.nextInt();

if(numbers > largest) {
	secondlargest = largest;
	largest = number;
}else if (number > secondlargest) {
	secondLaegest = number;
}
}
}
