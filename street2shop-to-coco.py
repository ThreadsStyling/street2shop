import argparse
import json
import os

# As extracted from modanet2018_instances_train.json
MODANET_CLASSES = {
      "bag": 1,
      "belt": 2,
      "boots": 3,
      "footwear": 4,
      "outer": 5,
      "dress": 6,
      "sunglasses": 7,
      "pants": 8,
      "top": 9,
      "shorts": 10,
      "skirt": 11,
      "headwear": 12,
      "scarf/tie": 13
}

# Street2Shop-to-Modanet category mapping. All other categories will
# be ignored.
CATEGORY_MAPPING = {
    'bags': 'bag',
    'belts': 'belt',
    'dresses': 'dress',
    'eyewear': 'sunglasses',
    'footwear': 'footwear',
    'hats': 'headwear',
    'leggings': 'pants',
    'outerwear': 'outer',
    'pants': 'pants',
    'skirts': 'skirt',
    'tops': 'top'
}

def get_args():
    parser = argparse.ArgumentParser(description="""
    Convert Street2Shop metadata to COCO annotations.
    """)
    parser.add_argument("meta", nargs='+')
    parser.add_argument("out_file",
                        help="File to write COCO-format annotations to")
    return parser.parse_args()

def convert_file(street2shop_meta):
    s2s_category = os.path.splitext(os.path.basename(street2shop_meta))[0].split('_')[-1]
    print("%s → %s" % (street2shop_meta, CATEGORY_MAPPING[s2s_category]))

    annotations = []
    with open(street2shop_meta, mode='r') as f:
        for p in json.load(f):
            bb = {
                "image_id": "%09d" % p['photo'],
                "category_id": MODANET_CLASSES[CATEGORY_MAPPING[s2s_category]],
                "bbox": [
                    p['bbox']['left'],
                    p['bbox']['top'],
                    p['bbox']['width'],
                    p['bbox']['height']
                ]
            }
            annotations.append(bb)

    return annotations

def main():
    args = get_args()

    annotations = []

    for m in args.meta:
        annotations += convert_file(m)

    print('%d products total' % len(annotations))

    with open(args.out_file, 'w') as f:
        f.write(json.dumps({"annotations": annotations}, indent=4))

if __name__ == "__main__":
    main()
