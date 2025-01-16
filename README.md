# OpenPose from Source Demo
This repository demonstrates my personal project where I compiled and ran [CMU OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) from source to process custom video and image inputs for non-commercial research purposes. Through this project, I explored OpenPose's capabilities, including 2D pose estimation for body, hand, and face keypoints, while integrating various input types like webcam, videos and images. The repository also highlights key learnings, troubleshooting steps, and efficient usage of OpenPose for multi-person detection scenarios. This serves as a comprehensive guide for anyone looking to set up and utilize OpenPose from source for their own research or academic projects.

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
   - [CMake-GUI “NOT FOUND” Error](#cmake-gui-not-found-error)
   - [Model Error](#model-error)
6. [License](#license)

## Results
2D Pose Estimation Test (Body, Hand, Face)
<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/jm_golf_011.gif" width="300" height="200" hspace="0"/>
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/dance_001.gif" width="300" height="200" hspace="50"/> <br>
  <sup>Golf Pose Estimation(Body) single subject & Dance Pose Estimation(Body) multiple subject simultaneously</sup>
</p>

<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/theater.gif" width="300" height="200" />
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/sign_lang_001.gif" width="300" height="200" hspace="50" /> <br>
  <sup>Pose Estimation(Face) & Pose Estimation(Hand&Face)</sup> 
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
     <br>
     <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/create_build_folder_zoom.png" width=70% height=70% />


## Download Dependencies
When you navigate to `..\openpose_initial\3rdparty\windows`, you will see several `.bat` files. These batch files are used to download and configure third-party dependencies required by OpenPose. However, running these `.bat` files directly in the `Command Prompt` might fail because some of the referenced websites are no longer accessible. 
<p align="center">
   <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/GetCaffe3rdparty.bat_download_error.png /> <br>
   <sup>getCaffe3rdparty.bat failed due to no connection</sup>
</p>

Download dependencies manually:
- [3rdparty_v1_2021.zip](https://drive.google.com/file/d/1WvftDLLEwAxeO2A-n12g5IFtfLbMY9mG/edit)


## Download Models
The `getModels.bat` script in `D:\my_programming\openpose\models` may fail to download the required models due to connectivity issues or the server being unavailable. To resolve this, you need to download the [models](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit) manually.
<p align="center">
   <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/getModels.bat_download_error.png" /> <br>
   <sup>getModels.bat failed due to no connection</sup>
</p>

Download models manually:
- [Model.zip](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit)


## Error Handling
### CMake-GUI “NOT FOUND” Error
When configuring and generating in CMake-GUI, you might encounter **"NOT FOUND"** errors for dependencies such as `Boost`, `Caffe`, `GFlags`, or `GLog`. These errors occur because the required `.lib` files are missing or their paths are not set correctly.  
  
### Model Error
The `getModels.bat` script in `D:\my_programming\openpose\models` may fail to download the required models due to connectivity issues or the server being unavailable. To resolve this, you need to download the [models](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit) manually.
<p align="center">
   <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/getModels.bat_download_error.png" /> <br>
   <sup>getModels.bat failed due to no connection</sup>
</p>

When you manually download the `model.zip` file and extract it, follow these steps carefully to replace the `.caffemodel` files without affecting other essential files, unless necessary for specific purposes.  

**1. Unzip the Downloaded Model File**
   - Extract the model.zip file into a temporary folder.
   - Inside the extracted folder, locate the .caffemodel files for the respective models:
      - Face Model: `pose_iter_116000.caffemodel`
      - Hand Model: `pose_iter_102000.caffemodel`
      - Body Models (e.g., BODY_25): `pose_iter_584000.caffemodel`

**2. Replace the Existing `.caffemodel`**
   - Navigate to the original model folder: `..\openpose\models`.
   - Replace only the `.caffemodel` files under the respective directories.

**3. Verify Supporting Files Are Untouched**
   - For `Face Models`: Ensure `.xml` and `.prototxt` files are present and untouched in: `..\openpose\models\face`
   - For `Hand Models`: Ensure `.prototxt` files remain untouched in: `..\openpose\models\hand`
   - For `Pose Models`: Under `body_25`, ensure `.prototxt` files remain untouched in: `..\openpose\models\pose\body_25`

**4. Avoid Confusion with New Files**
   - Do not copy extra files from the extracted `model.zip` that do not belong to the corresponding directories.
   - Double-check that only the `.caffemodel` files are replaced.  

**5. Test the Setup**
   - After replacing the `.caffemodel` files, run OpenPose to confirm the models load correctly and there are no missing file errors.

## Repository Contents
- `openpose_quick_commands.txt`: Quick commands for running OpenPose.


## Runtime Analysis


## License
This repository uses CMU OpenPose under the [OpenPose License](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE).

**Note**: OpenPose is licensed for academic or non-profit organization non-commercial research use only. Redistribution of OpenPose code or binaries is not permitted.
