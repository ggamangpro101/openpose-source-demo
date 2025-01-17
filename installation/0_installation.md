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
   - Create "build" folder in "openpose" folder
     <br>
     <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/installation/png/create_build_folder.png" width=70% height=70% />
