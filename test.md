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

3. Assume we detected several pairs of points of two images taken from the same camera in different positions, how to calculate the distance of the two camera positions? (camera intrinsics are provided)

    a) You can't, because the result is up to scale
    
    b) use epipolar constraint to calculate fundamental matrix or essential matrix 
    
    c) use PnP
    
    d) use triangulate
    
