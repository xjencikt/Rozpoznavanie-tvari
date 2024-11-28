import os
import pandas as pd
from deepface import DeepFace

def face_detected(img_path):
    try:
        result = DeepFace.detectFace(img_path=img_path)
        if result is not None:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", str(e))
        return False

folder_path = "../BIOM2/aaa/raceCheck"

analysis_results = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        img_path = os.path.join(root, file)

        if img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            if face_detected(img_path):
                result = DeepFace.analyze(img_path=img_path, enforce_detection=True, detector_backend="mtcnn")[0]

                folder_name = os.path.basename(root)
                image_name = file

                result['Foldername'] = folder_name
                result['Imagename'] = image_name

                analysis_results.append(result)
            else:
                print("Face not found in:", img_path)

df = pd.DataFrame(analysis_results)

df.to_csv('featuresALLmtcnn.csv', index=False)
