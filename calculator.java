public class calculator {

    private static int addition(int a , int b){
        int answer = a + b;
        return answer;

    }
    private static int subtraction(int a, int b){
        int answer = a - b;
        return answer;

    }
    private static int multiplication(int a, int b){
        int answer = a * b;
        return answer;
    }
    private static int division(int a , int b){
        int answer = a / b;
        return answer;
    }
    
    public static void main(String[] args){
        String choice= args[0];
        switch(choice){
            case "addition":
                int firstValue = Integer.parseInt(args[1]);
                int secondValue= Integer.parseInt(args[2]);
                int answer = addition(firstValue,secondValue);
                System.out.println(answer);
            case "subtraction":
                int firstValue1 = Integer.parseInt(args[1]);
                int secondValue1= Integer.parseInt(args[2]);
                int answer1 = subtraction(firstValue1,secondValue1);
                System.out.println(answer1);
            case "multiplication":
                int firstValue2 = Integer.parseInt(args[1]);
                int secondValue2= Integer.parseInt(args[2]);
                int answer2 = multiplication(firstValue2,secondValue2);
                System.out.println(answer2);
            case "division":
                int firstValue3 = Integer.parseInt(args[1]);
                int secondValue3= Integer.parseInt(args[2]);
                int answer3 = division(firstValue3,secondValue3);
                System.out.println(answer3);

        }
        int firstValue = Integer.parseInt(args[1]);
        int secondValue = Integer.parseInt(args[2]);
        int answer = addition(firstValue,secondValue);
        System.out.println(answer);

    }
}
