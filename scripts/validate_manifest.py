#!/usr/bin/env python3
"""Validate the custom song manifest and ensure the files exist."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SONGS_DIR = ROOT / "songs"
MANIFEST_PATH = SONGS_DIR / "manifest.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not MANIFEST_PATH.exists():
        fail(f"Missing manifest: {MANIFEST_PATH}")

    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in manifest: {exc}")

    songs = manifest.get("songs")
    if not isinstance(songs, list):
        fail("Manifest must contain a 'songs' list.")

    if not songs:
        fail("Manifest contains no songs.")

    for index, song in enumerate(songs):
        if not isinstance(song, dict):
            fail(f"Song entry #{index} is not an object.")

        required = ["id", "title", "artist", "filename"]
        missing = [field for field in required if not song.get(field)]
        if missing:
            fail(f"Song entry #{index} is missing required fields: {', '.join(missing)}")

        filename = song["filename"]
        file_path = SONGS_DIR / filename
        if not file_path.exists():
            fail(f"Song file missing for '{song['id']}': {file_path.name}")

    print(f"Validated {len(songs)} song entries in {MANIFEST_PATH.name}.")


if __name__ == "__main__":
    main()
