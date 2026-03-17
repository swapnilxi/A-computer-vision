import asyncio
import websockets
import cv2
import mediapipe as mp
import json
import http.server
import socketserver
import threading
import os

# --- CONFIGURATION ---
HTML_FILE = "RainDeerGame-fast.html"  # Make sure this matches your filename exactly
HTTP_PORT = 8000
WS_PORT = 8765

# --- MEDIA PIPE SETUP ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# --- WEBSOCKET SERVER (HAND TRACKING) ---
async def send_hand_data(websocket):
    print("🎮 Game Connected to Tracker!")
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            success, image = cap.read()
            if not success: continue

            # Flip and convert
            image = cv2.flip(image, 1)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            results = hands.process(image_rgb)
            data = {"found": False}

            if results.multi_hand_landmarks:
                lm = results.multi_hand_landmarks[0]
                index_tip = lm.landmark[8]
                thumb_tip = lm.landmark[4]
                
                # Pythagorean distance for pinch
                pinch_dist = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5
                
                data = {
                    "found": True,
                    "x": index_tip.x,
                    "y": index_tip.y,
                    "pinch_dist": pinch_dist
                }

            await websocket.send(json.dumps(data))
            await asyncio.sleep(0.01) # 100 FPS cap (approx)

    except websockets.exceptions.ConnectionClosed:
        print("❌ Game Disconnected")
    finally:
        cap.release()

# --- HTTP SERVER (HOSTS THE GAME FILE) ---
def run_http_server():
    # This prevents the "Address already in use" error if you restart quickly
    socketserver.TCPServer.allow_reuse_address = True
    
    # Simple handler to serve files in the current folder
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", HTTP_PORT), Handler) as httpd:
        print(f"\n✅ SERVER STARTED!")
        print(f"👉 PLAY HERE: http://localhost:{HTTP_PORT}/{HTML_FILE}")
        print(f"   (Hand Tracker running on port {WS_PORT})\n")
        httpd.serve_forever()

async def main():
    # Start the WebSocket server
    async with websockets.serve(send_hand_data, "localhost", WS_PORT):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    # 1. Start HTTP Server in a separate thread (Background)
    threading.Thread(target=run_http_server, daemon=True).start()
    
    # 2. Start WebSocket Server in the main thread
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping server...")