import java.util.Scanner;


class Factorielle{  
    static int factorielle(int n){    
     if (n == 0)    
       return 1;    
     else    
       return(n * factorielle(n-1));    
    }

    public static void main(String args[]){  
     try{    
     System.out.print("Enter un entier : ");  
     Scanner scanner = new Scanner(System.in);  
     int number = 0;
     try{
      String temp_number = scanner.next(); 
      for(Character c : temp_number.toCharArray())
      {
         if(c == '.' || (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))
         {
            System.out.println("Entrer un entier en ligne de commande"); 
            return;
         }
      }
      number = Integer.parseInt(temp_number);
     }catch(Exception exa){
      System.out.println("L'entier entré est trop grand");  
      return;
     }
     if(number < 0)
     {
        System.out.println("L'entier est négatif ,la factorielle n'est pas défine");  
        return;
     }

      int fact = factorielle(number);   
      System.out.println("Factorielle "+number+" est: "+fact);    

     if(fact <= 0)
     {
        System.out.println("ArrayIndexOutOfBoundsException");
     }

     }catch(StackOverflowError exc){

        System.out.println("StackOverFlowExeption");

     }
   }
 
}  