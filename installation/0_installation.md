# Installation Guide for OpenPose
This guide provides detailed steps for installing OpenPose. Follow these instructions carefully to set up the environment.

## 1. Download OpenPose Repository from [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
**1. Navigate to your working directory** <br>

**2. Choose one of the following methods to download OpenPose:** <br>
  - Option 1: git clone the rpeository <br>
  ```
  git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
  ```
  - Option 2: Click **Download ZIP** and unzip `openpose-master.zip` in your working directory


## 2. Install Required Tools and Libraries
**1. Visit [CMake-GUI](https://cmake.org/download/) and download the appropriate version for your operating system.** <br>

**2. Download [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) and [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)** <br>
  - Check compatibility
    - [CUDA Wikipedia Page](https://en.wikipedia.org/wiki/CUDA)
    - [NVIDIA CUDA GPUs Compatibility](https://developer.nvidia.com/cuda-gpus#compute)


## 3. Configure OpenPose with CMake
**1. Create "build" folder** <br>
  - Navigate to the `openpose` directory <br>
  - Create a folder named `build` inside the `openpose` folder <br>

**2. Open CMake-GUI** <br>
  - Launch the CMake GUI application <br>
  - Set the followings: <br>
    - **Where is the source code:** Browse to the root `openpose` folder <br>
    - **Where to build the binaries:** Browse to the newly created `build` folder <br>

**3. Configure the Project** <br>
  - Click **Configure** and select your preferred compiler (e.g. Visual Studio 16 2019, x64) <br>
  
    <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/png/cmake_gui.png" width=75% height=75% /> <br>


**4. Error during configuration**
  - If you encounter any issues, refer to the [Error Handling Guide](../error/0_error_handling.md). Otherwise, proceed to the next step.

    - NOTFOUND error
  
    <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/png/cmake_generate_error.png" width=75% height=75% />

**5. Generate Build Files**
  - After configuration is complete, click **Generate** to create the build files


## 4. Build OpenPose
**1. Open the Build System** <br>

  For Windows:  
   - Open the `openpose.sln` file in `../openpose/build` with Visual Studio

**2. Compile the Code**

  For Visual Studio:
   - Select **Release, x64** mode in the build configuration
   - click **Build > Build Solution (Ctrl+Shift+B)** <br>
   - If the build is **successful**, you will see a mesage similar to: <br>
   <p align="center">
   <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/png/build_success.png" />     
   </p>

## 5. Verify Installation
**Test OpenPose Examples**
  - Navigate to `..openpose\build\x64\Release`
  - Run one of the example scripts to test your installation. For example:
```
OpenPoseDemo.exe --model_folder "(my_directory)/openpose/models"
```
