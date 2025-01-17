import json


def read_openpose_json(file_path):
    """
    Reads and parses an OpenPose JSON file.

    Args:
        file_path (str): Path to the OpenPose JSON file.

    Returns:
        dict: Parsed data from the JSON file.
    """
    try:
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Extract version and keypoints data
        version = data.get("version", "Unknown")
        people = data.get("people", [])

        print(f"OpenPose JSON Version: {version}")
        print(f"Number of people detected: {len(people)}")

        # Loop through each person detected
        for i, person in enumerate(people):
            print(f"\nPerson {i + 1}:")

            # Pose keypoints 2D
            pose_keypoints = person.get("pose_keypoints_2d", [])
            print(f"  Pose Keypoints 2D (x, y, confidence):")
            for j in range(0, len(pose_keypoints), 3):
                x, y, confidence = pose_keypoints[j:j + 3]
                print(f"    - Keypoint {j // 3 + 1}: (x={x}, y={y}, confidence={confidence})")

            # Face keypoints 2D
            face_keypoints = person.get("face_keypoints_2d", [])
            if face_keypoints:
                print(f"  Face Keypoints 2D: {face_keypoints}")

            # Hand keypoints 2D
            hand_left_keypoints = person.get("hand_left_keypoints_2d", [])
            hand_right_keypoints = person.get("hand_right_keypoints_2d", [])
            if hand_left_keypoints:
                print(f"  Left Hand Keypoints 2D: {hand_left_keypoints}")
            if hand_right_keypoints:
                print(f"  Right Hand Keypoints 2D: {hand_right_keypoints}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON file at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
file_path = r"D:\my_programming\openpose\output\output_json\jm_golf_004\jm_golf_004_000000000000_keypoints.json"
read_openpose_json(file_path)
