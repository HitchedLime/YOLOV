import json

def convert_to_coco_format(input_data):
    coco_format = {
        "info": input_data["info"],
        "images":[],
        "videos": input_data["videos"],
        "annotations":[],
        "categories": input_data["categories"]
    }
    for ann in input_data["annotations"]:
        ann_dic=ann
        ann_dic["image_id"]= ann["video_id"]
        coco_format["annotations"].append(ann_dic)



    for  data  in input_data["videos"]:

        for file_name in data["file_names"]:
            img_info = {}
            img_info["file_name"]= file_name
            img_info["width"]=data["width"]
            img_info["height"]=data["height"]
            img_info["id"]=data["id"]
            coco_format["images"].append((img_info))






    return coco_format

# Load your input JSON
input_json_path = 'ovis_train.json'  # Change this to your input file path
output_json_path = 'ovis_coco_format_train.json'  # Change this to your desired output file path

with open(input_json_path, 'r') as f:
    input_data = json.load(f)

# Convert to COCO format
coco_data = convert_to_coco_format(input_data)

# Save the COCO formatted data to a new JSON file
with open(output_json_path, 'w') as f:
    json.dump(coco_data, f, indent=4)

print(f"Converted dataset saved to {output_json_path}")