package training;

public class Fibo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 0; i <= 10; i++) {
			System.out.println("i=" + i + " / " + fibo(i));
		}
	}

	public static int fibo(int n) {
		if (n <= 1) {
			return 1;
		} else {
			return fibo(n - 1) + fibo(n - 2);
		}
	}
}
