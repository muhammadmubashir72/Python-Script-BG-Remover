from rembg import remove
import os

input_folder = "input_images"
output_folder = "output_images"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):

        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".png")

        with open(input_path, "rb") as i:
            input_data = i.read()

        output_data = remove(input_data)

        with open(output_path, "wb") as o:
            o.write(output_data)

        print(f"Done: {file}")

print("All images processed")

# from rembg import remove

# input_path = "input.jpg"
# output_path = "output.png"

# with open(input_path, "rb") as i:
#     with open(output_path, "wb") as o:
#         o.write(remove(i.read()))

# print("Done")