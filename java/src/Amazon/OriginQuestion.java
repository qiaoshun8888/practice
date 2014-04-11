package Amazon;

import java.util.Collections;
import java.util.PriorityQueue;

/**
 * Created by xin on 3/14/14.
 */
public class OriginQuestion {
    public static class SimplePQ {
        PriorityQueue<Integer> queue;
        Integer min;
        int k;

        public SimplePQ(int k) {
            this.k = k;
            this.queue = new PriorityQueue<Integer>(k, Collections.reverseOrder());
        }

        public void offer(int distance) {
            if (this.queue.size() < this.k || distance < this.min) {
                this.queue.offer(distance);
                this.min = distance;
            }
        }

        public int peek() {
            return queue.peek();
        }
    }

    public static void main(String[] args) {
        SimplePQ spq = new SimplePQ(5);
        spq.offer(10);
        spq.offer(9);
        spq.offer(8);
        spq.offer(7);
        spq.offer(6);
        spq.offer(5);
        spq.offer(4);
        spq.offer(3);
        spq.offer(2);
        spq.offer(1);
        System.out.println(spq.peek());
    }
}
