#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define M_PI 3.14159265358979323846

double deg_to_rad(double deg) { return deg * (M_PI / 180.0); }

double rad_to_deg(double rad) { return rad * (180.0 / M_PI); }

int *solve(int a, int b, int c, int alpha, int beta, int gamma) {
  int *solution = malloc(4 * sizeof(int));
  if (!solution)
    return NULL;

  double alpha_rad = deg_to_rad((double)alpha);
  double beta_rad = deg_to_rad((double)beta);
  double gamma_rad = deg_to_rad((double)gamma);
  double c_x = (double)a * cos(alpha_rad) - (double)b * sin(beta_rad) -
               (double)c * cos(gamma_rad);
  double c_y = (double)a * sin(alpha_rad) + (double)b * cos(beta_rad) -
               (double)c * sin(gamma_rad);

  solution[0] = (int)round(hypot(c_x, c_y));

  double angle = rad_to_deg(atan2(c_y, c_x));
  int sec = (int)(angle * 3600);
  int deg = sec / 3600;
  sec = sec % 3600;
  int min = sec / 60;
  sec %= 60;
  solution[1] = deg;
  solution[2] = min;
  solution[3] = sec;

  return solution;
}
