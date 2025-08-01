int read4(char *buf4);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        int total = 0;
        char buf4[4];
        while (total < n) {
            int count = read4(buf4);
            if (count == 0)
                break; // No more char to read

            for (int i = 0; i < count && total < n; ++i) {
                buf[total] = buf4[i];
                total++;
            }
        }
        return total;
        
    }
};