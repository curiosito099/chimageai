from diffusers import StableDiffusionPipeline
import torch

# Cargar el modelo
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
prompt = ("Majestic neon cityscape at night, with towering holographic billboards, vibrant cyberpunk vibes, "
    "flying cars weaving between skyscrapers, a giant luminous moon overhead, cinematic lighting, 8k, highly detailed, "
          "trending on ArtStation."
)
negative_prompt = ("blurry, out of frame, poorly drawn details, watermark, text, low resolution, ugly")
image = pipe(prompt, num_inference_steps=50, guidance_scale=8.5, negative_prompt=negative_prompt).images[0]
image.save("TIKTOK_curiosito_city_cyber_.png") # Guardar la imagen
print("✅ Imagen generada y guardada como 'TIKTOK_curiosito_city_cyber_.png'")