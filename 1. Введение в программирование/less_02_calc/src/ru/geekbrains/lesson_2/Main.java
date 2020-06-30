package ru.geekbrains.lesson_2;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		System.out.println("Выберете операцию");
		System.out.println("1. Сложение");
		System.out.println("2. Вычитание");
		System.out.println("3. Умножение");
		System.out.println("4. Деление");
		Scanner sc = new Scanner(System.in);
		int operation = sc.nextInt();
		System.out.println("Введите первое число");
		int a = sc.nextInt();
		System.out.println("Введите второе число");
		int b = sc.nextInt();
		int res;
		if (operation == 1){
			res = a + b;
		}else if (operation == 2){
			res = a - b;
		}else if (operation == 3){
			res = a * b;
		}else{
			res = a / b;
		}
		System.out.println("Результат = " + res);
	}
}
