// Stack Batch Removal

/* Implement a stack that accepts the following commands and performs the operations described:

   push value: Push integer value onto the top of the stack.
   pop: Pop the top element from the stack.
   remove_lower value: Remove all current elements in the stack less than value.
   remove_upper value: Remove all current elements in the stack more than value.
   
   Additionally, after each operation listed above,
   print the current top element of the stack on a new line.
   If no such element exists, print "EMPTY".
*/


import java.io.*;
import java.util.*;


class Stack {

    // Complete the 'solve' function below.
    private static void removeLower(Deque<Integer> stack, int value) {
        Deque<Integer> tempStack = new ArrayDeque<>();
        
        while (!stack.isEmpty()) {
            int top = stack.pop();
            if (top >= value) {
                tempStack.push(top);
            }
        }
        
        while (!tempStack.isEmpty()) {
            stack.push(tempStack.pop());
        }
    }
    
    private static void removeUpper(Deque<Integer> stack, int value) {
        Deque<Integer> tempStack = new ArrayDeque<>();
        
        while (!stack.isEmpty()) {
            int top = stack.pop();
            if (top <= value) {
                tempStack.push(top);
            }
        }
        
        while (!tempStack.isEmpty()) {
            stack.push(tempStack.pop());
        }
    }
    
    public static void solve(int n, String[] operations) {
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (String operation : operations) {
            String[] parts = operation.split(" ");
            String command = parts[0];
            
            switch (command) {
                case "push" ->                     {
                        int value = Integer.parseInt(parts[1]);
                        stack.push(value);
                    }
                case "pop" -> {
                    if (!stack.isEmpty()) {
                        stack.pop();
                    }
                }
                case "remove_lower" ->                     {
                        int value = Integer.parseInt(parts[1]);
                        removeLower(stack, value);
                    }
                case "remove_upper" ->                     {
                        int value = Integer.parseInt(parts[1]);
                        removeUpper(stack, value);
                    }
                default -> {
                }
            }
            
            if (stack.isEmpty()) {
                System.out.println("EMPTY");
            }
            
            else {
                System.out.println(stack.peek());
            }
        }
    }

}


public class stack_batch_removal {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] lines = new String[n];
        for (int i = 0; i < n; i++) {
            lines[i] = br.readLine();
        }
        Stack.solve(n, lines);
    }
}