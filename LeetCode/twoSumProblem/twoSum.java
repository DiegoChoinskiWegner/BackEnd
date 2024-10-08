import java.util.HashMap;
import java.util.Map;

public static void twoSum(String[] args) {
    
    public class SolutionPropose {
        int target;
        int nums[];


        public int[] twoSum(int[] nums, int target){
            this.nums = nums;
            this.target = target;
            int num_index_map[];
            num_index_map = new int[nums.length];
            
            for (int i = 0; i < nums.length; i++){
                int complement = target - nums[i];
                for (int j = i + 1; j < nums.length; j++){
                    if (nums[j] == complement){
                        return new int[]{i, j};
                    }
                }
            }
        }
    }



    class SolutionSugestedAI {
        public int[] twoSum(int[] nums, int target) {
            Map<Integer, Integer> num_index_map = new HashMap<>();
            for (int i = 0; i < nums.length; i++) {
                int complement = target - nums[i];
                if (num_index_map.containsKey(complement)) {
                    return new int[] { num_index_map.get(complement), i };
                }
                num_index_map.put(nums[i], i);
            }
            return new int[] {};
        }
    }
}