import sys
import cv2
import numpy as np
import ArducamDepthCamera as ac
import json
import math
print(dir(ac))

MAX_DISTANCE = 2

def process_frame(depth_buf: np.ndarray, amplitude_buf: np.ndarray) -> np.ndarray:
        
    depth_buf = np.nan_to_num(depth_buf)

    amplitude_buf[amplitude_buf<=7] = 0
    amplitude_buf[amplitude_buf>7] = 255

    depth_buf = (1 - (depth_buf/MAX_DISTANCE)) * 255
    depth_buf = np.clip(depth_buf, 0, 255)
    result_frame = depth_buf.astype(np.uint8)  & amplitude_buf.astype(np.uint8)
    return result_frame 
def depth_data_to_pointcloud(depth_data: np.ndarray, amplitude_data: np.ndarray, min_distance=0.1, max_distance=4):
    height, width = depth_data.shape
    y, x = np.mgrid[0:height, 0:width]
    x = x.astype(np.float32)
    y = y.astype(np.float32)
    z = depth_data.astype(np.float32)
    fx = 240 / (2 * np.tan(0.5 * np.pi * 64.3 / 180))
    fy = 180 / (2 * np.tan(0.5 * np.pi * 50.4 / 180))
    x = ((120 - x) / fx) * z
    y = ((90 - y) / fy) * z
    point_cloud = np.stack([x, y, z], axis=-1)
    point_cloud = point_cloud.reshape(-1, 3)

    amplitude_data = amplitude_data.reshape(-1)
    valid_points = (point_cloud[:, 2] >= min_distance) & (point_cloud[:, 2] <= max_distance) & (amplitude_data > 30)

    point_cloud = point_cloud[valid_points]

    return point_cloud

def point_cloud_to_json(point_cloud):
    json_data = {'points': []}
    
    for point in point_cloud:
        json_data['points'].append({'x': float(point[0]), 'y': float(point[1]), 'z': float(point[2])})
        
    return json_data
class UserRect():
    def __init__(self) -> None:
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

selectRect = UserRect()

followRect = UserRect()

def on_mouse(event, x, y, flags, param):
    global selectRect,followRect
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pass

    elif event == cv2.EVENT_LBUTTONUP:
        selectRect.start_x = x - 4 if x - 4 > 0 else 0
        selectRect.start_y = y - 4 if y - 4 > 0 else 0
        selectRect.end_x = x + 4 if x + 4 < 240 else 240
        selectRect.end_y=  y + 4 if y + 4 < 180 else 180
    else:
        followRect.start_x = x - 4 if x - 4 > 0 else 0
        followRect.start_y = y - 4 if y - 4 > 0 else 0
        followRect.end_x = x + 4 if x + 4 < 240 else 240
        followRect.end_y = y + 4 if y + 4 < 180 else 180
        
def usage(argv0):
    print("Usage: python "+argv0+" [options]")
    print("Available options are:")
    print(" -d        Choose the video to use")


if __name__ == "__main__":
    cam = ac.ArducamCamera()
    if cam.init(ac.TOFConnect.CSI,0) != 0 :
        print("initialization failed")
    if cam.start(ac.TOFOutput.DEPTH) != 0 :
        print("Failed to start camera")
    cam.setControl(ac.TOFControl.RANG,MAX_DISTANCE)
    cv2.namedWindow("preview", cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback("preview",on_mouse)
    while True:
        frame = cam.requestFrame(200)
        if frame != None:
            depth_buf = frame.getDepthData()
            amplitude_buf = frame.getAmplitudeData()
            cam.releaseFrame(frame)
            amplitude_buf*=(255/1024)
            amplitude_buf = np.clip(amplitude_buf, 0, 255)
            point_cloud = depth_data_to_pointcloud(depth_buf, amplitude_buf)

            # Convert the point cloud data to JSON format
            point_cloud_json = point_cloud_to_json(point_cloud)

            # Save the JSON data to a file
            with open('static/pointcloud.json', 'w') as outfile:
                json.dump(point_cloud_json, outfile)
            cv2.imshow("preview_amplitude", amplitude_buf.astype(np.uint8))
            #print("select Rect distance:",np.mean(depth_buf[selectRect.start_y:selectRect.end_y,selectRect.start_x:selectRect.end_x]))
            result_image = process_frame(depth_buf,amplitude_buf)
            result_image = cv2.applyColorMap(result_image, cv2.COLORMAP_JET)
            cv2.rectangle(result_image,(selectRect.start_x,selectRect.start_y),(selectRect.end_x,selectRect.end_y),(128,128,128), 1)
            cv2.rectangle(result_image,(followRect.start_x,followRect.start_y),(followRect.end_x,followRect.end_y),(255,255,255), 1)
    
            cv2.imshow("preview",result_image)

            key = cv2.waitKey(1)
            if key == ord("q"):
                exit_ = True
                cam.stop()
                sys.exit(0)
