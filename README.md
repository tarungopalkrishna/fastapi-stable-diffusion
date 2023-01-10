# FastAPI and Stable Diffusion

Returns the image for the prompt

Install packages with
```bash
    # Install huggingface packages
    pip install diffusers transformers accelerate scipy safetensors
    # Install fastAPI packages
    pip install fastapi
    pip install "uvicorn[standard]"
```

To run
```bash
    uvicorn main:app --reload
```