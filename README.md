# OpenPose from Source Demo
 <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/jpg/openpose_banner.png" height="80%"/>

This repository demonstrates my personal project where I compiled and ran [CMU OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) from source to process custom video and image inputs for non-commercial research purposes. Through this project, I explored OpenPose's capabilities, including 2D pose estimation for body, hand, and face keypoints, while integrating various input types like webcam, videos and images. The repository also highlights key learnings, troubleshooting steps, and efficient usage of OpenPose for multi-person detection scenarios. This serves as a comprehensive guide for anyone looking to set up and utilize OpenPose from source for their own research or academic projects.

## Environment 
- Operating system: **Windows 10** 
- GPU: **NVIDIA GeForce RTX 4070**
- **Visual Studio 2019 Community**
- CUDA: **12.0** 
- cuDNN: **cudnn-12.0-windows-x86_64-v8.8.0.121** 

## Contents

1. [Results](#results)
2. [Installation](#installation)
3. [Donwload Dependencies](#Download-Dependencies)
4. [Error Handling](#Error-Handling)
   - [CMake-GUI “NOT FOUND” Error](#cmake-gui-not-found-error)
   - [Model Error](#model-error)
   - [DLL Error](#dll-error)
6. [License](#license)

## Results
2D Pose Estimation Test (Body, Hand, Face)
<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/jm_golf_011.gif" width="400" height="300" hspace="0"/>
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/dance_001.gif" width="400" height="300" hspace="25"/> <br>
  <sup>Golf Pose Estimation(Body) single subject & Dance Pose Estimation(Body) multiple subject simultaneously</sup>
</p>

<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/theater.gif" width="400" height="300" />
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/sign_lang_001.gif" width="400" height="300" hspace="25" /> <br>
  <sup>Pose Estimation(Face) & Pose Estimation(Hand&Face)</sup> 
</p>

## JSON
### Write JSON File and Analyze <br>
This section focuses on how to work with JSON files generated by OpenPose, including writing, organizing, and analyzing the data for downstream applications.

**JSON Files Overview**
- OpenPose outputs JSON files containing pose estimation data for each frame of the input video or image sequence.
- These JSON files provide:
  - Keypoints: 2D (x, y) coordinates for body parts.
  - Confidence Scores: Certainty of detection for each keypoint.

### Pose Keypoints (BODY_25 Model)

| Keypoint Number | Body Part        | Keypoint Number | Body Part        |
|-----------------|------------------|-----------------|------------------|
| 1               | Nose             | 14              | Left Knee        |
| 2               | Neck             | 15              | Left Ankle       |
| 3               | Right Shoulder   | 16              | Right Eye        |
| 4               | Right Elbow      | 17              | Left Eye         |
| 5               | Right Wrist      | 18              | Right Ear        |
| 6               | Left Shoulder    | 19              | Left Ear         |
| 7               | Left Elbow       | 20              | Left Big Toe     |
| 8               | Left Wrist       | 21              | Left Small Toe   |
| 9               | Mid-Hip          | 22              | Left Heel        |
| 10              | Right Hip        | 23              | Right Big Toe    |
| 11              | Right Knee       | 24              | Right Small Toe  |
| 12              | Right Ankle      | 25              | Right Heel       |
| 13              | Left Hip         |                 |                  |


### Sample OpenPose JSON Output

```plaintext
OpenPose JSON Version: 1.3
Number of people detected: 1

Person 1:
  Pose Keypoints 2D (x, y, confidence):
    - Keypoint 1: (x=597.415, y=1147.46, confidence=0.87474)
    - Keypoint 2: (x=513.611, y=1152.96, confidence=0.865808)
    - Keypoint 3: (x=524.199, y=1184.22, confidence=0.907281)
    - Keypoint 4: (x=524.315, y=1278.61, confidence=0.908036)
    - Keypoint 5: (x=534.692, y=1362.15, confidence=0.937148)
    - Keypoint 6: (x=487.542, y=1142.45, confidence=0.835867)
    - Keypoint 7: (x=466.625, y=1231.23, confidence=0.0860125)
    - Keypoint 8: (x=482.332, y=1289.08, confidence=0.101454)
    - Keypoint 9: (x=409.065, y=1304.65, confidence=0.821696)
    - Keypoint 10: (x=430.094, y=1315.05, confidence=0.891222)
    - Keypoint 11: (x=471.728, y=1451.54, confidence=0.873621)
    - Keypoint 12: (x=435.163, y=1613.83, confidence=0.947365)
    - Keypoint 13: (x=398.449, y=1283.92, confidence=0.824988)
    - Keypoint 14: (x=471.955, y=1440.73, confidence=0.852741)
    - Keypoint 15: (x=445.899, y=1572, confidence=0.817724)
    - Keypoint 16: (x=587.182, y=1126.66, confidence=0.817243)
    - Keypoint 17: (x=0, y=0, confidence=0)
    - Keypoint 18: (x=560.782, y=1111.08, confidence=0.962837)
    - Keypoint 19: (x=0, y=0, confidence=0)
    - Keypoint 20: (x=513.738, y=1592.71, confidence=0.740854)
    - Keypoint 21: (x=492.891, y=1577.01, confidence=0.685205)
    - Keypoint 22: (x=440.472, y=1587.67, confidence=0.408025)
    - Keypoint 23: (x=492.948, y=1629.44, confidence=0.733568)
    - Keypoint 24: (x=482.449, y=1645.09, confidence=0.774996)
    - Keypoint 25: (x=419.486, y=1634.69, confidence=0.848233)
```

### Movement Analysis (e.g. Right Wrist)
<img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/results/jm_golf_004/05_right_wrist/plot_movement_analysis_right_wrist.png" />


## Installation
1. Download OpenPose from [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) in to working directory.
2. Install Required Tools and Libraries
   - Download [CMake-GUI](https://cmake.org/download/)
   - Download [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) and [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)
   - Check CUDA/cuDNN compatibility
     - [CUDA Wikipedia Page](https://en.wikipedia.org/wiki/CUDA)
     - [NVIDIA CUDA GPUs Compatibility](https://developer.nvidia.com/cuda-gpus#compute)
3. Configure OpenPose with CMake
4. Build OpenPose
5. Verify/Test Installation

For detailed installation guide, refer to [Installation Guide](https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/0_installation.md)

## Download Dependencies
When you navigate to `..\openpose_initial\3rdparty\windows`, you will see several `.bat` files. These batch files are used to download and configure third-party dependencies required by OpenPose. However, running these `.bat` files directly in the `Command Prompt` might fail because some of the referenced websites are no longer accessible. 
<p align="center">
   <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/getCaffe3rdparty.bat_download_error.png /> <br>
   <sup>getCaffe3rdparty.bat failed due to no connection</sup>
</p>

Download dependencies manually:
- [3rdparty_v1_2021.zip](https://drive.google.com/file/d/1WvftDLLEwAxeO2A-n12g5IFtfLbMY9mG/edit)


## Download Models
The `getModels.bat` script in `D:\my_programming\openpose\models` may fail to download the required models due to connectivity issues or the server being unavailable. To resolve this, you need to download the [models](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit) manually.
<p align="center">
   <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/getModels.bat_download_error.png" /> <br>
   <sup>getModels.bat failed due to no connection</sup>
</p>

Download models manually:
- [Model.zip](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit)


## Error Handling
### CMake-GUI “NOT FOUND” Error
When configuring and generating in CMake-GUI, you might encounter **"NOT FOUND"** errors for dependencies such as `Boost`, `Caffe`, `GFlags`, or `GLog`. These errors occur because the required `.lib` files are missing or their paths are not set correctly.  
  
### Model Error
The `getModels.bat` script in `D:\my_programming\openpose\models` may fail to download the required models due to connectivity issues or the server being unavailable. To resolve this, you need to download the [models](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit) manually. <br>
When you manually download the `model.zip` file and extract it, follow these steps carefully to replace the `.caffemodel` files without affecting other essential files, unless necessary for specific purposes.  

For detailed installation guide, refer to [Error Handling Guide](https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/0_error_handling.md)

### DLL Error


## Repository Contents
- `openpose_quick_commands.txt`: Quick commands for running OpenPose.


## Runtime Analysis


## License
This repository uses CMU OpenPose under the [OpenPose License](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE).

**Note**: OpenPose is licensed for academic or non-profit organization non-commercial research use only. Redistribution of OpenPose code or binaries is not permitted.
