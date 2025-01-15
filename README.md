# OpenPose from Source Demo

This repository demonstrates how I used [CMU OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) to process my own video and image inputs for non-commercial research purposes.

## Environment 
- Operating system: Windows 10 
- GPU: NVIDIA GeForce RTX 4070
- Visual Studio 2019 Community
- CUDA: 12.0 
- cuDNN: cudnn-12.0-windows-x86_64-v8.8.0.121 

## Contents

1. [Results](#results)
2. [Installation](#installation)
3. [Donwload Dependencies](#Download-Dependencies)
4. [Error Handling](#Error-Handling)
5. [License](#license)

## Results
2D Pose Estimation Test (Body, Hand, Face)
<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/jm_golf_11.gif" width="300" height="200" />
  <img src="https://github.com/ggamangpro101/openpose-demo/blob/main/gif/hand_005.gif" width="300" height="200" />
</p>
<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-demo/blob/main/gif/movie_theater_face.gif" width="300" height="200" />
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/hand_005.gif" width="300" height="200" />
</p>

## Installation
1. Download OpenPose from [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) in to working directory.
2. Download [CMake-GUI](https://cmake.org/download/)
3. Download [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) and [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)
   - Check compatibility
     https://en.wikipedia.org/wiki/CUDA
     https://developer.nvidia.com/cuda-gpus#compute
4. Open CMake-GUI
   - Create "build" folder in "openpose" folder
   - 


## Download Dependencies
When you navigate to ..\openpose_initial\3rdparty\windows, you will see several .bat files. These batch files are used to download and configure third-party dependencies required by OpenPose. However, running these .bat files directly in the Command Prompt might fail because some of the referenced websites are no longer accessible.
<p>
![GetCaffe3rdparty bat_download_error](https://github.com/user-attachments/assets/a4c7c1f8-9c2c-4b14-aec7-a7fdf5fd98b7)
</p>

Instead, download dependencies manually:
- [Model.zip](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit)
- [3rdparty_v1_2021.zip](https://drive.google.com/file/d/1WvftDLLEwAxeO2A-n12g5IFtfLbMY9mG/edit)

## Error Handling
- CMake-GUI “NOT FOUND” Error
  
  - BOOST NOT FOUND:
  ![image](https://github.com/user-attachments/assets/3f2613a1-acd0-424a-a60a-aa10fd8b322c)
    - BOOST_FILESYSTEM_LIB_DEBUG -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/boost_filesystem-vc142-mt-gd-x64-1_74.lib
    - BOOST_FILESYSTEM_LIB_RELEASE --> 
    ../openpose/3rdparty/windows/caffe3rdparty/lib/boost_filesystem-vc142-mt-x64-1_74.lib
    - BOOST_SYSTEM_LIB_DEBUG -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/boost_system-vc142-mt-gd-x64-1_74.lib
    - BOOST_SYSTEM_LIB_RELEASE -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/boost_system-vc142-mt-x64-1_74.lib

  - Caffe NOT FOUND:
  ![image](https://github.com/user-attachments/assets/5d8b5aa2-d750-4097-ad77-9644f8d758b5)
    - Caffe_LIB_DEBUG --> 
    ../openpose/3rdparty/windows/caffe/lib/caffe-d.lib
    - Caffe_LIB_RELEASE --> 
    ../openpose/3rdparty/windows/caffe/lib/caffe.lib
    - Caffe_Proto_LIB_DEBUG --> 
    ../openpose/3rdparty/windows/caffe/lib/caffeproto-d.lib
    - Caffe_Proto_LIB_RELEASE --> 
    ../openpose/3rdparty/windows/caffe/lib/caffeproto.lib

  - GFLAGS NOT FOUND:
  ![image](https://github.com/user-attachments/assets/8f6edb5f-042b-4fc2-8501-60324b3ff88d)
    - GFLAGS_LIBRARY_DEBUG -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/gflagsd.lib
    - GFLAGS_LIBRARY_RELEASE -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/gflags.lib 

  - GLOG NOT FOUND:
  ![image](https://github.com/user-attachments/assets/e754bf28-962b-43a6-90e0-47ac4f3360dc)
    - GLOG_LIBRARY_DEBUG -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/glogd.lib
    - GLOG_LIBRARY_RELEASE -->
    ../openpose/3rdparty/windows/caffe3rdparty/lib/glog.lib

- Model Error

## Repository Contents
- `run_demo.sh`: Example script for running OpenPose.
- `jm_golf_#.mp4`: Input video for the demo.
- `output/`: Folder for processed files.


## Runtime Analysis


## License
This repository uses CMU OpenPose under the [OpenPose License](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE).

**Note**: OpenPose is licensed for academic or non-profit organization non-commercial research use only. Redistribution of OpenPose code or binaries is not permitted.
