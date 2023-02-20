# Finding words in video frames

This is a simple tool to find words in videos using OCR (tesseract). It can be helpful for analyzing screen recordings of software user studies. The python script will output a list of timestamps where the word (or phrase) was found in the video.

## Preprocessing of video frames

The python script analyzes single video frames stored in a folder. The frames can be extracted from a video using ffmpeg. The following command will extract one frame per second and store them in the folder 'frames':

```
$ ffmpeg -i input_video.mp4 -r 1 -qscale:v 2 frames/%04d.jpg
```
whereas  ```-r 1``` means _one frame per second_ and  ```-qscale:v 2``` controls the _jpg quality_.


### Alternative ffmpeg method using fps filter
```$ ffmpeg -i input_vide.mp4 -vf fps=1/3 -qscale:v 2 frames/%04d.jpg```

```fps=1/3``` means one frame every three seconds

## Usage

### Python dependencies

- pytesseract
- PIL

### Run the script
```python videomatcher.py```
