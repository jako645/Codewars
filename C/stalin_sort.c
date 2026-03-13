#include <stdio.h>

void delete_element(int idx, size_t *length, int array[*length]) {
  for (int j = idx + 1; j < (int)*length - 1; j++) {
    array[j] = array[j + 1];
  }
  (*length)--;
}

void stalin_sort(size_t *length, int array[*length]) {
  for (int i = 0; i < (int)*length - 1; i++) {
    if (array[i + 1] < array[i]) {
      delete_element(i, length, array);
      i--;
    }
  }
}
