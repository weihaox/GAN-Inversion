# <p align=center>`awesome gan-inversion papers`</p>
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

This repo is a collection of resources on GAN inversion, as a supplement for our [survey](https://arxiv.org/abs/2101.05278):

```bibtex
@article{xia2021survey,
  author  = {Xia, Weihao and Zhang, Yulun and Yang, Yujiu and Xue, Jing-Hao and Zhou, Bolei and Yang, Ming-Hsuan},
  title   = {GAN Inversion: A Survey},
  journal = {arXiv preprint arXiv: 2101.05278},
  year={2021}
}
```

## Contributing

Feedback and contributions are welcome!

If you think I have missed out on something (or) have any suggestions (papers, implementations and other resources), feel free to [pull a request](https://github.com/xiaweihao/awesome-image-translation/pulls).

I have released the [latex files](https://github.com/weihaox/documents/tree/main/gan-inversion). Please [pull a request](https://github.com/weihaox/documents/pulls), open an issue, or send me an email if you find any inappropriate expressions of the survey.

markdown format:
``` markdown
**Here is the Paper Name.**<br>
*[Author 1](homepage), Author 2, and Author 3.*<br>
Conference or Journal Year. [[PDF](link)] [[Project](link)] [[Github](link)] [[Video](link)] [[Data](link)]
```
## Survey

[[Papers on Generative Modeling](https://github.com/zhoubolei/awesome-generative-modeling)]

**GAN Inversion: A Survey.**<br>
*Weihao Xia, Yulun Zhang, Yujiu Yang, Jing-Hao Xue, Bolei Zhou, Ming-Hsuan Yang.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2101.05278)]

## inverted pretrained model

**Alias-Free GAN: Alias-Free Generative Adversarial Networks.**<br>
*Tero Karras, Miika Aittala, Samuli Laine, Erik Härkönen, Janne Hellsten, Jaakko Lehtinen, Timo Aila.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2106.12423)] [[Project](https://nvlabs.github.io/alias-free-gan)] [[Github](https://github.com/NVlabs/alias-free-gan)] [[Rosinality](https://github.com/rosinality/alias-free-gan-pytorch)]

**StyleGAN2-Ada: Training Generative Adversarial Networks with Limited Data.**<br>
*Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, Timo Aila.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2006.06676)] [[Github](https://github.com/NVlabs/stylegan2-ada)] [[Steam StyleGAN2-ADA](https://github.com/woctezuma/steam-stylegan2-ada)]

**StyleGAN2: Analyzing and Improving the Image Quality of StyleGAN.**<br>
*[Tero Karras](https://research.nvidia.com/person/tero-karras), [Samuli Laine](https://research.nvidia.com/person/samuli-laine), [Miika Aittala](https://research.nvidia.com/person/miika-aittala), Janne Hellsten, Jaakko Lehtinen, [Timo Aila](https://research.nvidia.com/person/timo-aila).*<br>
CVPR 2020.
[[PDF](https://arxiv.org/abs/1912.04958)] 
[[Offical TF](https://github.com/NVlabs/stylegan2)]
[[PyTorch](https://github.com/rosinality/stylegan2-pytorch)]
[[Unoffical Tensorflow 2.0](https://github.com/manicman1999/StyleGAN2-Tensorflow-2.0)]

**StyleGAN: A Style-Based Generator Architecture for Generative Adversarial Networks.**<br>
*Tero Karras, Samuli Laine, Timo Aila.*<br>
CVPR 2019. [[PDF](https://arxiv.org/abs/1812.04948)] [[Offical TF](https://github.com/NVlabs/stylegan)]

**ProGAN: Progressive Growing of GANs for Improved Quality, Stability, and Variation.**<br>
*Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen.*<br>
ICLR 2018. [[PDF](https://arxiv.org/abs/1710.10196)] [[Offical TF](https://github.com/tkarras/progressive_growing_of_gans)]

## inversion method

This part contatins generatal inversion methods, while methods in the next *application* part are mainly designed for specific tasks.

**StyleVideoGAN: A Temporal Generative Model using a Pretrained StyleGAN.**<br>
*[Gereon Fox](https://www.mpi-inf.mpg.de/~gfox/), [Ayush Tewari](https://www.mpi-inf.mpg.de/~atewari/), Mohamed Elgharib, [Christian Theobalt](http://gvv.mpi-inf.mpg.de/).*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2107.07224)]

**Semantic and Geometric Unfolding of StyleGAN Latent Space.**<br>
*Mustafa Shukor, Xu Yao, Bharath Bhushan Damodaran, Pierre Hellier.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2107.04481)]

**Pivotal Tuning for Latent-based Editing of Real Images.**<br>
*Daniel Roich, Ron Mokady, Amit H. Bermano, Daniel Cohen-Or.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2106.05744.pdf)] [[Github](https://github.com/danielroich/PTI)]

**Prior Image-Constrained Reconstruction using Style-Based Generative Models.**<br> 
*Varun A Kelkar, Mark Anastasio.*<br>
ICML 2021. [[PDF](https://arxiv.org/pdf/2102.12525.pdf)]

**Ensembling with Deep Generative Views.**<br> 
*Lucy Chai, Jun-Yan Zhu, Eli Shechtman, Phillip Isola, Richard Zhang.*<br> 
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.14551)] [[Github](https://github.com/chail/gan-ensembling)] [[Project](https://chail.github.io/gan-ensembling/)]

**Disentangled Face Attribute Editing via Instance-Aware Latent Space Search.**<br>
*Yuxuan Han, [Jiaolong Yang](http://jlyang.org/), Ying Fu.*<br>
IJCAI 2021. [[PDF](https://arxiv.org/abs/2105.12660)] [[Github](https://github.com/yxuhan/IALS)]

**Intermediate Layer Optimization for Inverse Problems using Deep Generative Models.**<br>
*Giannis Daras, Joseph Dean, Ajil Jalal, Alexandros G. Dimakis.*<br>
ICML 2021. [[PDF](https://arxiv.org/abs/2102.07364)] [[Github](https://github.com/giannisdaras/ilo)]

**Explaining in Style: Training a GAN to explain a classifier in StyleSpace.**<br> 
*Oran Lang, Yossi Gandelsman, Michal Yarom, Yoav Wald, Gal Elidan, Avinatan Hassidim, William T. Freeman, Phillip Isola, Amir Globerson, Michal Irani, Inbar Mosseri.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2104.13369)] [[Project](https://explaining-in-style.github.io/)]

**Transforming the Latent Space of StyleGAN for Real Face Editing.**<br> 
*Heyi Li, Jinlong Liu, Yunzhi Bai, Huayan Wang, Klaus Mueller.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2105.14230)] [[Github](https://github.com/AnonSubm2021/TransStyleGAN)]

**A Simple Baseline for StyleGAN Inversion.**<br> 
*Tianyi Wei, Dongdong Chen, Wenbo Zhou, Jing Liao, Weiming Zhang, Lu Yuan, Gang Hua, Nenghai Yu.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2104.07661)] [[Github](https://github.com/wty-ustc/StyleGAN-Inversion-Baseline)] [[Project](https://wty-ustc.github.io/inversion/)]

**ReStyle: A Residual-Based StyleGAN Encoder via Iterative Refinement.**<br> 
*[Yuval Alaluf](https://yuval-alaluf.github.io/), [Or Patashnik](https://orpatashnik.github.io/), [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2104.02699)] [[Project](https://yuval-alaluf.github.io/restyle-encoder/)] [[Github](https://github.com/yuval-alaluf/restyle-encoder)]

**LatentCLR: A Contrastive Learning Approach for Unsupervised Discovery of Interpretable Directions.**<br> 
*Oğuz Kaan Yüksel, Enis Simsar, Ezgi Gülperi Er, Pinar Yanardag.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2104.00820)] [[Github](https://github.com/catlab-team/latentclr)]

**Using Latent Space Regression to Analyze and Leverage Compositionality in GANs.**<br> 
*[Lucy Chai](http://people.csail.mit.edu/lrchai/), [Jonas Wulff](http://people.csail.mit.edu/jwulff/), [Phillip Isola](http://web.mit.edu/phillipi/).*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=sjuuTm4vj0)] [[Github](https://github.com/chail/latent-composition)] [[Project](https://chail.github.io/latent-composition/)] [[Colab](https://colab.research.google.com/drive/1p-L2dPMaqMyr56TYoYmBJhoyIyBJ7lzH?usp=sharing)]

**Hijack-GAN: Unintended-Use of Pretrained, Black-Box GANs.**<br>
*Hui-Po Wang, Ning Yu, Mario Fritz.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.14107)]

**e4e: Designing an Encoder for StyleGAN Image Manipulation.**<br>
*[Omer Tov](https://yotamnitzan.github.io/), Yuval Alaluf, Yotam Nitzan, Or Patashnik, Daniel Cohen-Or.*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2102.02766)] [[Github](https://github.com/omertov/encoder4editing)]

**Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation.**<br>
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing.*<br>
ICLR 2021. [[PDF](https://arxiv.org/abs/2102.01187)]

**Improved StyleGAN Embedding: Where are the Good Latents?**<br>
*Peihao Zhu, Rameen Abdal, [Yipeng Qin](http://yipengqin.github.io/), [Peter Wonka](http://peterwonka.net/).*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2012.09036)]

**Learning a Deep Reinforcement Learning Policy Over the Latent Space of a Pre-trained GAN for Semantic Age Manipulation.**<br>
*Kumar Shubham, Gopalakrishnan Venkatesh, Reijul Sachdev, Akshi, Dinesh Babu Jayagopi, G. Srinivasaraghavan.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.00954)]

**Lifting 2D StyleGAN for 3D-Aware Face Generation.**<br>
*[Yichun Shi](https://seasonsh.github.io/), Divyansh Aggarwal, [Anil K. Jain](http://www.cse.msu.edu/~jain/).*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.13126)]

**Navigating the GAN Parameter Space for Semantic Image Editing.**<br>
*Anton Cherepkov, Andrey Voynov, Artem Babenko.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.13786)] [[Github](https://github.com/yandex-research/navigan)]

**Augmentation-Interpolative AutoEncoders for Unsupervised Few-Shot Image Generation.**<br>
*Davis Wertheimer, Omid Poursaeed, Bharath Hariharan.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.13026)]

**Mask-Guided Discovery of Semantic Manifolds in Generative Models.**<br>
*[Mengyu Yang](https://mengyu.page/), [David Rokeby](https://www.cdtps.utoronto.ca/people/directories/all-faculty/david-rokeby), [Xavier Snelgrove](https://wxs.ca/).*<br>
Workshop on Machine Learning for Creativity and Design (NeurIPS) 2020. [[PDF](https://github.com/bmolab/masked-gan-manifold/blob/main/masked-gan-manifold.pdf)] [[Github](https://github.com/bmolab/masked-gan-manifold)]

**Unsupervised Discovery of Disentangled Manifolds in GANs.**<br>
*Yu-Ding Lu, Hsin-Ying Lee, Hung-Yu Tseng, Ming-Hsuan Yang.*<br>
arxiv 2020. [[PDF]](https://arxiv.org/abs/2011.11842)]

**StyleSpace Analysis: Disentangled Controls for StyleGAN Image Generation.**<br>
*Zongze Wu, Dani Lischinski, Eli Shechtman.*<br>
CVPR 2021 (oral). [[PDF]](https://arxiv.org/abs/2011.12799) [[Github](https://github.com/betterze/StyleSpace)]

**On The Inversion Of Deep Generative Models (When and How Can Deep Generative Models be Inverted?).**<br>
*Aviad Aberdam, Dror Simon, Michael Elad.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2006.15555)] [[OpenReview](https://openreview.net/pdf?id=TSrvUnWkjGR)]

**PIE: Portrait Image Embedding for Semantic Control.**<br> 
*[A. Tewari](http://people.mpi-inf.mpg.de/~atewari/), M. Elgharib, M. BR, F. Bernard, H-P. Seidel, P. P‌érez, M. Zollhöfer, C.Theobalt.*<br> 
SIGGRAPH Asia 2020. [[PDF](http://gvv.mpi-inf.mpg.de/projects/PIE/data/paper.pdf)] [[Project](http://gvv.mpi-inf.mpg.de/projects/PIE/)]

**Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation.**<br>
*Elad Richardson, Yuval Alaluf, Or Patashnik, Yotam Nitzan, Yaniv Azar, Stav Shapiro, Daniel Cohen-Or.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2008.00951)] [[Github](https://github.com/eladrich/pixel2style2pixel)] [[Project](eladrich.github.io/pixel2style2pixel/)]

**GAN-Control: Explicitly Controllable GANs.**<br>
*Alon Shoshan, Nadav Bhonker, Igor Kviatkovsky, Gerard Medioni.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2101.02477)]

**Understanding the Role of Individual Units in a Deep Neural Network.**<br>
*David Bau, Jun-Yan Zhu, Hendrik Strobelt, Agata Lapedriza, Bolei Zhou, Antonio Torralba.*<br>
National Academy of Sciences 2020. [[PDF](https://arxiv.org/abs/2009.05041)] [[Github](https://github.com/davidbau/dissect/)] [[Project](https://dissect.csail.mit.edu/)]

**GHFeat: Generative Hierarchical Features from Synthesizing Images.**<br>
*Yinghao Xu, Yujun Shen, Jiapeng Zhu, Ceyuan Yang, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2007.10379.pdf)] [[Github](https://github.com/genforce/ghfeat)] [[Project](https://genforce.github.io/ghfeat/)]

**Collaborative Learning for Faster StyleGAN Embedding.**<br>
*Shanyan Guan, Ying Tai, Bingbing Ni, Feida Zhu, Feiyue Huang, Xiaokang Yang.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2007.01758)]

**Disentangling in Latent Space by Harnessing a Pretrained Generator.**<br>
*Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2005.07728)]

**Face Identity Disentanglement via Latent Space Mapping.**<br>
*Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or.*<br>
SIGGRAPH Asia (TOG) 2020. [[PDF](https://arxiv.org/abs/2005.07728)] [[Github](https://github.com/YotamNitzan/ID-disentanglement)]

**Transforming and Projecting Images into Class-conditional Generative Networks.**<br>
*[Minyoung Huh](http://minyounghuh.com/), [Richard Zhang](https://richzhang.github.io/), [Jun-Yan Zhu](https://people.csail.mit.edu/junyanz/), [Sylvain Paris](http://people.csail.mit.edu/sparis/), [Aaron Hertzmann](https://www.dgp.toronto.edu/~hertzman/).*<br>
ECCV 2020. [[PDF](http://arxiv.org/abs/2005.01703)] [[Github](https://github.com/minyoungg/GAN-Transform-and-Project)] [[Project](https://minyoungg.github.io/GAN-Transform-and-Project/)]

**Improving Inversion and Generation Diversity in StyleGAN using a Gaussianized Latent Space.**<br>
*[Jonas Wulff](http://people.csail.mit.edu/jwulff/), Antonio Torralba.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2009.06529)]

**MimicGAN: Robust Projection onto Image Manifolds with Corruption Mimicking.**<br>
*[Rushil Anirudh](https://rushila.com/), [Jayaraman J. Thiagarajan](https://jjthiagarajan.com/), [Bhavya Kailkhura](https://people.llnl.gov/kailkhura1), [Timo Bremer](https://people.llnl.gov/bremer5).*<br>
IJCV 2020. [[PDF](https://link.springer.com/article/10.1007/s11263-020-01310-5)]

**StyleFlow: Attribute-conditioned Exploration of StyleGAN-Generated Images using Conditional Continuous Normalizing Flows.**<br>
*Rameen Abdal, Peihao Zhu, Niloy Mitra, Peter Wonka.*<br>
Siggraph (TOG) 2021. [[PDF](https://arxiv.org/abs/2008.02401)] [[Github](https://rameenabdal.github.io/StyleFlow)]

**Rewriting a Deep Generative Model.**<br>
*David Bau, Steven Liu, Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2007.15646)] [[Github](https://github.com/davidbau/rewriting)]

**StyleGAN2 Distillation for Feed-forward Image Manipulation.**<br>
*Yuri Viazovetskyi, Vladimir Ivashkin, Evgeny Kashin.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2003.03581)] [[Github](https://github.com/EvgenyKashin/stylegan2-distillation)]

**In-Domain GAN Inversion for Real Image Editing.**<br>
*Jiapeng Zhu, Yujun Shen, Deli Zhao, Bolei Zhou.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2004.00049)] [[Project](https://genforce.github.io/idinvert/)] [[Github](https://github.com/genforce/idinvert)]

**Exploiting Deep Generative Prior for Versatile Image Restoration and Manipulation.**<br>
*Xingang Pan, Xiaohang Zhan, Bo Dai, Dahua Lin, Chen Change Loy, Ping Luo.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2003.13659)] [[Github](https://github.com/XingangPan/deep-generative-prior)]

**Your Local GAN: Designing Two Dimensional Local Attention Mechanisms for Generative Models.**<br>
*Giannis Daras, Augustus Odena, Han Zhang, Alexandros G. Dimakis.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1911.12287)]

**A Disentangling Invertible Interpretation Network for Explaining Latent Representations.**<br>
*Patrick Esser, Robin Rombach, Björn Ommer.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/2004.13166)] [[Project](https://compvis.github.io/iin/)] [[Github](https://github.com/CompVis/iin)]

**Editing in Style: Uncovering the Local Semantics of GANs.**<br>
*Edo Collins, Raja Bala, Bob Price, Sabine Süsstrunk.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/2004.14367)] [[Github](https://github.com/IVRL/GANLocalEditing)]

**Image Processing Using Multi-Code GAN Prior.**<br>
*[Jinjin Gu](http://www.jasongt.com/), Yujun Shen, Bolei Zhou.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1912.07116)] [[Project](https://genforce.github.io/mganprior/)] [[Github](https://github.com/genforce/mganprior)]

**Image2StyleGAN++: How to Edit the Embedded Images?**<br>
*Rameen Abdal, [Yipeng Qin](http://yipengqin.github.io/), Peter Wonka.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1911.11544)]

**Semantic Photo Manipulation with a Generative Image Prior.**<br>
*David Bau, Hendrik Strobelt, William Peebles, Jonas, Bolei Zhou, Jun-Yan Zhu, Antonio Torralba.*<br>
SIGGRAPH 2019. [[PDF](https://arxiv.org/abs/2005.07727)]

**Image2StyleGAN: How to Embed Images Into the StyleGAN Latent Space?**<br>
*Rameen Abdal, [Yipeng Qin](http://yipengqin.github.io/), Peter Wonka.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1904.03189)] [[Github](https://github.com/RameenAbdal/image2styleganv1-v2)]

**GAN-based Projector for Faster Recovery with Convergence Guarantees in Linear Inverse Problems.**<br>
*Ankit Raj, Yuqi Li, Yoram Bresler.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1902.09698)]

**Inverting Layers of a Large Generator.**<br>
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba.*<br>
ICCV 2019. [[PDF](https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_18.pdf)]

**Detecting Overfitting in Deep Generators via Latent Recovery.**<br>
*Ryan Webster, Julien Rabin, Loic Simon, Frederic Jurie.*<br>
CVPR 2019. [[PDF](https://openaccess.thecvf.com/content_CVPR_2019/papers/Webster_Detecting_Overfitting_of_Deep_Generative_Networks_via_Latent_Recovery_CVPR_2019_paper.pdf)][[Colab](https://colab.research.google.com/drive/1N6zP4xlPunWOkmakcl0mamfhq946nMLB?usp=sharing)]

**Inverting The Generator Of A Generative Adversarial Network (II).**<br>
*Antonia Creswell, Anil A Bharath.*<br>
TNNLS 2018. [[PDF](https://arxiv.org/abs/1802.05701)] [[Github](https://github.com/ToniCreswell/InvertingGAN)]

**Invertibility of Convolutional Generative Networks from Partial Measurements.**<br>
*Fangchang Ma, Ulas Ayaz, Sertac Karaman.*<br>
NeurIPS 2018. [[PDF](https://papers.nips.cc/paper/8171-invertibility-of-convolutional-generative-networks-from-partial-measurements)] [[Github](https://github.com/fangchangma/invert-generative-networks)]

**Metrics for Deep Generative Models.**<br>
*Nutan Chen, Alexej Klushyn, Richard Kurle, Xueyan Jiang, Justin Bayer, Patrick van der Smagt.*<br>
AISTATS 2018. [[PDF](https://arxiv.org/abs/1711.01204)]

**Towards Understanding the Invertibility of Convolutional Neural Networks.**<br>
*Anna C. Gilbert, Yi Zhang, Kibok Lee, Yuting Zhang, Honglak Lee.*<br>
IJCAI 2017.  [[PDF](https://arxiv.org/abs/1705.08664)]

**One Network to Solve Them All - Solving Linear Inverse Problems using Deep Projection Models.**<br>
*J. H. Rick Chang, Chun-Liang Li, Barnabas Poczos, B. V. K. Vijaya Kumar, Aswin C. Sankaranarayanan.*<br>
ICCV 2017. [[PDF](https://arxiv.org/abs/1703.09912)]

**Precise Recovery of Latent Vectors from Generative Adversarial Networks.**<br>
*Zachary C. Lipton, Subarna Tripathi.*<br>
ICLR 2017 workshop. [[PDF](https://arxiv.org/abs/1702.04782)] [[Github](https://github.com/SubarnaTripathi/ReverseGAN)]

**Inverting The Generator Of A Generative Adversarial Network.**<br>
*Antonia Creswell, Anil Anthony Bharath.*<br>
NIPSW 2016. [[PDF](https://arxiv.org/abs/1611.05644)]

**Generative Visual Manipulation on the Natural Image Manifold.**<br>
*Jun-Yan Zhu, Philipp Krähenbühl, Eli Shechtman, Alexei A. Efros.*<br>
ECCV 2016. [[PDF](https://arxiv.org/abs/1609.03552v2)]

## latent space navigation

Inversion is not the ultimate goal. The reason that we invert a real image into the latent space of a trained GAN model is that we can manipulate the inverted image in the latent space by discovering the desired code with certain attributes. This technique is usually known as latent space navigation, GAN steerability, latent code manipulation, or other names in the literature. Although often regarded as an independent research field, it acts as an indispensable component of GAN inversion for manipulation. Many inversion methods also involve efficient discovery of a desired latent code.

**LARGE: Latent-Based Regression through GAN Semantics.**<br>
*Yotam Nitzan, Rinon Gal, Ofir Brenner, Daniel Cohen-Or.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2107.11186)] [[Github](https://github.com/YotamNitzan/LARGE)] [[Project](https://yotamnitzan.github.io/LARGE)]

**StyleFusion: A Generative Model for Disentangling Spatial Segments.**<br>
*Omer Kafri, Or Patashnik, Yuval Alaluf, Daniel Cohen-Or.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2107.07437)] [[Github](https://github.com/OmerKafri/StyleFusion)]

**LowRankGAN: Low-Rank Subspaces in GANs.**<br> 
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2106.04488)] [[Github](https://github.com/zhujiapeng/LowRankGAN)]

**Discovering Interpretable Latent Space Directions of GANs Beyond Binary Attributes.**<br>
*Huiting Yang, Liangyu Chai, Qiang Wen, Shuang Zhao, Zixun Sun, Shengfeng He.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_Discovering_Interpretable_Latent_Space_Directions_of_GANs_Beyond_Binary_Attributes_CVPR_2021_paper.pdf)]

**Surrogate Gradient Field for Latent Space Manipulation.**<br>
*Minjun Li, Yanghua Jin, Huachun Zhu.*<br>
CVPR 2021. [[PDF](http://arxiv.org/abs/2104.09065)]

**L2M-GAN: Learning To Manipulate Latent Space Semantics for Facial Attribute Editing.**<br>
*Guoxing Yang, Nanyi Fei, Mingyu Ding, Guangzhen Liu, Zhiwu Lu, Tao Xiang.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_L2M-GAN_Learning_To_Manipulate_Latent_Space_Semantics_for_Facial_Attribute_CVPR_2021_paper.html)]

**MoCoGAN-HD: A Good Image Generator Is What You Need for High-Resolution Video Synthesis.**<br>
*Yu Tian, Jian Ren, Menglei Chai, Kyle Olszewski, Xi Peng, Dimitris N. Metaxas, Sergey Tulyakov.*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=6puCSjH3hwA)] [[Github](https://github.com/snap-research/MoCoGAN-HD)]

**A Latent Transformer for Disentangled and Identity-Preserving Face Editing.**<br>
*Xu Yao, Alasdair Newson, Yann Gousseau, Pierre Hellier.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2106.11895)] [[Github](https://github.com/InterDigitalInc/Latent-Transformer)]

**Do Not Escape From the Manifold: Discovering the Local Coordinates on the Latent Space of GANs.**<br>
*Jaewoong Choi, Changyeon Yoon, Junho Lee, Jung Ho Park, Geonho Hwang, Myungjoo Kang.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2106.06959)]

**GAN Steerability without optimization.**<br>
*Nurit Spingarn-Eliezer, Ron Banner, Tomer Michaeli.*<br>
ICLR 2021. [[OpenReview](https://openreview.net/forum?id=zDy_nQCXiIj)] [[PDF](https://arxiv.org/abs/2012.05328)]

**SeFa: Closed-Form Factorization of Latent Semantics in GANs.**<br>
*Yujun Shen, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2007.06600)] [[Github](https://github.com/genforce/sefa)] [[Project](https://genforce.github.io/sefa/)]

**Interpreting the Latent Space of GANs via Correlation Analysis for Controllable Concept Manipulation.**<br>
*Ziqiang Li, Rentuo Tao, Hongjing Niu, Bin Li.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2006.10132)]

**GANSpace: Discovering Interpretable GAN Controls.**<br>
*Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2004.02546)] [[Github](https://github.com/harskish/ganspace)]

**On the "steerability" of generative adversarial networks.**<br>
*Ali Jahanian, Lucy Chai, Phillip Isola.*<br>
ICLR 2020. [[PDF](https://arxiv.org/abs/1907.07171)] [[Project](https://ali-design.github.io/gan_steerability/)]

**Interpreting the Latent Space of GANs for Semantic Face Editing.**<br>
*[Yujun Shen](http://shenyujun.github.io/), [Jinjin Gu](http://www.jasongt.com/), [Xiaoou Tang](http://www.ie.cuhk.edu.hk/people/xotang.shtml), [Bolei Zhou](http://bzhou.ie.cuhk.edu.hk/).*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1907.10786)] [[Project](https://genforce.github.io/interfacegan/)] [[Github](https://github.com/genforce/interfacegan)]

**Seeing What a GAN Cannot Generate.**<br>
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1910.11626)] [[PDF](http://ganseeing.csail.mit.edu/)]

**Unsupervised Discovery of Interpretable Directions in the GAN Latent Space.**<br>
*Andrey Voynov, Artem Babenko.*<br>
ICML 2020. [[PDF](https://arxiv.org/abs/2002.03754)] [[Github](https://github.com/anvoynov/GANLatentDiscovery)]

## application

### content generation

**StyleCariGAN: Caricature Generation via StyleGAN Feature Map Modulation.**<br>
*Wongjong Jang, Gwangjin Ju, [Yucheol Jung](https://ycjung.info/), [Jiaolong Yang](http://jlyang.org/), [Xin Tong](https://www.microsoft.com/en-us/research/people/xtong/), [Seungyong Lee](http://phome.postech.ac.kr/~leesy/).*<br>
TOG 2021. [[PDF](https://arxiv.org/pdf/2107.04331.pdf)] [[Github](https://github.com/PeterZhouSZ/StyleCariGAN)]

**Coarse-to-Fine: Facial Structure Editing of Portrait Images via Latent Space Classifications.**<br>
*[Yiqian Wu](https://onethousandwu.com/), [Yongliang Yang](http://www.yongliangyang.net/), Qinjie Xiao, [Xiaogang Ji](http://www.cad.zju.edu.cn/home/jin).*<br>
TOG 2021. [[PDF](http://www.cad.zju.edu.cn/home/jin/sig2021/paper46.pdf)] [[Project](http://www.cad.zju.edu.cn/home/jin/sig2021/sig2021.htm)]

**One Shot Face Swapping on Megapixels.**<br>
*Yuhao Zhu, Qi Li, Jian Wang, Chengzhong Xu, Zhenan Sun.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2105.04932.pdf)] [[Github](https://github.com/zyainfal/One-Shot-Face-Swapping-on-Megapixels)]

**StyleMapGAN: Exploiting Spatial Dimensions of Latent in GAN for Real-time Image Editing.**<br>
*[Hyunsu Kim](https://github.com/blandocs), [Yunjey Choi](https://yunjey.github.io/), [Junho Kim](https://github.com/taki0112), [Sungjoo Yoo](http://cmalab.snu.ac.kr/), [Youngjung Uh](https://github.com/youngjung).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.14754)] [[Github](https://github.com/naver-ai/StyleMapGAN)]

**In&Out : Diverse Image Outpainting via GAN Inversion.**<br>
*Yen-Chi Cheng, Chieh Hubert Lin, Hsin-Ying Lee, Jian Ren, Sergey Tulyakov, Ming-Hsuan Yang.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2104.00675)] [[Github](https://yccyenchicheng.github.io/InOut/)]

**InfinityGAN: Towards Infinite-Resolution Image Synthesis.**<br>
*Chieh Hubert Lin, Hsin-Ying Lee, Yen-Chi Cheng, Sergey Tulyakov, Ming-Hsuan Yang.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2104.03963)] [[Project](https://hubert0527.github.io/infinityGAN/)]

**Paint by Word.**<br>
*David Bau, Alex Andonian, Audrey Cui, YeonHwan Park, Ali Jahanian, Aude Oliva, Antonio Torralba.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2103.10951)]

**Few-shot Semantic Image Synthesis Using StyleGAN Prior.**<br>
*Yuki Endo, Yoshihiro Kanamori.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2103.14877)] [[Github](https://github.com/endo-yuki-t/Fewshot-SMIS)]

**Unsupervised Image Transformation Learning via Generative Adversarial Networks.**<br>
*Kaiwen Zha, Yujun Shen, Bolei Zhou.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2103.07751)] [[Project](https://genforce.github.io/trgan)]

**TediGAN: Text-Guided Diverse Image Generation and Manipulation.**<br>
*Weihao Xia, Yujiu Yang, Jing-Hao Xue, Baoyuan Wu.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.03308)] [[Data](https://github.com/weihaox/Multi-Modal-CelebA-HQ)] [[Github](https://github.com/weihaox/TediGAN)]

**LOHO: Latent Optimization of Hairstyles via Orthogonalization.**<br>
*Rohit Saha, Brendan Duke, Florian Shkurti, Graham W. Taylor, Parham Aarabi.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2103.03891)] [[Github](https://github.com/dukebw/LOHO)]

**SAM: Only a Matter of Style-Age Transformation Using a Style-Based Regression Model.**<br>
*Yuval Alaluf, Or Patashnik, [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2102.02754)] [[Github](https://github.com/yuval-alaluf/SAM)]

**Exploring Adversarial Fake Images on Face Manifold.**<br>
*Dongze Li, Wei Wang, Hongxing Fan, Jing Dong.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2101.03272)]

**Generating Images from Caption and Vice Versa via CLIP-Guided Generative Latent Space Search.**<br>
*Federico A. Galatolo, Mario G.C.A. Cimino, Gigliola Vaglini.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2102.01645)]

**Unsupervised Image-to-Image Translation via Pre-trained StyleGAN2 Network.**<br>
*Jialu Huang, Jing Liao, Sam Kwong.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2010.05713)]

**DeepI2I: Enabling Deep Hierarchical Image-to-Image Translation by Transferring from GANs.**<br>
*yaxing wang, Lu Yu, Joost van de Weijer.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2011.05867)] [[Github](https://github.com/yaxingwang/DeepI2I)]

**DeepLandscape: Adversarial Modeling of Landscape Videos.**<br>
*E. Logacheva, R. Suvorov, O. Khomenko, A. Mashikhin, and V. Lempitsky.*<br>
ECCV 2020. [[PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123680256.pdf)] [[Github](https://github.com/saic-mdal/deep-landscape)] [[Project](https://saic-mdal.github.io/deep-landscape/)]

### image restoration

**GLEAN: Generative Latent Bank for Large-Factor Image Super-Resolution.**<br>
*[Kelvin C.K. Chan](https://ckkelvinchan.github.io/), Xintao Wang, Xiangyu Xu, Jinwei Gu, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.00739)] [[Project](https://ckkelvinchan.github.io/projects/GLEAN)] [[Github](https://github.com/ckkelvinchan/GLEAN)]

**GFP-GAN: Towards Real-World Blind Face Restoration with Generative Facial Prior.**<br>
*[Xintao Wang](https://xinntao.github.io/), [Yu Li](https://yu-li.github.io/), [Honglun Zhang](https://scholar.google.com/citations?hl=en&user=KjQLROoAAAAJ), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en).*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2101.04061)] [[Project](https://xinntao.github.io/)]

**Style Generator Inversion for Image Enhancement and Animation.**<br>
*[Aviv Gabbay](http://www.cs.huji.ac.il/~avivga), [Yedid Hoshen](http://www.cs.huji.ac.il/~ydidh).*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/1906.11880)] [[Project](http://www.vision.huji.ac.il/style-image-prior/)] [[Github](https://github.com/avivga/style-image-prior)]

### image understanding

**DatasetGAN: Efficient Labeled Data Factory with Minimal Human Effort.**<br>
*[Yuxuan Zhang](https://www.alexyuxuanzhang.com/), [Huan Ling](http://www.cs.toronto.edu/~linghuan/), [Jun Gao](http://www.cs.toronto.edu/~jungao/), [Kangxue Yin](https://kangxue.org/), [Jean-Francois Lafleche](), [Adela Barriuso](), [Antonio Torralba](https://groups.csail.mit.edu/vision/torralbalab/), [Sanja Fidler](http://www.cs.utoronto.ca/~fidler/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.06490)] [[Github](https://github.com/nv-tlabs/datasetGAN_release)] [[Project](https://nv-tlabs.github.io/datasetGAN/)]

**Repurposing GANs for One-shot Semantic Part Segmentation.**<br>
*Nontawat Tritrong, Pitchaporn Rewatbowornwong, [Supasorn Suwajanakorn](https://www.supasorn.com/).*<br>
CVPR 2021 (oral). [[PDF](https://arxiv.org/abs/2103.04379)] [[Project](https://repurposegans.github.io/)] [[Github](https://github.com/bryandlee/repurpose-gan)]

**Labels4Free: Unsupervised Segmentation using StyleGAN.**<br>
*[Rameen Abdal](https://scholar.google.com/citations?user=kEQimk0AAAAJ&hl=en), [Peihao Zhu](https://scholar.google.com/citations?user=Gn8URq0AAAAJ&hl=en), [Niloy Mitra](http://www0.cs.ucl.ac.uk/staff/n.mitra/), [Peter Wonka](http://peterwonka.net/).*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2103.14968)] [[Project](https://rameenabdal.github.io/Labels4Free)] [[Github](https://github.com/RameenAbdal/Labels4Free)]

**Segmentation in Style: Unsupervised Semantic Image Segmentation with Stylegan and CLIP.**<br>
*Daniil Pakhomov, Sanchit Hira, Narayani Wagle, Kemar E. Green, Nassir Navab.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2107.12518.pdf)] [[Github](https://github.com/warmspringwinds/segmentation_in_style)]

### compressed sensing

**Generator Surgery for Compressed Sensing.**<br>
*Niklas Smedemark-Margulies, Jung Yeon Park, Max Daniels, Rose Yu, Jan-Willem van de Meent, Paul Hand.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2102.11163)] [[Github](https://github.com/nik-sm/generator-surgery)]

**Task-Aware Compressed Sensing with Generative Adversarial Networks.**<br>
*Maya Kabkab, Pouya Samangouei, Rama Chellappa.*<br>
AAAI 2018. [[PDF](https://arxiv.org/pdf/1802.01284.pdf)]

### 3D

**OSTeC: One-Shot Texture Completion.**<br>
*Baris Gecer, Jiankang Deng, Stefanos Zafeiriou.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2012.15370)] [[Github](https://github.com/barisgecer/OSTeC)]

**GAN2Shape: Do 2D GANs Know 3D Shape? Unsupervised 3D shape reconstruction from 2D Image GANs.**<br>
*[Xingang Pan](https://xingangpan.github.io/), Bo Dai, Ziwei Liu, Chen Change Loy, Ping Luo.*<br>
ICLR 2021 (oral). [[PDF](https://arxiv.org/abs/2011.00844)] [[Github](https://github.com/XingangPan/GAN2Shape)] [[Project](https://xingangpan.github.io/projects/GAN2Shape.html)]

**Unsupervised 3D Shape Completion through GAN-Inversion.**<br>
*Junzhe Zhang, Xinyi Chen, Zhongang Cai, Liang Pan, Haiyu Zhao, Shuai Yi, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2104.13366)] [[Project](https://junzhezhang.github.io/projects/ShapeInversion/)]

## acknowledgement

Thanks for the feedback from [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Andrey Voynov](https://github.com/anvoynov), and [Rushil Anirudh](https://rushila.com/).
