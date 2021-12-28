# nClusterFramework

Read the docs here for more info: https://nclusterframework.readthedocs.io/en/latest/

## Description
A Framework for clustering multidimensional time series data based on windows of time. This is primarily designed for ingesting and clustering musical data.

This framework, as of now, is only designed for clustering. There is no featurization or visualization, just JSON inputs and JSON outputs.

---

## General Functionality
### nCluster
nCluster is the parent object, which includes parameters, a list of Feature names, a dictionary of channels, a dictionary of flags, and a dictionary of info.

The point of nCluster is to assign windows to certain time data in order to cluster those windows based on certain characteristics.

### Channels
Channels allow the user to organize organize different streams of temporal data. For instance, one channel could be used to store features derived from acoustical data from a drum, while another channel could be used to store the same features from a saxophone. Within one instance of the framework, the same features must be used for each channel, as that is necessary for clustering to occur

In essence, a channel is a 2D structure, where 1D is time and the second dimension is features. Each element in a channel has a uid (unique identifier), allowing it to be associated with flags and info

### Features
Features are the vector used to define the content of a particular timestamp.

### Flags
 - start_beat: weather or not a flag coresponds to the beginning of a beat
 - end_beat: weather or not a flag coresponds to the end of a beat or not


Internally used flags which denote specific things of importance. within a channel. Structurally the flags dictionary has the following content:
```
{(channel, uid): {name: "flag name"}}
```