# Real-Time Sign Language to Speech App

A simple browser-based app that captures your webcam, streams frames to the Hugging Face Space [`Remostartdev/realtime_signlanguage`](https://huggingface.co/spaces/Remostartdev/realtime_signlanguage), and speaks the recognized sign language text using the browser's built-in Speech Synthesis API.

## Features
- Real-time webcam streaming to the model
- Live text display of recognized segments
- Automatic text-to-speech (toggleable)
- Lightweight single-file HTML app
- Works on desktop and mobile browsers (HTTPS required for camera)

## How it works
1. Browser accesses the camera via `getUserMedia`.
2. Frames are captured at ~8 FPS, resized, JPEG-encoded, and sent as binary WebSocket messages.
3. The HF Space model processes the stream and returns JSON segments containing the translated text.
4. The app displays the text and speaks each new segment using `speechSynthesis`.

**WebSocket endpoint**: `wss://remostartdev-realtime-signlanguage.hf.space/ws`

## Deploy to Render (Static Site)

### Option 1: From this folder (recommended)

1. Push this folder to a GitHub repository (or create a new one).
2. Go to [Render Dashboard](https://dashboard.render.com/).
3. Click **New +** → **Static Site**.
4. Connect your GitHub repo.
5. Settings:
   - **Name**: `signlang-speech` (or anything you like)
   - **Branch**: `main`
   - **Root Directory**: leave blank (or set if the files are in a subfolder)
   - **Build Command**: leave blank
   - **Publish Directory**: `.` (or the folder containing `index.html`)
6. Click **Create Static Site**.
7. Once deployed, open the Render URL. Allow camera access when prompted.

### Option 2: Manual upload
You can also host the `index.html` file on any static host (Netlify, Vercel, GitHub Pages, etc.).

## Local testing
Simply open `index.html` in a modern browser.  
**Note**: Camera access requires HTTPS or `localhost`. For pure local file testing you may need a simple server:

```bash
# Python
python -m http.server 8000

# or Node
npx serve .
```

Then visit `http://localhost:8000`.

## Customization
Edit the constants at the top of the `<script>` in `index.html`:
- `TARGET_FPS` — frame rate sent to the model (try 5–12)
- `JPEG_QUALITY` — compression (0.5–0.8)
- `FRAME_WIDTH` / `FRAME_HEIGHT` — resolution of sent frames

## Requirements
- Modern browser with WebSocket + MediaDevices support (Chrome, Edge, Firefox, Safari)
- Camera permission
- The Hugging Face Space must be running (it is free and usually stays warm)

## Privacy
Video frames are sent only to the public Hugging Face Space. No data is stored by this app. Speech synthesis happens entirely in the browser.
