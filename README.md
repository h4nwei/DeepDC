# DeepDC: Deep Distance Correlation as a Perceptual Image Quality Evaluator

This is the repository of paper [DeepDC: Deep Distance Correlation as a Perceptual Image Quality Evaluator](https://arxiv.org/pdf/2211.04927v2.pdf). 

### Highlights:

* A novel FR-IQA model that fully utilizes the *texture-sensitiv*e of pre-trained deep neural network (DNN) features, which computes **distance correlation** in the deep feature domain 
* The model is **exclusively** based on the features of the pre-trained DNNs and does not rely on fine-tuning with mean opinion scores (MOSs)
* Extensive experiments achieve superior performance on five standard IQA datasets, one perceptual similarity dataset, two texture similarity datasets, and one geometric transformation dataset
* It can be employed as an objective function in texture synthesis and neural style transfer
   



### ====== PyTorch Implementation ======
**Installation:** 
- ```pip install DeepDC-PyTorch```

### Requirements: 
- Python >= 3.6
- PyTorch >= 1.0

**Usage:** 
```python
from DeepDC_PyTorch import DeepDC
model = DeepDC()
# calculate DeepDC between X, Y (a batch of RGB images, data range: 0~1) 
deepdc_score = model(X, Y)
```
or

```bash
git clone https://github.com/h4nwei/DeepDC
cd DeepDC_PyTorch
python DeepDC.py --ref <ref_path> --dist <dist_path>
```


## Reference

- R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang, “The unreasonable effectiveness of deep features as a perceptual metric,” in *IEEE Conference on Computer Vision and Pattern Recognition*, 2018, pp. 586–595.
- K. Ding, K. Ma, S. Wang, and E. P. Simoncelli, “Image quality assessment: Unifying structure and texture similarity,” *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 44, no. 5, pp. 2567–2581, 2020.
- I. Kligvasser, T. Shaham, Y. Bahat, and T. Michaeli, “Deep selfdissimilarities as powerful visual fingerprints,” in *Neural Information Processing Systems*, 2021, pp. 3939–3951.

## Citation
```bibtex
@article{zhu2023DeepDC,
title={DeepDC: Deep Distance Correlation as a Perceptual Image Quality Evaluator},
author={Zhu, Hanwei and Chen, Baoliang and Zhu, Lingyu and Wang, Shiqi and Lin, Weisi},
journal={CoRR},
volume = {abs/2211.04927v2},
year={2023},
url = {https://arxiv.org/pdf/2211.04927v2.pdf}
}
