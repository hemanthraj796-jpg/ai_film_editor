from moviepy import VideoFileClip, concatenate_videoclips
import os

def assemble_movie(video_folder, output_folder):
    # This list follows the logic of your script beats
    sequence = ["shot1.mp4", "shot2.mp4", "shot3.mp4", "shot4.mp4"]
    clips = []

    print("--- AI Video Assembly Started ---")

    for filename in sequence:
        file_path = os.path.join(video_folder, filename)
        
        if os.path.exists(file_path):
            print(f"Adding {filename} to the timeline...")
            # Load the clip
            clip = VideoFileClip(file_path)
            
            # If the clip is too long, we'll take just the first 5 seconds 
            # to make the edit feel "snappy"
            short_clip = clip.subclip(0, min(5, clip.duration))
            clips.append(short_clip)
        else:
            print(f"❌ Could not find {filename}")

    if clips:
        print("Stitching clips together...")
        # 'method=compose' ensures clips of different sizes fit together
        final_video = concatenate_videoclips(clips, method="compose")
        
        # Save the result
        output_path = os.path.join(output_folder, "final_rough_cut.mp4")
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"✅ Success! Your movie is ready at: {output_path}")
    else:
        print("No clips were found to stitch.")

# Define your paths
raw_video_dir = "../data/raw_video"
output_dir = "../output"

# Create output folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

assemble_movie(raw_video_dir, output_dir)