# DSP visualization tools for python
## Introduction
Digital signal processing can analyze, transform, and filter input signals. It has a wide range of applications, such as voice signal processing, digital image processing, vibration signal processing, biomedical processing, and so on. Python contains a variety of visualization libraries that can process digital signals and display the results in a visual form for easy understanding and analysis.

## Visualization tools
### Matplotlib
Matplotlib is the oldest and most widely used data visualization library for Python. Its design is very similar to MATLAB and is the basis for many other libraries.

#### Signal processing
Matplotlib can perform signal processing, such as cleaning noisy sine waves.
Create a sine wave with a frequency of 2000Hz, then create a noise wave with a frequency of 80HZ, convert them into numpy arrays, and add the two to generate a noisy sine wave. The results are shown in Figure 1.   
<p align="center">
<img src="https://github.com/lqi25/MiniProject3/blob/master/img/fig1.png"/> 
</p>
The synthetic wave is filtered, and the noise wave whose frequency is too small is filtered out. The result is shown in fig2. After the filtering, the displayed sine wave is the same as the original wave.   
<p align="center">
<img src="https://github.com/lqi25/MiniProject3/blob/master/img/fig2.png"/> 
</p>

### Pygal
pygal, which provides interactive images that can be embedded directly into a web browser. It can output charts to svg format. With just a few simple lines of code, you can make charts for histograms, line charts, pie charts, and more.


### Seaborn
Seaborn has a more advanced API package based on matplotlib, which can make a variety of statistical charts, which is convenient for users to analyze and statistics the data.
