import java.util.Scanner;
public class CreatingComparator{
		public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.println("Enter a four digit integer");
	int digit = input.nextInt(); 

	int firstnum = digit % 10 ;
	int secondnum =digit / 1000;
	int thirdnum = digit /10 % 10
	int fourthnum = digit / 100 % 10

	int first_num = firstnum + 7;
	int second_num = secondnum +7;
	int third_num = thirdnum + 7;
	int fourth_num = fouthnum + 7;

	int newvalue = first_num + second_num + third_num +fourth_num;
	
	int new_value = newvalue / 10
	