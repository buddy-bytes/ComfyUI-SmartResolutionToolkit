from .latent_utils import PRESETS, ASPECT_RATIOS, snap64

class SmartResolutionPicker:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution_preset": (list(PRESETS.keys()), {"default": "FullHD_1920x1080"}),
                "aspect_ratio": (list(ASPECT_RATIOS.keys()), {"default": "16:9_Widescreen"}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate"
    CATEGORY = "utils/latent"

    def calculate(self, resolution_preset, aspect_ratio):
        long_side = PRESETS[resolution_preset]
        ar_w, ar_h = ASPECT_RATIOS[aspect_ratio]

        scale = long_side / float(max(ar_w, ar_h))
        width = snap64(ar_w * scale)
        height = snap64(ar_h * scale)
        
        return (width, height)
