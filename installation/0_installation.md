## Installation
1. Download OpenPose Repository from [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
   1. Navigate to your working directory
   2. Choose one of the following methods to download OpenPose:
      - Option 1: git clone the rpeository
        ```
        git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
        ```
      - Option 2: Click **Download ZIP** and unzip `openpose-master.zip` in your working directory
       
2. Install Required Tools and Libraries
   1. Visit [CMake-GUI](https://cmake.org/download/) and download the appropriate version for your operating system.
   2. Download [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) and [cuDNN](https://developer.nvidia.com/rdp/cudnn-archive)
      - Check compatibility
        - [CUDA Wikipedia Page](https://en.wikipedia.org/wiki/CUDA)
        - [NVIDIA CUDA GPUs Compatibility](https://developer.nvidia.com/cuda-gpus#compute)

3. Configure OpenPose with CMake
   1. Create "build" folder
      - Navigate to the `openpose` directory
      - Create a folder named `build` inside the `openpose` folder
   2. Open CMake-GUI
      - Launch the CMake GUI application
      - Set the followings:
        - **Where is the source code:** Browse to the root `openpose` folder
        - **Where to build the binaries:** Browse to the newly created `build` folder
   3. Configure the Project
      - Click **Configure** and select your preferred compiler (e.g. Visual Studio 16 2019)
   4. Generate Build Files
      - After configuration is complete, click **Generate** to create the build files
   <src img="https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/png/cmake_gui.png" width=70% height=70% />
