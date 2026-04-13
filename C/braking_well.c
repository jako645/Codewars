#include <math.h>

#define REACTION_TIME 1
#define G 9.81

double kmph_to_mps(double kmph) { return (kmph * 5 / 18); }

double mps_to_kmph(double mps) { return (mps * 18 / 5); }

double dist(double v, double mu) {
  double v_mps = kmph_to_mps(v);
  double reaction_dist = v_mps * REACTION_TIME;
  double breaking_dist = v_mps * v_mps / (2 * mu * G);
  return reaction_dist + breaking_dist;
}

double speed(double d, double mu) {
  double mgt = mu * G * REACTION_TIME;
  double v = sqrt(mgt * mgt + 2.0 * mu * G * d) - mgt;
  return mps_to_kmph(v);
}
