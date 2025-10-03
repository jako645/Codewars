#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define ASCII_TABLE_SIZE 256

bool makes_the_sentence(const char *characters, size_t count,
                        const char *sentence) {
  int freqArray[ASCII_TABLE_SIZE] = {0};
  int freqSentence[ASCII_TABLE_SIZE] = {0};

  for (unsigned i = 0; i < count; i++) {
    unsigned char c = characters[i];
    freqArray[c]++;
  }

  for (unsigned i = 0; sentence[i] != '\0'; i++) {
    unsigned char c = sentence[i];
    if (c != ' ') {
      freqSentence[c]++;
    }
  }

  for (unsigned i = 0; i < ASCII_TABLE_SIZE; i++) {
    if (freqSentence[i] != freqArray[i]) {
      return false;
    }
  }

  return true;
}
