

## Collecting object labels

```
tmp = [labels[i] for i in classes[scores>0.5].astype(int)]
from collections import Counter
Counter(tmp)
>>> Counter({'cow': 4, 'person': 2})
tmp2 = Counter(tmp)
tmp2['cow']
```



## Image processing
To run the image processing script:
```
python TFLite_detection_image.py --modeldir=Sample_TFLite_model --image=test1.jpg
```


## InfluxDB

Drop the whole series:

```
DROP SERIES FROM "tflite_demo"
```
