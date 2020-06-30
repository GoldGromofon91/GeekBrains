package ru.geekbrains.lesson_4;

import java.util.Scanner;

public class Main {
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println(" Ваша задача угадать число!");
        for (int i = 10; i <=30; i += 10){
            playlevel(i);
            System.out.println("Вы выйграли раунд!");
        }
        System.out.println("Вы выйграли игру!");
        sc.close();
    }
    private static void playlevel (int range) {
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
    }
}
