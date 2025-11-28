PRESETS = {
    "SD–512px": 512,
    "HD–1280px": 1280,
    "FullHD–1920px": 1920,
    "2K–2048px": 2048,
    "QHD–2560px": 2560,
    "4K–3840px": 3840,
    "8K–7680px": 7680,
}

ASPECT_RATIOS = {
    # Square
    "1:1-AlbumArt": (1, 1),

    # Portrait Formats
    "4:5-InstagramPortrait": (4, 5),
    "2:3-ClassicPortrait": (2, 3),
    "3:4-EditorialPortrait": (3, 4),

    # Vertical Video
    "9:16-TikTokReel": (9, 16),

    # Landscape / Video
    "4:3-ClassicVideo": (4, 3),
    "16:9-Widescreen": (16, 9),

    # Cinematic Aspect
    "21:9-CinemaScope": (21, 9),

    # Ultra Wide
    "32:9-UltraWideBanner": (32, 9),
}

def snap64(x):
    """Snap to nearest multiple of 64 — Latent-safe resolution"""
    return max(64, int(round(x / 64.0)) * 64)
