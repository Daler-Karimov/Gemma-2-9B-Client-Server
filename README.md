# Gemma-2-9B-Client-Server
On this repository you can download a client-server application to use Google's LLM model called Gemma 2. 

# Installation Instructions

1. **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Download and Install CUDA Toolkit:**
    - Download and install the CUDA Toolkit from the [NVIDIA website](https://developer.nvidia.com/cuda-downloads).
    - Ensure that the Windows environment variables are set up automatically. If not, manually add the path to the CUDA Toolkit to the PATH variable.

3. **Install Torch:**
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cuXXX
    ```
    Replace `XXX` with your CUDA version. You can find your CUDA version by running the command: `nvcc -V` or `nvidia-smi`.

4. **Get Hugging Face Token:**
    - Obtain a token on Hugging Face with "Write" permission.
    - Specify the token in the `app.py` code on line 17.

5. **Run the Application:**
    - Run `Run.bat`. This will automatically download all model files.
    - After the installation is complete, the model will run on: [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### Additional Information

- For more information about Hugging Face and obtaining tokens, visit the [Hugging Face website](https://huggingface.co/).
- Make sure to have the necessary permissions and system requirements to install and run the application.
- For troubleshooting or further assistance, please refer to the documentation or contact the developer.