#include <vector>
#include <queue>
using namespace std;

int rea4(char *buf4);

/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    /**
     * Reads n characters from the file and writes into buffer.
     * @param buffer Destination buffer
     * @param n Number of characters to read
     * @return The number of actual characters read
     */
    int read(char* buffer, int n) {
        int totalRead = 0; // Total number of characters read

        // Continue reading until we have read n characters or there is no more to read.
        while (totalRead < n) {
            // Refill the tempBuffer if it's empty
            if (bufferIndex == bufferSize) {
                bufferSize = read4(tempBuffer);
                bufferIndex = 0; // Reset buffer index
                // If no characters were read, we've reached the end of the file
                if (bufferSize == 0) break;
            }

            // Read from tempBuffer into buffer until we have read n characters 
            // or the tempBuffer is exhausted.
            while (totalRead < n && bufferIndex < bufferSize) {
                buffer[totalRead++] = tempBuffer[bufferIndex++];
            }
        }

        return totalRead; // Return the total number of characters read
    }

private:
    char tempBuffer[4]; // Temporary buffer to store read4 results
    int bufferIndex = 0; // Index for the next read character in tempBuffer
    int bufferSize = 0; // Represents how many characters read4 last read into tempBuffer
};