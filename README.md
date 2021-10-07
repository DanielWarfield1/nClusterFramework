# MelClusterFramework
Framework for streaming and clustering mel spectrogram data

currently accepts the following commands for setting up:

```
set num_channels (int)
set num_flags (int, should be >= 1)
set input_size (int)
set channel_length (int)
set syncronous_function syn_func
set asyncronous_function async_func
set win_function win_func
set window_size (int)
set score_function score_func
initialize
```

and these commands for running

```python
add [(channel), [(mel spectrogram values, input_size)], [(flags, num_flags)]]
run asynch
```

for add, the first flag should be weather or not this mel spectrogram coresponds to the start of a beat.

run asynch plots a tsne plot



here's an example of actually getting it running:

```
set num_channels 2
set num_flags 2
set input_size 5
set channel_length 100
set syncronous_function syn_func
set asyncronous_function async_func
set win_function win_func
set window_size 5
set score_function score_func
initialize

add [0, [0,1,2,3,4], [True, 1]]
add [0, [0,1,2,3,4], [False, 1]]
add [0, [0,0,2,3,4], [False, 1]]
add [0, [0,0,2,3,4], [False, 1]]
add [0, [0,0,2,3,4], [True, 1]]
```

