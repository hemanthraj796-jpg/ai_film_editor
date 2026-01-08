import os
import cv2
from moviepy import VideoFileClip, concatenate_videoclips

def get_motion_score(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame1 = cap.read()
    if not ret: return 0
    prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    total_motion = 0
    frame_count = 0
    while True:
        ret, frame2 = cap.read()
        if not ret: break
        next_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(prev_gray, next_gray)
        total_motion += diff.mean()
        prev_gray = next_gray
        frame_count += 1
    cap.release()
    return total_motion / frame_count if frame_count > 0 else 0

def smart_edit():
    # --- BULLETPROOF PATH LOGIC ---
    # This finds the 'AI_FILM_EDITOR' folder automatically
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    base_dir = os.path.dirname(script_dir)
    video_dir = os.path.join(base_dir, "data", "raw_video")
    output_dir = os.path.join(base_dir, "output")
    
    # Ensure output exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    shots = ["shot1.mp4", "shot2.mp4", "shot3.mp4", "shot4.mp4"]
    final_clips = []

    print(f"--- AI Analyzing Motion & Rendering ---")
    print(f"Looking in: {video_dir}")

    for shot in shots:
        path = os.path.join(video_dir, shot)
        if not os.path.exists(path):
            print(f"❌ Skipping {shot}: Not found at {path}")
            continue

        motion = get_motion_score(path)
        print(f"✅ Found {shot}: Motion Score = {motion:.2f}")

        clip = VideoFileClip(path)
        
        # Decision Logic
        if motion > 10: 
            print(f"   -> High Motion. Cutting {shot} to 2s.")
            processed_clip = clip.subclipped(0, min(2, clip.duration))
        elif "shot4" in shot:
            print(f"   -> Glow Effect. Keeping full duration.")
            processed_clip = clip.subclipped(0, clip.duration)
        else:
            print(f"   -> Normal Shot. Cutting to 4s.")
            processed_clip = clip.subclipped(0, min(4, clip.duration))

        final_clips.append(processed_clip)

    if final_clips:
        print("\nStitching final video...")
        final_video = concatenate_videoclips(final_clips, method="compose")
        final_video.write_videofile(os.path.join(output_dir, "ai_final_cut.mp4"), codec="libx264")
        print("\n🎉 SUCCESS! Your edit is in the /output folder.")
    else:
        print("❌ Error: Still no clips were found. Check filenames!")

if __name__ == "__main__":
    smart_edit()