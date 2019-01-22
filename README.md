#### Street2shop dataset tools

http://www.tamaraberg.com/street2shop/

Get the dataset:
```
bash get_street2shop.sh
```

Download the images:
```
mkdir images
cd images
cat ../photos/photos.txt | sed -e 's/,/ /' | tr ' ' '\n' | parallel --bar -N2 '[ ! -e {1} ] && wget --timeout 10 --quiet {2} -O {1}'
```

Convert annotations to COCO format:

```
python3 street2shop-to-coco.py meta/json/{train,test}_*.json street2shop_coco.json
```
