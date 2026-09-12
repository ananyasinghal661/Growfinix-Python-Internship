import os
import asyncio
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import AsyncInferenceClient

# Load the secret token from .env
load_dotenv(Path(__file__).resolve().parent / ".env")

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

# Folder locations
BASE_DIR = Path(__file__).resolve().parent
PROMPTS_FILE = BASE_DIR / "prompts.txt"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# Hugging Face image generation client
client = AsyncInferenceClient(token=HF_TOKEN)


async def generate_image(prompt, image_number):
    print(f"Generating image {image_number}...")

    image = await client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    output_file = OUTPUT_DIR / f"image_{image_number}.png"
    image.save(output_file)

    print(f"Saved: {output_file}")


async def main():
    # Read prompts from prompts.txt
    prompts = PROMPTS_FILE.read_text(encoding="utf-8").splitlines()

    # Remove empty lines
    prompts = [prompt.strip() for prompt in prompts if prompt.strip()]

    # Generate images asynchronously
    tasks = [
        generate_image(prompt, number)
        for number, prompt in enumerate(prompts, start=1)
    ]

    await asyncio.gather(*tasks)

    print("All images generated successfully!")


if __name__ == "__main__":
    asyncio.run(main())