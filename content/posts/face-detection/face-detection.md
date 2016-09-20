Title: Face detection using MB-LBP and Adaboost
Date: 2016-08-23
Category: project
Tags: ml, detection
Slug: face-detection
Authors: Valentin Iovene

# Abstract

Face detection is the task of localizing faces in images. One must distinguish
between face *detection* and face *recognition*. The latter is the task of
recognizing someone from an image of her face.

Face detection can be seen as a function $f$ taking an image $x$ as input and
returning *bounding boxes* around the faces contained in this image.

<div style="text-align: center;">
<img alt="Face detection seen as a function"
src="posts/face-detection/as-a-function.svg" width="70%">
</div>

Face detection

- is used by *Facebook* to detect faces in images you share and make it easier
for you to tag your friends,
- can be used to **track** faces in videos of people moving around (e.g.
*Snapchat*'s face swap feature requires face detection),
- and is a prerequisite for any real-life applications of face recognition
*(e.g. Law Enforcement localizing a suspect in a big city using video
surveillance systems)*.

The detection process needs to be fast enough to keep up with the demand
(millions of users / billions of streamed images).

There has been extensive research in this area but one of the major
breakthrough happened in 2001 when *Paul Viola* and *Michael Jones* published
their object detection framework (which was named the "Viola-Jones framework")
(cite).

Even though it was invented more than 15 years ago *(time of writing)*,
*OpenCV*'s face detection implementation (source) is still based on it.

This article explains how the *Multi-Block Local Binary Patterns (MB-LBP)*
visual descriptors (which will soon be introduced) can be used in lieu of the
*Haar-like features* used by the original *Viola-Jones* framework for face
detection. This approach was demonstrated by Zhang et al. in 2007. (cite)

# MB-LBP definition

A face detection algorithm looks at *features* of an image to determine whether
it is a face or not.

MB-LBP of different sizes and at different locations are considered

<div style="text-align: center;">
<img alt="MB-LBP features" src="posts/face-detection/animated_mblbp.gif">
</div>

```cpp
std::vector<mblbp_feature> mblbp_all_features()
{
  std::vector<mblbp_feature> features;

  for(int block_w = min_block_size; block_w <= max_block_size; block_w += 3)
    for(int block_h = min_block_size; block_h <= max_block_size; block_h += 3)
      for(int x = 0; x <= initial_window_w - block_w; ++x)
        for(int y = 0; y <= initial_window_h - block_h; ++y)
          features.push_back(mblbp_feature(x, y, block_w, block_h));

  return features;
}
```
