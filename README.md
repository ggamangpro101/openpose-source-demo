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
   - [CMake-GUI “NOT FOUND” Error](#cmake-gui-not-found-error)
   - [Model Error](#model-error)
6. [License](#license)

## Results
2D Pose Estimation Test (Body, Hand, Face)
<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/jm_golf_011.gif" width="300" height="200" />   
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/dance_001.gif" width="300" height="200" />  
</p>

<p align="center">
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/theater.gif" width="300" height="200" />
  <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/gif/sign_lang_001.gif" width="300" height="200" />
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
<img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/GetCaffe3rdparty.bat_download_error.png />
</p>

Instead, download dependencies manually:
- [Model.zip](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit)
- [3rdparty_v1_2021.zip](https://drive.google.com/file/d/1WvftDLLEwAxeO2A-n12g5IFtfLbMY9mG/edit)

## Error Handling
### CMake-GUI “NOT FOUND” Error
When configuring and generating in CMake-GUI, you might encounter **"NOT FOUND"** errors for dependencies such as `Boost`, `Caffe`, `GFlags`, or `GLog`. These errors occur because the required `.lib` files are missing or their paths are not set correctly.  
  - **BOOST NOT FOUND :**   
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/BOOST_NOTFOUND.png width=90% height=90% />
     
     - BOOST_FILESYSTEM_LIB_DEBUG :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_filesystem-vc142-mt-gd-x64-1_74.lib`

     - BOOST_FILESYSTEM_LIB_RELEASE :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_filesystem-vc142-mt-x64-1_74.lib`

     - BOOST_SYSTEM_LIB_DEBUG :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_system-vc142-mt-gd-x64-1_74.lib`

     - BOOST_SYSTEM_LIB_RELEASE :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_system-vc142-mt-x64-1_74.lib`

  - **Caffe NOT FOUND :**  
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/Caffe_NOTFOUND.png width=90% height=90%/>
    
      - Caffe_LIB_DEBUG :
      `../openpose/3rdparty/windows/caffe/lib/caffe-d.lib`

      - Caffe_LIB_RELEASE :
      `../openpose/3rdparty/windows/caffe/lib/caffe.lib`

      - Caffe_Proto_LIB_DEBUG :
      `../openpose/3rdparty/windows/caffe/lib/caffeproto-d.lib`

      - Caffe_Proto_LIB_RELEASE : 
      `../openpose/3rdparty/windows/caffe/lib/caffeproto.lib`

  - **GFLAGS NOT FOUND :**  
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/GFLAGS_NOTFOUND.png width="90%" height="90%"/>
    
      - GFLAGS_LIBRARY_DEBUG :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/gflagsd.lib`

      - GFLAGS_LIBRARY_RELEASE :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/gflags.lib `

  - **GLOG NOT FOUND :**  
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/GLOG_NOTFOUND.png width=90% height=90%/>
    
      - GLOG_LIBRARY_DEBUG :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/glogd.lib`

      - GLOG_LIBRARY_RELEASE :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/glog.lib`

### Model Error
The `getModels.bat` script in `D:\my_programming\openpose\models` may fail to download the required models due to connectivity issues or the server being unavailable. To resolve this, you need to download the [models](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit) manually.
<p align="center">
<img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/getModels.bat_download_error.png" />
</p>

When you manually download the `model.zip` file and extract it, follow these steps carefully to replace the `.caffemodel` files without affecting other essential files.  

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
