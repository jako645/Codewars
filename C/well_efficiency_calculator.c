#include <stdbool.h>
#include <stddef.h>

extern const double FIELD[20][20];

bool is_efficient(size_t x, size_t y, double threshold) {
  double fields_sum = 0.0;
  for (int dx = -1; dx <= 1; dx++) {
    for (int dy = -1; dy <= 1; dy++) {
      int new_x = (int)x + dx;
      int new_y = (int)y + dy;
      if (new_x >= 0 && new_x < 20 && new_y >= 0 && new_y < 20) {
        fields_sum += FIELD[new_x][new_y];
      }
    }
  }
  return fields_sum >= threshold;
}
