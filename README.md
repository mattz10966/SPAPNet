# 

# SPAPNet: Spatial Pyramidal Attention Parkinson’s tremor classification Network
![Image text](https://github.com/mattz10966/SPAPNet/blob/main/Framework.png)

Pose-based Tremor Classification for Parkinson’s Disease Diagnosis from Video

Parkinson's disease (PD) is a progressive neurodegenerative disorder that results in a variety of motor dysfunction symptoms, including tremor, bradykinesia, rigidity and postural instability. The diagnosis of PD mainly relies on clinical experience rather than a definite medical test, and the diagnostic accuracy is only about 73-84% since it is challenged by the subjective opinions or experiences of different medical experts. Therefore, an efficient and interpretable automatic early-onset PD diagnosis system is valuable for supporting clinicians for more robust diagnostic decision-making. To this end, we propose to classify Parkinson's tremor since it is one of the most predominant symptoms for early-onset PD with strong generalizability. Different from other computer-aided time and resource-consuming Parkinson's Tremor (PT) classification systems that rely on wearable sensors, we propose SPAPNet, which only requires consumer-grade non-intrusive video recordings as input to classify PT for early diagnosis of PD. For the first time, we propose to use a novel attention module with a lightweight pyramidal channel-squeezing-fusion architecture to extract relevant PT information and filter the noise efficiently. This design aids in improving both classification performance and system interpretability. Experimental results show that our system outperforms state-of-the-arts by achieving a balanced accuracy of 90.9% and an F1-score of 90.6% in classifying PT with the non-PT class. 

For the full TIM-TREMOR dataset, please refer to https://data.4tu.nl/articles/dataset/Technology_in_Motion_Tremor_Dataset_TIM-Tremor/12694256?file=24034127


# Initialization
python >= 3.7

pytorch
tensorflow ==1.14.0

# Library requirement and installation
`
pip install requirement.txt
`
`
cd torchlight; python setup.py install; cd ..
`
# Getting started

For a quick training with example data on the TIM-TREMOR dataset
```
python start.py
```

Full evaluation code will be coming soon!


