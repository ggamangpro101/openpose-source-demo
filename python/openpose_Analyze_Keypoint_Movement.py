import os
import json
import numpy as np
import matplotlib.pyplot as plt

# Directory containing JSON files
json_dir = r"D:\my_programming\openpose\output\output_json\jm_golf_004"

def load_keypoints(json_dir):
    keypoint_data = []

    for file in sorted(os.listdir(json_dir)):
        if file.endswith("_keypoints.json"):
            filepath = os.path.join(json_dir, file)
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                    if data["people"]:  # Ensure there are detected people
                        person = data["people"][0]  # Use the first detected person
                        keypoints = np.array(person["pose_keypoints_2d"]).reshape(-1, 3)  # Reshape to (num_keypoints, 3)
                        keypoint_data.append({
                            "frame": file,
                            "keypoints": keypoints
                        })
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON file: {file}")
    return keypoint_data

# Calculate movement between frames
def calculate_movement(keypoint_data):
    movements = []

    for i in range(1, len(keypoint_data)):
        prev_frame = keypoint_data[i - 1]["keypoints"]
        curr_frame = keypoint_data[i]["keypoints"]

        # Calculate differences in x and y for each keypoint
        dx = curr_frame[:, 0] - prev_frame[:, 0]
        dy = curr_frame[:, 1] - prev_frame[:, 1]
        movement = np.sqrt(dx**2 + dy**2)  # Euclidean distance

        movements.append({
            "frame": keypoint_data[i]["frame"],
            "movement": movement
        })

    return movements

# Plot movement for a specific keypoint
def plot_keypoint_movement(movements, keypoint_index, keypoint_name):
    movement_values = [m["movement"][keypoint_index] for m in movements]
    frame_numbers = range(len(movements))

    plt.figure(figsize=(10, 5))
    plt.plot(frame_numbers, movement_values, marker='o')
    plt.title(f"Movement Analysis for {keypoint_name}")
    plt.xlabel("Frame")
    plt.ylabel("Movement (Euclidean Distance)")
    plt.grid()
    plt.show()

# Main workflow
if __name__ == "__main__":
    # Step 1: Load keypoint data
    keypoint_data = load_keypoints(json_dir)
    print(f"Loaded {len(keypoint_data)} frames with keypoint data.")

    # Step 2: Calculate movement between frames
    movements = calculate_movement(keypoint_data)
    print(f"Calculated movements for {len(movements)} frames.")

    # Step 3: Convert NumPy arrays to lists
    for movement in movements:
        movement["movement"] = movement["movement"].tolist()  # Fix for JSON serialization

    # Step 4: Analyze movement for a specific keypoint
    '''
        | Keypoint Number | Body Part        | Keypoint Number | Body Part        |
        |-----------------|------------------|-----------------|------------------|
        | 1               | Nose             | 14              | Left Knee        |
        | 2               | Neck             | 15              | Left Ankle       |
        | 3               | Right Shoulder   | 16              | Right Eye        |
        | 4               | Right Elbow      | 17              | Left Eye         |
        | 5               | Right Wrist      | 18              | Right Ear        |
        | 6               | Left Shoulder    | 19              | Left Ear         |
        | 7               | Left Elbow       | 20              | Left Big Toe     |
        | 8               | Left Wrist       | 21              | Left Small Toe   |
        | 9               | Mid-Hip          | 22              | Left Heel        |
        | 10              | Right Hip        | 23              | Right Big Toe    |
        | 11              | Right Knee       | 24              | Right Small Toe  |
        | 12              | Right Ankle      | 25              | Right Heel       |
        | 13              | Left Hip         |                 |                  |
    '''
    keypoint_index = 5  # Example: 0 = Nose
    keypoint_name = "Right Wrist"
    plot_keypoint_movement(movements, keypoint_index, keypoint_name)

    # Optional: Save movement data to a JSON file
    output_file = os.path.join(json_dir, "movement_summary_right_elbow.json")
    with open(output_file, "w") as f:
        json.dump(movements, f, indent=4)
    print(f"Movement data saved to {output_file}")
