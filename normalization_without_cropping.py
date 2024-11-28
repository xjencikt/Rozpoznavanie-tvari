import cv2
import os


def convert_and_normalize_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    subfolders = [os.path.join(input_folder, folder) for folder in os.listdir(input_folder) if
                  os.path.isdir(os.path.join(input_folder, folder))]

    for folder in subfolders:
        files = os.listdir(folder)

        for file in files:
            if file.lower().endswith(('.jpg')):
                image_path = os.path.join(folder, file)
                image = cv2.imread(image_path)

                if image is not None:
                    bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    normalized_image = cv2.normalize(bgr_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

                    output_path = os.path.join(output_folder, os.path.relpath(folder, input_folder), file)
                    output_subfolder = os.path.dirname(output_path)
                    if not os.path.exists(output_subfolder):
                        os.makedirs(output_subfolder)
                    cv2.imwrite(output_path, normalized_image)
                    print(f"Processed {file}")
                else:
                    print(f"Could not read {file}")


input_folder = "images_original"
output_folder = "new_again"
convert_and_normalize_images(input_folder, output_folder)
