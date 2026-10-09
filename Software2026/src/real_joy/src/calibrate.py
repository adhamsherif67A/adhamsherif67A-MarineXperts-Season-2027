import cv2
import numpy as np
import glob
import os
import yaml

# ------------ User Parameters ------------
folder = "./images/"          # فولدر الصور
h_edges = 9                   # عدد internal corners horizontal
v_edges = 6                   # عدد internal corners vertical
square_size = 25.0            # حجم مربع checkerboard بالمليمتر
serial = 123                  # رقم تسلسلي لحفظ الملفات
max_repr_error = 1.0          # للتحقق من الجودة
verbose = True
# ---------------------------------------

# ---------------- Read Images ----------------
left_images = sorted(glob.glob(os.path.join(folder, "image_left_*.png")))
right_images = sorted(glob.glob(os.path.join(folder, "image_right_*.png")))

if len(left_images) != len(right_images) or len(left_images) == 0:
    raise RuntimeError("Check left/right images: counts mismatch or empty folder")

print(f"Found {len(left_images)} stereo image pairs")

# ---------------- Prepare Object Points ----------------
objp = np.zeros((v_edges*h_edges,3), np.float32)
objp[:,:2] = np.mgrid[0:h_edges,0:v_edges].T.reshape(-1,2)
objp *= square_size  # scale by square size

objpoints = []  # 3d points
imgpoints_left = []  # 2d points left
imgpoints_right = []  # 2d points right

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# ---------------- Detect Corners ----------------
for i, (lpath, rpath) in enumerate(zip(left_images, right_images)):
    img_l = cv2.imread(lpath, cv2.IMREAD_GRAYSCALE)
    img_r = cv2.imread(rpath, cv2.IMREAD_GRAYSCALE)

    ret_l, corners_l = cv2.findChessboardCorners(img_l, (h_edges,v_edges))
    ret_r, corners_r = cv2.findChessboardCorners(img_r, (h_edges,v_edges))

    if ret_l and ret_r:
        objpoints.append(objp)

        corners_l = cv2.cornerSubPix(img_l, corners_l, (5,5), (-1,-1), criteria)
        corners_r = cv2.cornerSubPix(img_r, corners_r, (5,5), (-1,-1), criteria)

        imgpoints_left.append(corners_l)
        imgpoints_right.append(corners_r)

        if verbose:
            cv2.drawChessboardCorners(img_l, (h_edges,v_edges), corners_l, ret_l)
            cv2.drawChessboardCorners(img_r, (h_edges,v_edges), corners_r, ret_r)
            cv2.imshow('Left', img_l)
            cv2.imshow('Right', img_r)
            cv2.waitKey(50)
    else:
        print(f"- Checkerboard not detected in pair #{i}")

cv2.destroyAllWindows()

# ---------------- Mono Calibration ----------------
img_shape = img_l.shape[::-1]

ret_l, mtx_l, dist_l, rvecs_l, tvecs_l = cv2.calibrateCamera(objpoints, imgpoints_left, img_shape, None, None)
ret_r, mtx_r, dist_r, rvecs_r, tvecs_r = cv2.calibrateCamera(objpoints, imgpoints_right, img_shape, None, None)

# ---------------- Stereo Calibration ----------------
flags = cv2.CALIB_FIX_INTRINSIC
ret_stereo, mtx_l, dist_l, mtx_r, dist_r, R, T, E, F = cv2.stereoCalibrate(
    objpoints, imgpoints_left, imgpoints_right,
    mtx_l, dist_l, mtx_r, dist_r,
    img_shape,
    criteria=criteria,
    flags=flags
)

# ---------------- Save YAML ----------------
calib_file = f"zed_calibration_{serial}.yml"
data = {
    'Size': img_shape,
    'K_LEFT': mtx_l.tolist(),
    'D_LEFT': dist_l.tolist(),
    'K_RIGHT': mtx_r.tolist(),
    'D_RIGHT': dist_r.tolist(),
    'R': R.tolist(),
    'T': T.tolist()
}

with open(calib_file, 'w') as f:
    yaml.dump(data, f)

print(f"Calibration done! Saved to {calib_file}")

# Optional: print reprojection errors
def reprojection_error(objpoints, imgpoints, rvecs, tvecs, K, dist):
    total_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], K, dist)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        total_error += error
    return total_error/len(objpoints)

err_l = reprojection_error(objpoints, imgpoints_left, rvecs_l, tvecs_l, mtx_l, dist_l)
err_r = reprojection_error(objpoints, imgpoints_right, rvecs_r, tvecs_r, mtx_r, dist_r)
print(f"Reprojection Error - Left: {err_l:.4f} px, Right: {err_r:.4f} px")