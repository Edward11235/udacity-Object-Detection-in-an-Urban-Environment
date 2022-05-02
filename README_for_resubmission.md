### Project overview
This repository trains a SSD model that can locate and classify pedestrians, vehicles, and cycles in the image. It uses tensorflow object detection api and uses pipeline_new.config to denote the structure of the neural network that we want to train. Object detection is important since we need to avoid pedestrians, vehicles, and cycles when we test a autonomous car on the road.

### Set up
All the steps are basically covered in this README file.
First, we need to split the dataset into train and validation set. create.split.py contains the method to do so.
Second, we need to train the model. The Train section above shows how to do that 
Third, we need to evaluate and store the model.
In the end, we can make a gif to show the performance of our model.


### Dataset
#### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.

The chart I want to use is in Exploratory Data Analysis.ipynb.
In exploratory analysis section, I checked some images and there are mainly vehicles in the picture with a few cyclists. Also, I drew a graph in the Exploratory Data Analysis.ipynb, and found that there are about 3600 vehicles, 1200 pedestrians, and 100 cyclists. This indicates that our model mainly needs to recognize cars, and since we have little data about cyclists, we may not perform well in term of detecting cyclists. Hence we need more data about cyclists.

Also, I saw some images that were taken in the night. I think we can used data augmentation to convert daytime images into nighttime images by simply decrease it's brightness. This gives us more meaningful data.

#### Cross validation
As I wrote in create_split.py, I put 80% of data into training set and 20% remaining data into test set.
 
Justification:
First of all, cross validation is used to determine if we have overfitting problem. 
We don't want to put the majority of data to validation set since in this case, we loss data that can be trained.
Also, we don't want to put too little data to validation set since in this case, the result of cross validation may not be meanful (like, if one image indicates that there is overfitting, it may just be an coincidance)
8:2 is a good ratio since 80% data is enough for training, and 20% data in cross validation is significant enough to determine if there is over-fitting.

### Training
#### Experiment_1
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.
As shown in the gif, the resulting model is prerry well in terms of detecting cars. However, one weakness is that it has many repetitive bounding boxes for one car. Nevertheless, I think this is not a big deal since I can use non-maximum suppression techniques to deal with it.
The total loss is about 0.04.

#### Experiment_2
There is a screenshot in the workspace that is the tensorboard of my training. For experiment 2, we can see that the total loss is small, about 2, when learning rate is about 0.01. However, after learning rate increases to 0.08, the total
loss immediately increases to more than 20.  This indicates that I should not use a too big learning rate. 

#### Improve on the reference
#### I improve the previous two experiments and call it experiment_3
To improve the model, I first added grey-scale augmentation to pipeline.config as illustrated in Explore augmentations.ipynb. Then, I increased warm up steps to 100. Afterwards, I can tell there's an improvmenet since more cars were recognized in the gif, but it's not a signification improvement. Also, after increasing warm up steps, the time for trains was longer.
Also, I decrease learning rate to 0.02 to fix the problem mentioned in experiment_2
Moreover, I increase the batch_size to 5 this time to further improve the performance.

As shown in the screenshot for experiment_3, the total loss continuously decreases, which is much better than the performance of experiment_2. In the end, the total loss of experiemnt reaches about 2, which is a much better result.
These all indicates that my improvements work.
