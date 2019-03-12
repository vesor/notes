1. Assume L is the pose of camera in IMU coordinate, W is pose of IMU in world coordinate. 
Then what's the pose of camera in world coordinate?

a) X = W * L (not L * W, because Px = W * L * Pl, apply L first, then W.)
b) X = L * W
c) X = W * L.inverse
d) X = W.inverse * L

2. What can IMU measure? What can't be measured directly?

a) a, w; v, g;
b) v, w; a, g;
c) g, w; v, a;
d) a, v; w, g;

