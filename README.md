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
cat ../photos/photos.txt | sed -e 's/,/ /' | tr ' ' '\n' | parallel --bar -N2 '[ ! -e {1} ] && wget --quiet {2} -O {1}'
```
