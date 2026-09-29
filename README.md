# GH3-Custom-Songs

A lightweight repository for organizing and previewing custom song assets.

## Project structure

- `songs/` — audio files and metadata for the custom library
- `scripts/validate_manifest.py` — verifies the song manifest and file availability

## Included sample

- `songs/Backhouse Mike - Just Fine.mp3`

## Usage

1. Add new tracks to `songs/`.
2. Update `songs/manifest.json` with the song metadata.
3. Run the validation script:

```bash
python scripts/validate_manifest.py
```

This keeps the library easy to extend without introducing a heavy framework or build step.
