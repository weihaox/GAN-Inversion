# <p align=center>`awesome gan-inversion papers`</p>
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 

A collection of resources on GAN Inversion: Interpreting the Latent Space of Pretrained Models. 

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

```bibtex
@article{xia2021survey,
  author    = {Xia, Weihao and Zhang, Yulun and Yang, Yujiu and Xue, Jing-Hao and Zhou, Bolei and Yang, Ming-Hsuan},
  title     = {GAN Inversion: A Survey},
  journal={arXiv preprint arXiv: 2101.05278},
  year={2021}
}
```

## inverted pretrained model

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

**A Style-Based Generator Architecture for Generative Adversarial Networks.**<br>
*Tero Karras, Samuli Laine, Timo Aila.*<br>
CVPR 2019. [[PDF](https://arxiv.org/abs/1812.04948)] [[Offical TF](https://github.com/NVlabs/stylegan)]

**Progressive Growing of GANs for Improved Quality, Stability, and Variation.**<br>
*Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen.*<br>
ICLR 2018. [[PDF](https://arxiv.org/abs/1710.10196)] [[Offical TF](https://github.com/tkarras/progressive_growing_of_gans)]

## inversion method

This part contatins generatal inversion methods, while methods in the next *application* part are mainly designed for specific tasks.

**Using Latent Space Regression to Analyze and Leverage Compositionality in GANs.**<br> 
*Lucy Chai, Jonas Wulff, Phillip Isola.*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=sjuuTm4vj0)]

**Hijack-GAN: Unintended-Use of Pretrained, Black-Box GANs.**<br>
*Hui-Po Wang, Ning Yu, Mario Fritz.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.14107)]

**e4e: Designing an Encoder for StyleGAN Image Manipulation.**<br>
*[Omer Tov](https://yotamnitzan.github.io/), Yuval Alaluf, Yotam Nitzan, Or Patashnik, Daniel Cohen-Or.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2102.02766)] [[Github](https://github.com/omertov/encoder4editing)]

**Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation.**<br>
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing.*<br>
ICLR 2021. [[PDF](https://arxiv.org/abs/2102.01187)]

**Improved StyleGAN Embedding: Where are the Good Latents?**<br>
*Peihao Zhu, Rameen Abdal, Yipeng Qin, Peter Wonka.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2012.09036)]

**Learning a Deep Reinforcement Learning Policy Over the Latent Space of a Pre-trained GAN for Semantic Age Manipulation.**<br>
*Kumar Shubham, Gopalakrishnan Venkatesh, Reijul Sachdev, Akshi, Dinesh Babu Jayagopi, G. Srinivasaraghavan.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.00954)]

**Lifting 2D StyleGAN for 3D-Aware Face Generation.**<br>
*[Yichun Shi](https://seasonsh.github.io/), Divyansh Aggarwal, [Anil K. Jain](http://www.cse.msu.edu/~jain/).*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.13126)]

**Navigating the GAN Parameter Space for Semantic Image Editing.**<br>
*Anton Cherepkov, Andrey Voynov, Artem Babenko.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.13786)] [[Github](https://github.com/yandex-research/navigan)]

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
arxiv 2020. [[PDF]](https://arxiv.org/abs/2011.12799)

**GAN Steerability without optimization.**<br>
*Nurit Spingarn-Eliezer, Ron Banner, Tomer Michaeli.*<br>
ICLR 2021. [[OpenReview](https://openreview.net/forum?id=zDy_nQCXiIj)] [[PDF](https://arxiv.org/abs/2012.05328)]

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

**SeFa: Closed-Form Factorization of Latent Semantics in GANs.**<br>
*Yujun Shen, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2007.06600)] [[Github](https://github.com/genforce/sefa)] [[Project](https://genforce.github.io/sefa/)]

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

**Interpreting the Latent Space of GANs via Correlation Analysis for Controllable Concept Manipulation.**<br>
*Ziqiang Li, Rentuo Tao, Hongjing Niu, Bin Li.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2006.10132)]

**GANSpace: Discovering Interpretable GAN Controls.**<br>
*Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2004.02546)] [[Github](https://github.com/harskish/ganspace)]

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

**On the "steerability" of generative adversarial networks.**<br>
*Ali Jahanian, Lucy Chai, Phillip Isola.*<br>
ICLR 2020. [[PDF](https://arxiv.org/abs/1907.07171)] [[Project](https://ali-design.github.io/gan_steerability/)]

**Unsupervised Discovery of Interpretable Directions in the GAN Latent Space.**<br>
*Andrey Voynov, Artem Babenko.*<br>
ICML 2020. [[PDF](https://arxiv.org/abs/2002.03754)] [[Github](https://github.com/anvoynov/GANLatentDiscovery)]

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

**Interpreting the Latent Space of GANs for Semantic Face Editing.**<br>
*[Yujun Shen](http://shenyujun.github.io/), [Jinjin Gu](http://www.jasongt.com/), [Xiaoou Tang](http://www.ie.cuhk.edu.hk/people/xotang.shtml), [Bolei Zhou](http://bzhou.ie.cuhk.edu.hk/).*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1907.10786)] [[Project](https://genforce.github.io/interfacegan/)] [[Github](https://github.com/genforce/interfacegan)]

**Image2StyleGAN++: How to Edit the Embedded Images?**<br>
*Rameen Abdal, Yipeng Qin, Peter Wonka.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1911.11544)]

**Semantic Photo Manipulation with a Generative Image Prior.**<br>
*David Bau, Hendrik Strobelt, William Peebles, Jonas, Bolei Zhou, Jun-Yan Zhu, Antonio Torralba.*<br>
SIGGRAPH 2019. [[PDF](https://arxiv.org/abs/2005.07727)]

**Image2StyleGAN: How to Embed Images Into the StyleGAN Latent Space?**<br>
*Rameen Abdal, Yipeng Qin, Peter Wonka.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1904.03189)]

**Seeing What a GAN Cannot Generate.**<br>
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1910.11626)] [[PDF](http://ganseeing.csail.mit.edu/)]

**GAN-based Projector for Faster Recovery with Convergence Guarantees in Linear Inverse Problems.**<br>
*Ankit Raj, Yuqi Li, Yoram Bresler.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1902.09698)]

**Inverting Layers of a Large Generator.**<br>
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba.*<br>
ICCV 2019. [[PDF](https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_18.pdf)]

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

**Inverting The Generator Of A Generative Adversarial Network.**<br>
*Antonia Creswell, Anil Anthony Bharath.*<br>
NIPSW 2016. [[PDF](https://arxiv.org/abs/1611.05644)]

**Generative Visual Manipulation on the Natural Image Manifold.**<br>
*Jun-Yan Zhu, Philipp Krähenbühl, Eli Shechtman, Alexei A. Efros.*<br>
ECCV 2016. [[PDF](https://arxiv.org/abs/1609.03552v2)]

## application

### content generation

**TediGAN: Text-Guided Diverse Image Generation and Manipulation.**<br>
*Weihao Xia, Yujiu Yang, Jing-Hao Xue, Baoyuan Wu.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.03308)] [[Data](https://github.com/weihaox/Multi-Modal-CelebA-HQ)] [[Github](https://github.com/weihaox/TediGAN)]

**LOHO: Latent Optimization of Hairstyles via Orthogonalization.**<br>
*Rohit Saha, Brendan Duke, Florian Shkurti, Graham W. Taylor, Parham Aarabi.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2103.03891)] [[Github](https://github.com/dukebw/LOHO)]

**SAM: Only a Matter of Style-Age Transformation Using a Style-Based Regression Model.**<br>
*Yuval Alaluf, Or Patashnik, [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2102.02754)] [[Github](https://github.com/yuval-alaluf/SAM)]

**OSTeC: One-Shot Texture Completion.**<br>
*Baris Gecer, Jiankang Deng, Stefanos Zafeiriou.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2012.15370)] [[Github](https://github.com/barisgecer/OSTeC)]

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

### compressed sensing

**Generator Surgery for Compressed Sensing.**<br>
*Niklas Smedemark-Margulies, Jung Yeon Park, Max Daniels, Rose Yu, Jan-Willem van de Meent, Paul Hand.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2102.11163)] [[Github](https://github.com/nik-sm/generator-surgery)]

**Task-Aware Compressed Sensing with Generative Adversarial Networks.**<br>
*Maya Kabkab, Pouya Samangouei, Rama Chellappa.*<br>
AAAI 2018. [[PDF](https://arxiv.org/pdf/1802.01284.pdf)]

## acknowledgement

Thanks for the feedback from [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Andrey Voynov](https://github.com/anvoynov), and [Rushil Anirudh](https://rushila.com/).