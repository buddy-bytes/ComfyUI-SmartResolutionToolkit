import torch
from .latent_utils import PRESETS, ASPECT_RATIOS, snap64

class SmartLatentGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution_preset": (list(PRESETS.keys()), {"default": "FullHD_1920x1080"}),
                "aspect_ratio": (list(ASPECT_RATIOS.keys()), {"default": "16:9_Widescreen"}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 16}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("LATENT",)
    FUNCTION = "generate"
    CATEGORY = "latent/generator"

    def generate(self, resolution_preset, aspect_ratio, batch_size):
        long_side = PRESETS[resolution_preset]
        ar_w, ar_h = ASPECT_RATIOS[aspect_ratio]

        scale = long_side / float(max(ar_w, ar_h))
        width = snap64(ar_w * scale)
        height = snap64(ar_h * scale)

        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples": latent},)
