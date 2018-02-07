## Upgrade cuda & tensorflow

### Step 1: Remove previous cuda completely
1. To uninstall the CUDA Toolkit, run the uninstallation script provided in the bin directory of the toolkit. By default, it is located in /usr/local/cuda-7.5/bin:   
**$ sudo /usr/local/cuda-7.5/bin/uninstall_cuda_7.5.pl**    
   
2. To uninstall the NVIDIA Driver, run nvidia-uninstall:   
**$ sudo /usr/bin/nvidia-uninstall**   
    
3. Remove all nvidia drivers completely   
**sudo apt-get autoremove --purge nvidia-***     


### Step 2: Install Cuda Toolkit

0. Description: Toolkit contains 
    1. NVIDIA Accelerated Graphics Driver
    2. OpenGL libraries
    3. CUDA 8.0 Toolkit

1. Hit **CTRL+ALT+F1** and login using your credentials.    
    
2. kill your current X server session by typing **sudo service lightdm stop** or **sudo lightdm stop**
    
3. Enter runlevel 3 by typing **sudo init 3** and install your .run file.     
Run `sudo sh cuda_8.0.44_linux.run`  

4. You might be required to reboot when the installation finishes.     
If not, run **sudo service lightdm start** or **sudo start lightdm** to start your X server again.    

### Step 3: Environment Setup
* export PATH=/usr/local/cuda/bin:$PATH    
* export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH    

### Step 4: Install CuDNN

1. download CuDNN from https://developer.nvidia.com/cudnn

2. Uncompress and copy the cuDNN files into the toolkit directory. Assuming the toolkit is
installed in /usr/local/cuda, run the following commands

    tar xvzf cudnn-8.0-linux-x64-v5.1-ga.tgz
    sudo cp cuda/include/cudnn.h /usr/local/cuda/include
    sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
    sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*




### Step 5: Upgrade tensorflow 
1. Ubuntu/Linux 64-bit, GPU enabled, Python 2.7    
 Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.    
*$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.0-cp27-none-linux_x86_64.whl*

2. *$ sudo pip install --upgrade $TF_BINARY_URL*
