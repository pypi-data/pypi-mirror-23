# cloud-volume

Python client for reading and writing to Neuroglancer Precomputed volumes on cloud services. (https://github.com/google/neuroglancer/tree/master/src/neuroglancer/datasource/precomputed)

When working with a particular dataset, say an EM scan of a mouse, fish, or fly brain, you'll typically store that as a grayscale data layer accessible to neuroglanger. You may store additional labellings and processing results as other layers.


## Usage

Supports reading and writing to neuroglancer data layers on Amazon S3, Google Storage, and the local file system.

Supported URLs are of the forms:

$PROTOCOL://$BUCKET/$DATASET/$LAYER  

Supported Protocols:
	- gs:   Google Storage
	- s3:   Amazon S3
	- file: Local File System (absolute path)


```
vol = CloudVolume('gs://mybucket/retina/image') # Basic Example
image = vol[:,:,:] # Download the entire image stack into a numpy array
vol[64:128, 64:128, 64:128] = image # Write a 64^3 image to the volume
```

## Setup

```
git clone git@github.com:seung-lab/cloud-volume.git
cd cloud-volume
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```



