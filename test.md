1. Assume L is the pose of camera in IMU coordinate, W is pose of IMU in world coordinate. 
Then what's the pose of camera in world coordinate? (All poses represented as 4x4 matrix R|t)

    a) X = W * L (not L * W, because Px = W * L * Pl, apply L first, then W.)

    b) X = L * W

    c) X = W * L.inverse

    d) X = W.inverse * L


2. What can IMU measure? What can't be measured directly? (a = acceleration, w = rotation angle, v = velocity, g = gravity)

    a) a, w; v, g;

    b) v, w; a, g;

    c) g, w; v, a;

    d) a, v; w, g;

3. Assume we detected several pairs of points of two images taken from the same camera in different positions, how to calculate the distance of the two camera positions? (camera intrinsics are provided)

    a) You can't, because the result is up to scale
    
    b) use epipolar constraint to calculate fundamental matrix or essential matrix 
    
    c) use PnP
    
    d) use triangulate
    
4. Assume there are two poses represented as (Eigen::Vector3d translation, Eigen::Quaterniond rotation), then the interpolated rotation in the middle point of the two poses is:

    a) rotation1.slerp(0.5, rotation2)
    
    b) (rotation1 + rotation2) / 2
    
    c) (rotation1.toRotationMatrix() + rotation2.toRotationMatrix()) / 2
    
    d) (rotation1.toRotationMatrix().eulerAngles(0, 1, 2) + rotation2.toRotationMatrix().eulerAngles(0, 1, 2)) / 2
    
5. what's the output of the following c++ code?

        Eigen::RowVector2d v1(1, 2);
        auto v2 = v1 / 2;
        v1 = v1 * 10;
        std::cout << v1 << ";" << v2 << std::endl;
        
    a) 10 20;  5 10
    
    b) 10 20;  0.5 1
    
    c)  5 10;  5 10
    
    d) compile error

6. If use Ceres to solve problem as the following code: 
    
        class MyFunctor
        {
        public:
            static ceres::CostFunction* Create() {
                return new ceres::AutoDiffCostFunction<MyFunctor, 1, 2>(new MyFunctor());
            }

            template <typename T>
            bool operator()(const T* const X, T* residuals) const {
                residuals[0] = T(1) - X[0] + T(2) - T(5) * X[1];
                std::cout << "==res: " << residuals[0] << std::endl;
                return true;
            }
        };
    what's the output may looks like?
    
    a) ==res: -0.00279986 and ==res: [-0.00279986 ; -1, -5]
    
    b) ==res: -0.00279986 and ==res: [-0.00279986 ; 1, 5]
    
    c) ==res: -1, -5
    
    d) ==res: -0.00279986

7. Assume two poses represented as R1,t1 and R2,t2, then the relative translation between the two poses is:

    a) t2 - R1 * t1
    b) t2 - t1
    c) t2 - R1.inverse() * t1
    d) (t2 - t1) * R1
    
