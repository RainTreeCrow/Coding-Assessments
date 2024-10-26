// Rock Jumping

/* You are standing on the left bank of a river that is width units wide,
   and you're aiming to reach the right bank.
   The left bank is located at x = 0 and the right bank is located at x = width.
   There are several rocks in the river at various x coordinates between the banks,
   each with a specific height.
   You can jump between rocks or directly to the right bank.
   The cost to jump between two locations is given by the square of the distance between them.

   The water level is rising over time.
   Once the water reaches a certain level,
   some rocks will be submerged and can no longer be used for jumping.
   A rock is considered submerged if the water level is higher than its height.
   The water stops rising once you start your first jump.

   As additional constraints, we have a maximum jump distance maxJump,
   and there is a maximum total energy maxEnergy that you can use to cross the river.
   Thus, the total energy cost of all jumps should not exceed maxEnergy.
   Your task is to determine the maximum water height
   at which you can still reach the other side of the river
   without exceeding the maximum energy maxEnergy,
   considering the constraints provided.

   Function Description
   You are provided with four integers:
   width (the width of the river),
   numRocks (the number of rocks),
   maxJump (the maximum jump distance), and
   maxEnergy (the maximum total energy).

   Additionally, two arrays are provided containing integers:
   xi (the x-coordinate of the rocks) and
   height (the height of the rocks).
   Rocks are located strictly between the banks.

   Returns
   Return a single integer representing the maximum water height
   at which you can still reach the other side of the river.
   If it is impossible to reach the other side, output -1.
   If it will always be possible to reach the other side, output 1000.
*/


import java.io.*;
import java.util.*;


class RockJump {

    /*
     * Complete the 'maximumWaterHeight' function below.
     *
     * The function is expected to return an INTEGER.
     */
    
    private static boolean canCross(int width, int maxJump, long maxEnergy, int numRocks, int[] x, int[] heights, int waterLevel) {
        List<Integer> validRocks = new ArrayList<>();
        validRocks.add(0);
        for (int i = 0; i < numRocks; i++) {
            if (heights[i] >= waterLevel) {
                validRocks.add(x[i]);
            }
        }
        validRocks.add(width);
        
        int[] energyUsed = new int[validRocks.size()];
        Arrays.fill(energyUsed, Integer.MAX_VALUE);
        energyUsed[0] = 0;
        
        for (int currentIndex = 0; currentIndex < validRocks.size() - 1; currentIndex++) {
            int currentEnergy = energyUsed[currentIndex];
            
            if (currentEnergy > maxEnergy) {
                continue;
            }
            
            for (int nextIndex = currentIndex + 1; nextIndex < validRocks.size(); nextIndex++) {
                int jumpDistance = validRocks.get(nextIndex) - validRocks.get(currentIndex);
                if (jumpDistance <= maxJump) {
                    int newEnergy = currentEnergy + jumpDistance * jumpDistance;
                    if (newEnergy <= energyUsed[nextIndex]) {
                        energyUsed[nextIndex] = newEnergy;
                    }
                }
                else {
                    break;
                }
            }
        }
        return energyUsed[validRocks.size() - 1] <= maxEnergy;
    }

    public static int maximumWaterHeight(int width, int maxJump, long maxEnergy, int numRocks, int[] x, int[] heights) {
        if (width <= maxJump && width * width <= maxEnergy) {
            return 1000000000;
        }
        
        TreeSet<Integer> uniqueHeights = new TreeSet<>();
        for (int height : heights) {
            uniqueHeights.add(height);
        }
        List<Integer> sortedHeights = new ArrayList<>(uniqueHeights);
        
        int low = 0;
        int high = sortedHeights.size() - 1;
        int result = -1;
        
        while (low <= high) {
            int middle = (low + high) / 2;
            int waterLevel = sortedHeights.get(middle);
            
            if (canCross(width, maxJump, maxEnergy, numRocks, x, heights, waterLevel)) {
                result = waterLevel;
                low = middle + 1;
            }
            else {
                high = middle - 1;
            }
        }
        
        return result;
    }

}


public class rock_jumping {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // Read the initial parameters
        String[] line = br.readLine().split(" ");
        int width = Integer.parseInt(line[0]);
        int maxJump = Integer.parseInt(line[1]);
        long maxEnergy = Long.parseLong(line[2]);
        int numRocks = Integer.parseInt(line[3]);

        // Read the positions and heights of the rocks
        int[] x = new int[numRocks];
        int[] heights = new int[numRocks];
        for (int i = 0; i < numRocks; i++) {
            line = br.readLine().split(" ");
            x[i] = Integer.parseInt(line[0]);
            heights[i] = Integer.parseInt(line[1]);
        }

        // Call the function to get the result
        int result = RockJump.maximumWaterHeight(width, maxJump, maxEnergy, numRocks, x, heights);

        // Output the result to the console
        System.out.println(result);
    }
}