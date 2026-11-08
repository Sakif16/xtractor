import os
import sys
import cv2


def extract_frames(video_path, output_dir=None):
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video not found: {video_path}")

    if output_dir is None:
        name = os.path.splitext(os.path.basename(video_path))[0]
        output_dir = os.path.join("frames", name)

    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError("Could not open video file.")

    count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(output_dir, f"frame_{count:06d}.jpg"), frame)
        count += 1

    cap.release()
    print(f"Done. Extracted {count} frames to '{output_dir}/'")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_frames.py videos/clip.mp4 [output_dir]")
        sys.exit(1)

    video = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    extract_frames(video, out)