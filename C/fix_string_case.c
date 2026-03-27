#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>


char *solve(const char *str) {
  
  int str_length = strlen(str);
  int up_case_num = 0;
  for (int i = 0; i < str_length; i++) {
    if (isupper(str[i])) {
      up_case_num += 1;
    }
  }

  char *new_str = calloc((size_t)str_length + 1, sizeof(char));

  int i = 0;
  if (up_case_num > str_length / 2) {
    while (str[i] != '\0') {
      new_str[i] = (char)toupper((unsigned char)str[i]);
      i += 1;
    }
  } else {
    while (str[i] != '\0') {
      new_str[i] = (char)tolower((unsigned char)str[i]);
      i += 1;
    }
  }

  return new_str;
}
