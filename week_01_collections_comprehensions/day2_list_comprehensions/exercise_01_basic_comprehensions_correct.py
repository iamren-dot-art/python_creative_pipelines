# Frame range for a 2-sec animation at 24fps
frames = list(range(0, 48))


# 1. Create a list of frame times in seconds (frame / 24)
#    e.g., frame 0 = 0.0s, frame 24 = 1.0s
duration = [round(f / 24, 3) for f in frames]
print("--- Frames in seconds (24fps) ---")
for frame, time in zip(frames, duration):
    print(f"frame {frame} = {time}s")


# 2. Create a list of only even-numbered frames
even_frames = [f for f in frames if f % 2 == 0]
print("\n--- Even numbered frames only ---")
print(even_frames, sep="\n")


# 3. Create a list of frame labels: ["f00", "f01", "f02", ... "f47"]
#    Hint: f-strings work inside comprehensions. Look up f-string zero-padding
#    if you haven't used it before (:02d)
frame_labels = [f"f{f:02}" for f in frames]
print("\n--- Frame labels ---")
print(frame_labels)
