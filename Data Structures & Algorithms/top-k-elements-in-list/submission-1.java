class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(freq.get(a), freq.get(b))
        );

        int[] out = new int[k];

        for(int num : nums) {
            int count = freq.getOrDefault(num, 0) + 1;
            freq.put(num, count);
        }

         for (int key : freq.keySet()) {
            heap.offer(key);
            if (heap.size() > k) heap.poll();
        }

        
        for (int i = k - 1; i >= 0; i--) { // optional: highest freq ends up later
            out[i] = heap.poll();
        }
        return out;
    }
}
