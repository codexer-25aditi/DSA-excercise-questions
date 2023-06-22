// Online Java Compiler
// Use this editor to write, compile and run your Java code online
//Largest Power of Prime
import java.util.*;


class HelloWorld {
    static int PowerPrime(int num,int p){
        int sum=0;
        while(num>p){
            int q=num/p;
            sum=sum+q;
            num=num/p;
            
        }
        return sum;
        
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        int p=sc.nextInt();
        System.out.println(PowerPrime(num,p));
    }
}