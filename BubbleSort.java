package training;

import java.util.Arrays;
import java.util.Random;

public class BubbleSort {
	public static void main(String[] args) {
		int[] array = new int[10];
		Random r = new Random();

		for (int i = 0; i < array.length; i++) {
			array[i] = r.nextInt(100);
		}

		System.out.println("depart " + Arrays.toString(array));

		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array.length - i - 1; j++) {
				if (array[j] > array[j + 1]) {
					int temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
				}
				System.out.println("i =" + i + "j=" + j + " " + Arrays.toString(array));
			}
		}
	}
}
