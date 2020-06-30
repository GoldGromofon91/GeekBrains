package ru.geekbrains.lesson_3;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(" Ваша задача угадать число!");
        int range = 50;
        int mnumb = (int) (Math.random() * range);
        while (true){
            System.out.println(" Угадайте число от 0 до " + range);
            int unumb = sc.nextInt();
            if (unumb == mnumb){
                System.out.println(" Вы угадали загаданное системой число!");
                break;
            }else if (unumb > mnumb){
                System.out.println(" Загаданное системой число,меньше!");
            }else {
                System.out.println(" Загаданное системой число, больше!");
            }
        }
        sc.close();
    }
}
