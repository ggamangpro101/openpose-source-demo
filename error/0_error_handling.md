# Error Handling Guide
**Contents:**
- [CMake-GUI “NOT FOUND” Error](#cmake-gui-not-found-error)
- [Model Error](#model-error)
- [DLL Error](#dll-error)

## CMake-GUI “NOT FOUND” Error
When configuring and generating in CMake-GUI, you might encounter **"NOT FOUND"** errors for dependencies such as `Boost`, `Caffe`, `GFlags`, `GLog` or `OpenCV`. These errors occur because the required `.lib` files are missing or their paths are not set correctly.  

When you navigate to `..\openpose\3rdparty\windows`, opening any `.zip` file or running a `.bat` file may result in an empty file or a failure to download the required dependencies due to connectivity issues or an unavailable server. To resolve this, you need to download the [dependencies](https://drive.google.com/file/d/1WvftDLLEwAxeO2A-n12g5IFtfLbMY9mG/edit) manually and extract them into the `..\openpose\3rdparty\windows` directory. After extraction, you should see a `3rdParty` directory. Navigate to `../3rdParty/windows` and you should see:
<p align="center">
  <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/extrated_3rdParty.png width=70% height=70% />
  <sup>Extracted files from 3rdparty.zip </sup>
</p>

Copy the necessary `.zip` files into `..\openpose\3rdparty\windows`. To address errors such as `boost`, `caffe`, `gflags`, `glog`, or `opencv` NOTFOUND, specifically copy `caffe_16_2020_11_14.zip`, `caffe3rdpart_16_2020_11_14.zip` and `opencv_450_v15_2020_11_18.zip` into the `..\openpose\3rdparty\windows` directory and extract them.

After extraction, set the appropriate paths to these dependencies in your environment variables or build configuration to ensure they are correctly linked during the OpenPose build process.

  - **BOOST NOT FOUND :**
    <p align="center">   
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/BOOST_NOTFOUND.png width=90% height=90% />
    </p>
     
     - BOOST_FILESYSTEM_LIB_DEBUG :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_filesystem-vc142-mt-gd-x64-1_74.lib`

     - BOOST_FILESYSTEM_LIB_RELEASE :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_filesystem-vc142-mt-x64-1_74.lib`

     - BOOST_SYSTEM_LIB_DEBUG :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_system-vc142-mt-gd-x64-1_74.lib`

     - BOOST_SYSTEM_LIB_RELEASE :  
     `../openpose/3rdparty/windows/caffe3rdparty/lib/boost_system-vc142-mt-x64-1_74.lib`

  - **Caffe NOT FOUND :**  
    <p align="center">
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/Caffe_NOTFOUND.png width=90% height=90%/>
    </p>
    
      - Caffe_LIB_DEBUG :
      `../openpose/3rdparty/windows/caffe/lib/caffe-d.lib`

      - Caffe_LIB_RELEASE :
      `../openpose/3rdparty/windows/caffe/lib/caffe.lib`

      - Caffe_Proto_LIB_DEBUG :
      `../openpose/3rdparty/windows/caffe/lib/caffeproto-d.lib`

      - Caffe_Proto_LIB_RELEASE : 
      `../openpose/3rdparty/windows/caffe/lib/caffeproto.lib`

  - **GFLAGS NOT FOUND :**  
    <p align="center">
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/GFLAGS_NOTFOUND.png width="90%" height="90%"/>
    </p>
    
      - GFLAGS_LIBRARY_DEBUG :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/gflagsd.lib`

      - GFLAGS_LIBRARY_RELEASE :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/gflags.lib `

  - **GLOG NOT FOUND :**  
    <p align="center">
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/GLOG_NOTFOUND.png width=90% height=90%/>
    </p>
    
      - GLOG_LIBRARY_DEBUG :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/glogd.lib`

      - GLOG_LIBRARY_RELEASE :
      `../openpose/3rdparty/windows/caffe3rdparty/lib/glog.lib`

  - **OpenCV NOT FOUND :**
    <p align="center">
    <img src=https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/OpenCV_NOTFOUND.png width=90% height=90% />
    </p>

After setting all the required paths, reconfigure and generate the build. You should see the messages **'Configuring done'** and **'Generating done'** successfully.
<p align="center">
   <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/CMake_complete.png" /> <br>
   <sup>Cmake-GUI complete</sup>
</p>


## Model Error
The `getModels.bat` script in `D:\my_programming\openpose\models` may fail to download the required models due to connectivity issues or the server being unavailable. To resolve this, you need to download the [models](https://drive.google.com/file/d/1QCSxJZpnWvM00hx49CJ2zky7PWGzpcEh/edit) manually.
<p align="center">
   <img src="https://github.com/ggamangpro101/openpose-source-demo/blob/master/error/png/getModels.bat_download_error.png" /> <br>
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

## DLL Error
