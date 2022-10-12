 <!-- # <p align=center>`awesome gan-inversion`</p> -->
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com) 
![visitors](https://visitor-badge.glitch.me/badge?style=flat-square&page_id=weihaox/awesome-gan-inversion) 

<br />
<p align="center">
  <h1 align="center">GAN Inversion: A Survey</h1>
  <p align="center">
    TPAMI, 2022
    <br />
    <a href="https://xiaweihao.com/"><strong>Weihao Xia</strong></a>
    ·
    <a href="https://yulunzhang.com/"><strong>Yulun Zhang</strong></a>
    ·
    <a href="https://sites.google.com/view/iigroup-thu/about"><strong>Yujiu Yang</strong></a>
    ·
    <a href="http://www.homepages.ucl.ac.uk/~ucakjxu/"><strong>Jing-Hao Xue</strong></a>
    ·
    <a href="https://boleizhou.github.io/"><strong>Bolei Zhou</strong></a>
    ·
    <a href="https://faculty.ucmerced.edu/mhyang/"><strong>Ming-Hsuan Yang</strong></a>
  </p>

  <p align="center">
    <a href='https://arxiv.org/abs/2101.05278'>
      <img src='https://img.shields.io/badge/Paper-PDF-green?style=flat&logo=arXiv&logoColor=green' alt='arXiv PDF'>
    </a>
    <a href='https://github.com/weihaox/awesome-gan-inversion' style='padding-left: 0.5rem;'>
      <img src='https://img.shields.io/badge/Project-Page-blue?style=flat&logo=Google%20chrome&logoColor=blue' alt='Project Page'>
    </a>
    <a href='https://ieeexplore.ieee.org/document/9792208' style='padding-left: 0.5rem;'>
      <img src='https://img.shields.io/badge/TPAMI-PDF-red?style=flat&logoColor=red' alt='TPAMI PDF'>
    </a>
  </p>
</p>
<br />

This repo is a collection of resources on GAN inversion, as a supplement for our [survey](https://arxiv.org/abs/2101.05278).  If you find any work missing or have any suggestions (papers, implementations and other resources), feel free to [pull requests](https://github.com/weihaox/awesome-gan-inversion/pulls).

<details style="margin-left:3%;">
  <summary>citation</summary>
  <pre><code class="language-bib" style="font-size: 0.9rem;" id="citation">@article{xia2022gan,
    author  = {Xia, Weihao and Zhang, Yulun and Yang, Yujiu and Xue, Jing-Hao and Zhou, Bolei and Yang, Ming-Hsuan},
    title   = {GAN Inversion: A Survey},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
    year={2022}
  }
</code></pre>
</details> 

<details><summary>Table of Contents</summary><p>

- [inverted pretrained model](#inverted-pretrained-model)
- [inversion method](#inversion-method)
- [latent space navigation](#latent-space-navigation)
- [application](#application)
- [acknowledgement](#acknowledgement)

</p></details><p></p>

## inverted pretrained model

### 2D GANs

**StyleGAN-XL: Scaling StyleGAN to Large Diverse Datasets.**<br>
*[Axel Sauer](https://axelsauer.com/), [Katja Schwarz](https://katjaschwarz.github.io/), [Andreas Geiger](http://www.cvlibs.net/).*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2202.00273)] [[Project](https://sites.google.com/view/stylegan-xl/)] [[Github](https://github.com/autonomousvision/stylegan_xl)]

**Self-Distilled StyleGAN: Towards Generation from Internet Photos.**<br>
*[Ron Mokady](https://rmokady.github.io/), Michal Yarom, Omer Tov, Oran Lang, Daniel Cohen-Or, Tali Dekel, Michal Irani, Inbar Mosseri.*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2202.12211)] [[Project](https://self-distilled-stylegan.github.io/)] [[Github](https://github.com/self-distilled-stylegan/self-distilled-internet-photos)]

**Ensembling Off-the-shelf Models for GAN Training.**<br>
[Nupur Kumari](https://nupurkmr9.github.io/), [Richard Zhang](https://richzhang.github.io/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/)<br>
CVPR 2022. [[PDF](https://arxiv.org/pdf/2112.09130.pdf)] [[Project](https://www.cs.cmu.edu/~vision-aided-gan/)] [[Github](https://github.com/nupurkmr9/vision-aided-gan)]

**StyleGAN3: Alias-Free Generative Adversarial Networks.**<br>
*Tero Karras, Miika Aittala, Samuli Laine, Erik Härkönen, Janne Hellsten, Jaakko Lehtinen, Timo Aila.*<br>
NeurIPS 2021. [[PDF](https://arxiv.org/abs/2106.12423)] [[Project](https://nvlabs.github.io/alias-free-gan)] [[Github](https://github.com/NVlabs/stylegan3)] [[Rosinality](https://github.com/rosinality/alias-free-gan-pytorch)]

**StyleGAN2-Ada: Training Generative Adversarial Networks with Limited Data.**<br>
*Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, Timo Aila.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2006.06676)] [[Github](https://github.com/NVlabs/stylegan2-ada)] [[Steam StyleGAN2-ADA](https://github.com/woctezuma/steam-stylegan2-ada)]

**StyleGAN2: Analyzing and Improving the Image Quality of StyleGAN.**<br>
*[Tero Karras](https://research.nvidia.com/person/tero-karras), [Samuli Laine](https://research.nvidia.com/person/samuli-laine), [Miika Aittala](https://research.nvidia.com/person/miika-aittala), Janne Hellsten, Jaakko Lehtinen, [Timo Aila](https://research.nvidia.com/person/timo-aila).*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1912.04958)] [[PyTorch](https://github.com/rosinality/stylegan2-pytorch)] [[Offical TF](https://github.com/NVlabs/stylegan2)]  [[Unoffical Tensorflow 2.0](https://github.com/manicman1999/StyleGAN2-Tensorflow-2.0)]

**StyleGAN: A Style-Based Generator Architecture for Generative Adversarial Networks.**<br>
*Tero Karras, Samuli Laine, Timo Aila.*<br>
CVPR 2019. [[PDF](https://arxiv.org/abs/1812.04948)] [[Offical TF](https://github.com/NVlabs/stylegan)]

**ProGAN: Progressive Growing of GANs for Improved Quality, Stability, and Variation.**<br>
*Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen.*<br>
ICLR 2018. [[PDF](https://arxiv.org/abs/1710.10196)] [[Offical TF](https://github.com/tkarras/progressive_growing_of_gans)]

### 3D-aware GANs

**EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks.**<br>
*[Eric R. Chan](https://ericryanchan.github.io/), [Connor Z. Lin](https://connorzlin.com/), [Matthew A. Chan](https://matthew-a-chan.github.io/), [Koki Nagano](https://luminohope.org/), [Boxiao Pan](https://cs.stanford.edu/~bxpan/), [Shalini De Mello](https://research.nvidia.com/person/shalini-gupta), [Orazio Gallo](https://oraziogallo.github.io/), [Leonidas Guibas](https://geometry.stanford.edu/member/guibas/), [Jonathan Tremblay](https://research.nvidia.com/person/jonathan-tremblay), [Sameh Khamis](https://www.samehkhamis.com/), [Tero Karras](https://research.nvidia.com/person/tero-karras), [Gordon Wetzstein](https://stanford.edu/~gordonwz/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.07945)] [[Project](https://matthew-a-chan.github.io/EG3D)] [[Github](https://github.com/NVlabs/eg3d)]

**StyleNeRF: A Style-based 3D-Aware Generator for High-resolution Image Synthesis.**<br>
*[Jiatao Gu](http://jiataogu.me/), [Lingjie Liu](https://lingjie0206.github.io/), [Peng Wang](https://totoro97.github.io/about.html), [Christian Theobalt](http://people.mpi-inf.mpg.de/~theobalt/).*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2110.08985)] [[Project](http://jiataogu.me/style_nerf/)]

**StyleSDF: High-Resolution 3D-Consistent Image and Geometry Generation.**<br>
*[Roy Or-El](https://homes.cs.washington.edu/~royorel/), [Xuan Luo](https://roxanneluo.github.io/), Mengyi Shan, Eli Shechtman, Jeong Joon Park, Ira Kemelmacher-Shlizerman.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.11427)] [[Project](https://stylesdf.github.io/)] [[Github](https://github.com/royorel/StyleSDF)]

**pi-GAN: Periodic Implicit Generative Adversarial Networks for 3D-Aware Image Synthesis.**<br>
*[Eric R. Chan](https://ericryanchan.github.io/), [Marco Monteiro](https://marcoamonteiro.github.io/pi-GAN-website/), [Petr Kellnhofer](https://kellnhofer.xyz/), [Jiajun Wu](https://jiajunwu.com/), [Gordon Wetzstein](https://stanford.edu/~gordonwz/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.00926)] [[Project](https://marcoamonteiro.github.io/pi-GAN-website/)] [[Github](https://github.com/lucidrains/pi-GAN-pytorch)]

## inversion method

This part contatins generatal inversion methods, while methods in the next *application* part are mainly designed for specific tasks.

### 2D GAN inversion

**IntereStyle: Encoding an Interest Region for Robust StyleGAN Inversion.**<br>
*Seungjun Moon, GyeongMoon Park.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2209.10811)] 

**High-fidelity GAN Inversion with Padding Space.**<br>
*[Qingyan Bai](https://ezioby.github.io/padinv/), Yinghao Xu, Jiapeng Zhu, Weihao Xia, Yujiu Yang, Yujun Shen.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2203.11105)] [[Project](https://github.com/EzioBy/padinv)] [[Github](https://github.com/EzioBy/padinv)]

**Chunkmogrify: Real image inversion via Segments.**<br>
*[David Futschik](https://dcgi.fel.cvut.cz/people/futscdav), [Michal Lukáč](https://research.adobe.com/person/michal-lukac/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Daniel Sýkora](https://dcgi.fel.cvut.cz/home/sykorad/).*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2110.06269)] [[Github](https://github.com/futscdav/Chunkmogrify)]

**Feature-Style Encoder for Style-Based GAN Inversion.**<br>
*Xu Yao, Alasdair Newson, Yann Gousseau, Pierre Hellier.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2202.02183)] [[Github](https://github.com/InterDigitalInc/FeatureStyleEncoder)]

**Third Time's the Charm? Image and Video Editing with StyleGAN3.**<br>
*Yuval Alaluf, Or Patashnik, Zongze Wu, Asif Zamir, Eli Shechtman, Dani Lischinski, Daniel Cohen-Or.*<br>
Advances in Image Manipulation Workshop, ECCV 2022. [[PDF](https://arxiv.org/abs/2201.13433)] [[Project](https://yuval-alaluf.github.io/stylegan3-editing/)] [[Github](https://github.com/yuval-alaluf/stylegan3-editing)]

**Cycle Encoding of a StyleGAN Encoder for Improved Reconstruction and Editability.**<br>
*Xudong Mao, Liujuan Cao, Aurele Tohokantche Gnanha, Zhenguo Yang, Qing Li, Rongrong Ji.*<br>
ACM MM 2022. [[PDF](https://arxiv.org/abs/2207.09367)] [[Github](https://github.com/xudonmao/CycleEncoding)]

**Spatially-Adaptive Multilayer Selection for GAN Inversion and Editing.**<br>
*[Gaurav Parmar](https://gauravparmar.com/), [Yijun Li](https://yijunmaverick.github.io/), [Jingwan Lu](https://research.adobe.com/person/jingwan-lu/), [Richard Zhang](http://richzhang.github.io/), [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Krishna Kumar Singh](http://krsingh.cs.ucdavis.edu/).*<br>
CVPR 2022. [[PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Parmar_Spatially-Adaptive_Multilayer_Selection_for_GAN_Inversion_and_Editing_CVPR_2022_paper.pdf)] [[Project](https://www.cs.cmu.edu/~SAMInversion)] [[Github](https://github.com/adobe-research/sam_inversion)]

**Style Transformer for Image Inversion and Editing.**<br>
*Xueqi Hu, Qiusheng Huang, Zhengyi Shi, Siyuan Li, Changxin Gao, Li Sun, Qingli Li.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.07932)] [[Github](https://github.com/sapphire497/style-transformer)]

**High-Fidelity GAN Inversion for Image Attribute Editing.**<br>
*[Tengfei Wang](https://tengfei-wang.github.io), Yong Zhang, Yanbo Fan, Jue Wang, Qifeng Chen.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2109.06590)] [[Project](https://tengfei-wang.github.io/HFGI/)] [[Github](https://github.com/Tengfei-Wang/HFGI)]

**HyperInverter: Improving StyleGAN Inversion via Hypernetwork.**<br>
*[Tan M. Dinh](https://di-mi-ta.github.io/), [Anh Tuan Tran](https://sites.google.com/site/anhttranusc/), [Rang Nguyen](https://sites.google.com/site/rangmanhonguyen/), [Binh-Son Hua](https://sonhua.github.io/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.00719)] [[Project](https://di-mi-ta.github.io/HyperInverter/)]

**HyperStyle: StyleGAN Inversion with HyperNetworks for Real Image Editing.**<br>
*Yuval Alaluf, Omer Tov, Ron Mokady, Rinon Gal, Amit H. Bermano.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2111.15666)] [[Project](http://yuval-alaluf.github.io/hyperstyle/)] [[Github](https://github.com/yuval-alaluf/hyperstyle)]

**Overparameterization Improves StyleGAN Inversion.**<br>
*Yohan Poirier-Ginter, Alexandre Lessard, Ryan Smith, Jean-François Lalonde.*<br>
CVPR 2022 Workshop on AI for Content Creation. [[PDF](https://arxiv.org/abs/2205.06304)] [[Github](https://lvsn.github.io/OverparamStyleGAN/)]

**StyleAlign: Analysis and Applications of Aligned StyleGAN Models.**<br>
*Zongze Wu, Yotam Nitzan, Eli Shechtman, Dani Lischinski.*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2110.11323)]

**Semantic Unfolding of StyleGAN Latent Space.**<br>
*Mustafa Shukor, Xu Yao, Bharath Bushan Damodaran, Pierre Hellier.*<br>
ICIP 2022. [[PDF](https://arxiv.org/abs/2206.14892)]

**LSAP: Rethinking Inversion Fidelity, Perception and Editability in GAN Latent Space.**<br>
*Cao Pu, Lu Yang, Dongxv Liu, Zhiwei Liu, Wenguan Wang, Shan Li, Qing Song.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2209.12746)]

**Near Perfect GAN Inversion.**<br>
*Qianli Feng, Viraj Shah, Raghudeep Gadde, Pietro Perona, Aleix Martinez.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2202.11833)]

**Video2StyleGAN: Encoding Video in Latent Space for Manipulation.**<br>
*Jiyang Yu, Jingen Liu, Jing Huang, Wei Zhang, Tao Mei.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2206.13078)]

**Editing Out-of-domain GAN Inversion via Differential Activations.**<br>
*Haorui Song, Yong Du, Tianyi Xiang, Junyu Dong, Jing Qin, Shengfeng He*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2207.08134)] [[Github](https://github.com/HaoruiSong622/Editing-Out-of-Domain)]

**Expanding the Latent Space of StyleGAN for Real Face Editing.**<br>
*Yin Yu, Ghasedi Kamran, Wu HsiangTao, Yang Jiaolong, Tong Xi, Fu Yun.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2204.12530)]

**Encode-in-Style: Latent-based Video Encoding using StyleGAN2.**<br>
*[Trevine Oorloff](https://trevineoorloff.github.io/), [Yaser Yacoob](https://www.umiacs.umd.edu/people/yaser).*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2203.14512)] [[Project](https://trevineoorloff.github.io/Encode-in-Style.io/)] [[Github](https://github.com/trevineoorloff/Encode-in-Style)] [[Data](https://trevineoorloff.github.io/Encode-in-Style.io/)]

**Solving Inverse Problems with NerfGANs.**<br>
*Giannis Daras, Wen-Sheng Chu, Abhishek Kumar, Dmitry Lagun, Alexandros G. Dimakis.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2112.09061)]

**StyleGAN of All Trades: Image Manipulation with Only Pretrained StyleGAN.**<br>
*Min Jin Chong, Hsin-Ying Lee, David Forsyth.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2111.01619)] [[Github](https://github.com/mchong6/SOAT)]

**Semantic and Geometric Unfolding of StyleGAN Latent Space.**<br>
*Mustafa Shukor, Xu Yao, Bharath Bhushan Damodaran, Pierre Hellier.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2107.04481)]

**Pivotal Tuning for Latent-based Editing of Real Images.**<br>
*Daniel Roich, Ron Mokady, Amit H. Bermano, Daniel Cohen-Or.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2106.05744.pdf)] [[Github](https://github.com/danielroich/PTI)]

**Transforming the Latent Space of StyleGAN for Real Face Editing.**<br> 
*Heyi Li, Jinlong Liu, Yunzhi Bai, Huayan Wang, Klaus Mueller.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2105.14230)] [[Github](https://github.com/AnonSubm2021/TransStyleGAN)]

**E2Style: Improve the Efficiency and Effectiveness of StyleGAN Inversion.**<br> 
*Tianyi Wei, Dongdong Chen, Wenbo Zhou, Jing Liao, Weiming Zhang, Lu Yuan, Gang Hua, Nenghai Yu.*<br> 
TIP 2022. [[PDF](https://arxiv.org/abs/2104.07661)] [[Project](https://wty-ustc.github.io/inversion/)] [[Github](https://github.com/wty-ustc/StyleGAN-Inversion-Baseline)] 

**GAN-Control: Explicitly Controllable GANs.**<br>
*Alon Shoshan, Nadav Bhonker, Igor Kviatkovsky, Gerard Medioni.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2101.02477)]

**Improved StyleGAN Embedding: Where are the Good Latents?**<br>
*[Peihao Zhu](https://github.com/ZPdesu), [Rameen Abdal](https://github.com/RameenAbdal), [Yipeng Qin](https://scholar.google.com/citations?user=ojgWPpgAAAAJ&hl=en), [John Femiani](https://scholar.google.com/citations?user=rS1xJIIAAAAJ&hl=en), [Peter Wonka](http://peterwonka.net/).*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2012.09036)] [[Github](https://github.com/ZPdesu/II2S)]

**Learning a Deep Reinforcement Learning Policy Over the Latent Space of a Pre-trained GAN for Semantic Age Manipulation.**<br>
*Kumar Shubham, Gopalakrishnan Venkatesh, Reijul Sachdev, Akshi, Dinesh Babu Jayagopi, G. Srinivasaraghavan.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.00954)]

**Augmentation-Interpolative AutoEncoders for Unsupervised Few-Shot Image Generation.**<br>
*Davis Wertheimer, Omid Poursaeed, Bharath Hariharan.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2011.13026)]

**Unsupervised Discovery of Disentangled Manifolds in GANs.**<br>
*Yu-Ding Lu, Hsin-Ying Lee, Hung-Yu Tseng, Ming-Hsuan Yang.*<br>
arxiv 2020. [[PDF]](https://arxiv.org/abs/2011.11842)]

**Collaborative Learning for Faster StyleGAN Embedding.**<br>
*Shanyan Guan, [Ying Tai](https://tyshiwo.github.io/), Bingbing Ni, Feida Zhu, Feiyue Huang, Xiaokang Yang.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2007.01758)]

**Improving Inversion and Generation Diversity in StyleGAN using a Gaussianized Latent Space.**<br>
*[Jonas Wulff](http://people.csail.mit.edu/jwulff/), Antonio Torralba.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2009.06529)]

**From Continuity to Editability: Inverting GANs with Consecutive Images.**<br>
*[Yangyang Xu](https://qingyang-xu.github.io/), [Yong Du](https://www.csyongdu.com/), Wenpeng Xiao, Xuemiao Xu and [Shengfeng He](hengfenghe.com).*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2107.13812)] [[Github](https://github.com/Qingyang-Xu/InvertingGANs_with_ConsecutiveImgs)]

**Explaining in Style: Training a GAN to explain a classifier in StyleSpace.**<br> 
*Oran Lang, Yossi Gandelsman, Michal Yarom, Yoav Wald, Gal Elidan, Avinatan Hassidim, William T. Freeman, Phillip Isola, Amir Globerson, Michal Irani, Inbar Mosseri.*<br> 
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.13369)] [[Project](https://explaining-in-style.github.io/)]

**BDInvert: GAN Inversion for Out-of-Range Images with Geometric Transformations.**<br>
*[Kyoungkook Kang](https://kkang831.github.io/), Seongtae Kim, [Sunghyun Cho](https://www.scho.pe.kr/).*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2108.08998)] [[Project](https://kkang831.github.io/publication/ICCV_2021_BDInvert/)]

**ReStyle: A Residual-Based StyleGAN Encoder via Iterative Refinement.**<br> 
*[Yuval Alaluf](https://yuval-alaluf.github.io/), [Or Patashnik](https://orpatashnik.github.io/), [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br> 
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.02699)] [[Project](https://yuval-alaluf.github.io/restyle-encoder/)] [[Github](https://github.com/yuval-alaluf/restyle-encoder)]

**LatentCLR: A Contrastive Learning Approach for Unsupervised Discovery of Interpretable Directions.**<br> 
*Oğuz Kaan Yüksel, [Enis Simsar](https://enis.dev), Ezgi Gülperi Er, Pinar Yanardag.*<br> 
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.00820)] [[Github](https://github.com/catlab-team/latentclr)]

**Lifting 2D StyleGAN for 3D-Aware Face Generation.**<br>
*[Yichun Shi](https://seasonsh.github.io/), Divyansh Aggarwal, [Anil K. Jain](http://www.cse.msu.edu/~jain/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.13126)]

**Ensembling with Deep Generative Views.**<br> 
*Lucy Chai, Jun-Yan Zhu, Eli Shechtman, Phillip Isola, Richard Zhang.*<br> 
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.14551)] [[Github](https://github.com/chail/gan-ensembling)] [[Project](https://chail.github.io/gan-ensembling/)]

**Navigating the GAN Parameter Space for Semantic Image Editing.**<br>
*Anton Cherepkov, Andrey Voynov, Artem Babenko.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.13786)] [[Github](https://github.com/yandex-research/navigan)]

**StyleSpace Analysis: Disentangled Controls for StyleGAN Image Generation.**<br>
*Zongze Wu, Dani Lischinski, Eli Shechtman.*<br>
CVPR 2021 (oral). [[PDF]](https://arxiv.org/abs/2011.12799) [[Github](https://github.com/betterze/StyleSpace)]

**Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation.**<br>
*Elad Richardson, Yuval Alaluf, Or Patashnik, Yotam Nitzan, Yaniv Azar, Stav Shapiro, Daniel Cohen-Or.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2008.00951)] [[Github](https://github.com/eladrich/pixel2style2pixel)] [[Project](eladrich.github.io/pixel2style2pixel/)]

**GHFeat: Generative Hierarchical Features from Synthesizing Images.**<br>
*Yinghao Xu, Yujun Shen, Jiapeng Zhu, Ceyuan Yang, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2007.10379.pdf)] [[Github](https://github.com/genforce/ghfeat)] [[Project](https://genforce.github.io/ghfeat/)]

**Hijack-GAN: Unintended-Use of Pretrained, Black-Box GANs.**<br>
*Hui-Po Wang, Ning Yu, Mario Fritz.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.14107)]

**Prior Image-Constrained Reconstruction using Style-Based Generative Models.**<br> 
*Varun A Kelkar, Mark Anastasio.*<br>
ICML 2021. [[PDF](https://arxiv.org/pdf/2102.12525.pdf)]

**Intermediate Layer Optimization for Inverse Problems using Deep Generative Models.**<br>
*Giannis Daras, Joseph Dean, Ajil Jalal, Alexandros G. Dimakis.*<br>
ICML 2021. [[PDF](https://arxiv.org/abs/2102.07364)] [[Github](https://github.com/giannisdaras/ilo)]

**Using Latent Space Regression to Analyze and Leverage Compositionality in GANs.**<br> 
*[Lucy Chai](http://people.csail.mit.edu/lrchai/), [Jonas Wulff](http://people.csail.mit.edu/jwulff/), [Phillip Isola](http://web.mit.edu/phillipi/).*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=sjuuTm4vj0)] [[Github](https://github.com/chail/latent-composition)] [[Project](https://chail.github.io/latent-composition/)] [[Colab](https://colab.research.google.com/drive/1p-L2dPMaqMyr56TYoYmBJhoyIyBJ7lzH?usp=sharing)]

**Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation.**<br>
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing.*<br>
ICLR 2021. [[PDF](https://arxiv.org/abs/2102.01187)]

**Disentangled Face Attribute Editing via Instance-Aware Latent Space Search.**<br>
*Yuxuan Han, [Jiaolong Yang](http://jlyang.org/), Ying Fu.*<br>
IJCAI 2021. [[PDF](https://arxiv.org/abs/2105.12660)] [[Github](https://github.com/yxuhan/IALS)]

**High Fidelity GAN Inversion via Prior Multi-Subspace Feature Composition.**<br> 
*Guanyue Li, Qianfen Jiao, Sheng Qian, Si Wu, Hau-San Wong.*<br> 
AAAI 2021. [[PDF](https://ojs.aaai.org/index.php/AAAI/article/view/17017)]

**e4e: Designing an Encoder for StyleGAN Image Manipulation.**<br>
*[Omer Tov](https://yotamnitzan.github.io/), Yuval Alaluf, Yotam Nitzan, Or Patashnik, Daniel Cohen-Or.*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2102.02766)] [[Github](https://github.com/omertov/encoder4editing)]

**StyleFlow: Attribute-conditioned Exploration of StyleGAN-Generated Images using Conditional Continuous Normalizing Flows.**<br>
*Rameen Abdal, Peihao Zhu, Niloy Mitra, Peter Wonka.*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2008.02401)] [[Github](https://rameenabdal.github.io/StyleFlow)]

**Mask-Guided Discovery of Semantic Manifolds in Generative Models.**<br>
*[Mengyu Yang](https://mengyu.page/), [David Rokeby](https://www.cdtps.utoronto.ca/people/directories/all-faculty/david-rokeby), [Xavier Snelgrove](https://wxs.ca/).*<br>
NeurIPS 2020 Workshop on Machine Learning for Creativity and Design. [[PDF](https://github.com/bmolab/masked-gan-manifold/blob/main/masked-gan-manifold.pdf)] [[Github](https://github.com/bmolab/masked-gan-manifold)]

**Face Identity Disentanglement via Latent Space Mapping.**<br>
*[Yotam Nitzan](https://yotamnitzan.github.io/), [Amit Bermano](https://www.cs.tau.ac.il/~amberman/), [Yangyan Li](https://yangyan.li/), Daniel Cohen-Or.*<br>
SIGGRAPH ASIA 2020. [[PDF](https://arxiv.org/abs/2005.07728)] [[Project](https://yotamnitzan.github.io/ID-disentanglement/)] [[Github](https://github.com/YotamNitzan/ID-disentanglement)]

**PIE: Portrait Image Embedding for Semantic Control.**<br> 
*[A. Tewari](http://people.mpi-inf.mpg.de/~atewari/), M. Elgharib, M. BR, F. Bernard, H-P. Seidel, P. P‌érez, M. Zollhöfer, C.Theobalt.*<br>
TOG 2020. [[PDF](http://gvv.mpi-inf.mpg.de/projects/PIE/data/paper.pdf)] [[Project](http://gvv.mpi-inf.mpg.de/projects/PIE/)]

**Understanding the Role of Individual Units in a Deep Neural Network.**<br>
*David Bau, Jun-Yan Zhu, Hendrik Strobelt, Agata Lapedriza, Bolei Zhou, Antonio Torralba.*<br>
National Academy of Sciences 2020. [[PDF](https://arxiv.org/abs/2009.05041)] [[Github](https://github.com/davidbau/dissect/)] [[Project](https://dissect.csail.mit.edu/)]

**Face Identity Disentanglement via Latent Space Mapping.**<br>
*Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or.*<br>
TOG 2020. [[PDF](https://arxiv.org/abs/2005.07728)] [[Github](https://github.com/YotamNitzan/ID-disentanglement)]

**Transforming and Projecting Images into Class-conditional Generative Networks.**<br>
*[Minyoung Huh](http://minyounghuh.com/), [Richard Zhang](https://richzhang.github.io/), [Jun-Yan Zhu](https://people.csail.mit.edu/junyanz/), [Sylvain Paris](http://people.csail.mit.edu/sparis/), [Aaron Hertzmann](https://www.dgp.toronto.edu/~hertzman/).*<br>
ECCV 2020. [[PDF](http://arxiv.org/abs/2005.01703)] [[Github](https://github.com/minyoungg/GAN-Transform-and-Project)] [[Project](https://minyoungg.github.io/GAN-Transform-and-Project/)]

**MimicGAN: Robust Projection onto Image Manifolds with Corruption Mimicking.**<br>
*[Rushil Anirudh](https://rushila.com/), [Jayaraman J. Thiagarajan](https://jjthiagarajan.com/), [Bhavya Kailkhura](https://people.llnl.gov/kailkhura1), [Timo Bremer](https://people.llnl.gov/bremer5).*<br>
IJCV 2020. [[PDF](https://link.springer.com/article/10.1007/s11263-020-01310-5)]

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
TOG 2019. [[PDF](https://arxiv.org/abs/2005.07727)]

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
IJCAI 2017. [[PDF](https://arxiv.org/abs/1705.08664)]

**One Network to Solve Them All - Solving Linear Inverse Problems using Deep Projection Models.**<br>
*J. H. Rick Chang, Chun-Liang Li, Barnabas Poczos, B. V. K. Vijaya Kumar, Aswin C. Sankaranarayanan.*<br>
ICCV 2017. [[PDF](https://arxiv.org/abs/1703.09912)]

**Precise Recovery of Latent Vectors from Generative Adversarial Networks.**<br>
*Zachary C. Lipton, Subarna Tripathi.*<br>
ICLR 2017 workshop. [[PDF](https://arxiv.org/abs/1702.04782)] [[Github](https://github.com/SubarnaTripathi/ReverseGAN)]

**Inverting The Generator Of A Generative Adversarial Network.**<br>
*Antonia Creswell, Anil Anthony Bharath.*<br>
NeurIPS 2016 Workshop. [[PDF](https://arxiv.org/abs/1611.05644)]

**Generative Visual Manipulation on the Natural Image Manifold.**<br>
*Jun-Yan Zhu, Philipp Krähenbühl, Eli Shechtman, Alexei A. Efros.*<br>
ECCV 2016. [[PDF](https://arxiv.org/abs/1609.03552v2)]

### 3D GAN inverson

**3D GAN Inversion for Controllable Portrait Image Animation.**<br>
*[Connor Z. Lin](https://connorzlin.com/), David B. Lindell, Eric R. Chan, [Gordon Wetzstein](https://stanford.edu/~gordonwz/).*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2203.13441)] [[Project](https://www.computationalimaging.org/publications/3dganinversion/)]

**Pix2NeRF: Unsupervised Conditional π-GAN for Single Image to Neural Radiance Fields Translation.**<br>
*Shengqu Cai, Anton Obukhov, Dengxin Dai, Luc Van Gool.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2202.13162)]

**Unsupervised 3D Shape Completion through GAN-Inversion.**<br>
*[Junzhe Zhang](https://junzhezhang.github.io/), Xinyi Chen, Zhongang Cai, Liang Pan, Haiyu Zhao, Shuai Yi, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2104.13366)] [[Project](https://junzhezhang.github.io/projects/ShapeInversion/)]

<p width="100%" align="right"><a href="#">🔝</a></p>

## latent space navigation

Inversion is not the ultimate goal. The reason that we invert a real image into the latent space of a trained GAN model is that we can manipulate the inverted image in the latent space by discovering the desired code with certain attributes. This technique is usually known as latent space navigation, GAN steerability, latent code manipulation, or other names in the literature. Although often regarded as an independent research field, it acts as an indispensable component of GAN inversion for manipulation. Many inversion methods also involve efficient discovery of a desired latent code.

**Exploring Gradient-based Multi-directional Controls in GANs.**<br>
*Zikun Chen, Ruowei Jiang, Brendan Duke, Han Zhao, Parham Aarabi.*<br>
ECCV 2022 (oral). [[PDF](https://arxiv.org/abs/2209.00698)] [[Project](https://github.com/zikuncshelly/GradCtrl)] 

**Hierarchical Semantic Regularization of Latent Spaces in StyleGANs.**<br>
*Tejan Karmali, Rishubh Parihar, Susmit Agrawal, Harsh Rangwani, Varun Jampani, Maneesh Singh, R. Venkatesh Babu.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2208.03764)] [[Project](https://sites.google.com/view/hsr-eccv22/)] 
 
**CLIP2StyleGAN: Unsupervised Extraction of StyleGAN Edit Directions.**<br>
*Rameen Abdal, Peihao Zhu, John Femiani, Niloy J. Mitra, Peter Wonka.*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2112.05219)] [[Github](https://github.com/RameenAbdal/CLIP2StyleGAN)]

**Region-Based Semantic Factorization in GANs.**<br>
*Jiapeng Zhu, Yujun Shen, Yinghao Xu, Deli Zhao, Qifeng Chen.*<br>
ICML 2022. [[PDF](https://arxiv.org/abs/2202.09649)] [[Github](https://github.com/zhujiapeng/resefa)]

**Latent Image Animator: Learning to Animate Image via Latent Space Navigation.**<br>
*Yaohui Wang, Di Yang, Francois Bremond, Antitza Dantcheva.*<br>
ICLR 2022. [[PDF](https://openreview.net/forum?id=7r6kDq0mK_)] [[Project](https://wyhsirius.github.io/LIA-project)] [[Github](https://github.com/wyhsirius/LIA)]

**Do Not Escape From the Manifold: Discovering the Local Coordinates on the Latent Space of GANs.**<br>
*Jaewoong Choi, Changyeon Yoon, Junho Lee, Jung Ho Park, Geonho Hwang, Myungjoo Kang.*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2106.06959)]

**Tensor-based Emotion Editing in the StyleGAN Latent Space.**<br>
*René Haas, Stella Graßhof, Sami S. Brandt.*<br>
CVPR 2022 Workshop on AI for Content Creation Workshop. [[PDF](https://arxiv.org/pdf/2205.06102.pdf)]

**PaintInStyle: One-Shot Discovery of Interpretable Directions by Painting.**<br>
*Berkay Doner, Elif Sema Balcioglu, Merve Rabia Barin, Umut Kocasari, Mert Tiftikci, Pinar Yanardag.*<br>
CVPR 2022 Workshops. [[PDF](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/html/Doner_PaintInStyle_One-Shot_Discovery_of_Interpretable_Directions_by_Painting_CVPRW_2022_paper.html)]

**Rank in Style: A Ranking-Based Approach To Find Interpretable Directions.**<br>
*Umut Kocasari, Kerem Zaman, Mert Tiftikci, Enis Simsar, Pinar Yanardag.*<br>
CVPR 2022 Workshops. [[PDF](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/html/Kocasari_Rank_in_Style_A_Ranking-Based_Approach_To_Find_Interpretable_Directions_CVPRW_2022_paper.html)]

**LARGE: Latent-Based Regression through GAN Semantics.**<br>
*[Yotam Nitzan](https://yotamnitzan.github.io), [Rinon Gal](https://rinongal.github.io/), [Ofir Brenner](https://scholar.google.com/citations?user=iLLlWr8AAAAJ), [Daniel Cohen-Or](https://danielcohenor.com/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2107.11186)] [[Github](https://github.com/YotamNitzan/LARGE)] [[Project](https://yotamnitzan.github.io/LARGE)]

**StyleFusion: Disentangling Spatial Segments in StyleGAN-Generated Images.**<br>
*Omer Kafri, Or Patashnik, Yuval Alaluf, Daniel Cohen-Or.*<br>
TOG 2022. [[PDF](https://arxiv.org/abs/2107.07437)] [[Github](https://github.com/OmerKafri/StyleFusion)]

**Fantastic Style Channels and Where to Find Them: A Submodular Framework for Discovering Diverse Directions in GANs.**<br>
*[Enis Simsar](https://enis.dev/), [Umut Kocasari](https://catlab-team.github.io/), [Ezgi Gülperi Er](https://catlab-team.github.io/), [Pinar Yanardag](https://pinguar.org/).*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2203.08516)] [[Project](https://catlab-team.github.io/fantasticstyles/)] [[Demo](https://catlab-team.github.io/styleatlas/classes/FFHQ/)]

**Analyzing the Latent Space of GAN through Local Dimension Estimation.**<br>
*Jaewoong Choi, Geonho Hwang, Hyunsoo Cho, Myungjoo Kang.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2205.13182)]

**PandA: Unsupervised Learning of Parts and Appearances in the Feature Maps of GANs.**<br>
*James Oldfield, Christos Tzelepis, Yannis Panagakis, Mihalis A. Nicolaou, Ioannis Patras.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2206.00048)] [[Project](http://eecs.qmul.ac.uk/~jo001/PandA/)] [[Github](https://github.com/james-oldfield/PandA)] 

**Multi-level Latent Space Structuring for Generative Control.**<br>
*[Oren Katzir](https://orenkatzir.github.io/), Vicky Perepelook, Dani Lischinski, Daniel Cohen-Or.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2202.05910)]

**Rayleigh EigenDirections (REDs): GAN Latent Space Traversals for Multidimensional Features.**<br>
*Guha Balakrishnan, Raghudeep Gadde, Aleix Martinez, Pietro Perona.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2201.10423.pdf)]

**Optimizing Latent Space Directions For GAN-based Local Image Editing.**<br>
*Ehsan Pajouheshgar, Tong Zhang, Sabine Süsstrunk.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2111.12583)]

**Interpreting the Latent Space of GANs via Correlation Analysis for Controllable Concept Manipulation.**<br>
*Ziqiang Li, Rentuo Tao, Hongjing Niu, Bin Li.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2006.10132)]

**Tensor Component Analysis for Interpreting the Latent Space of GANs.**<br>
*[James Oldfield](https://james-oldfield.github.io/), Markos Georgopoulos, Yannis Panagakis, Mihalis A. Nicolaou, Ioannis Patras.*<br>
BMVC 2021. [[PDF](https://arxiv.org/abs/2111.11736)] [[Project](http://eecs.qmul.ac.uk/~jo001/TCA-latent-space/)] [[Github](https://github.com/james-oldfield/TCA-latent-space)]

**Tensor-based Subspace Factorization for StyleGAN.**<br>
*Rene Haas, Stella Graßhof and Sami S. Brandt.*<br>
FG 2021. [[PDF](https://arxiv.org/abs/2111.04554)]

**Exploratory Search of GANs with Contextual Bandits.**<br> 
*Ivan Kropotov, Alan Medlar, Dorota Glowacka.*<br> 
CIKM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3459637.3482103)]

**LowRankGAN: Low-Rank Subspaces in GANs.**<br> 
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen.*<br> 
NeurIPS 2021. [[PDF](https://arxiv.org/abs/2106.04488)] [[Github](https://github.com/zhujiapeng/LowRankGAN)]

**Controllable and Compositional Generation with Latent-Space Energy-Based Models.**<br>
*Weili Nie, Arash Vahdat, Anima Anandkumar.*<br>
NeurIPS 2021. [[PDF](https://arxiv.org/abs/2110.10873)]

**A Latent Transformer for Disentangled Face Editing in Images and Videos.**<br>
*Xu Yao, Alasdair Newson, Yann Gousseau, Pierre Hellier.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/html/Yao_A_Latent_Transformer_for_Disentangled_Face_Editing_in_Images_and_ICCV_2021_paper.html)] [[ArXiV](https://arxiv.org/abs/2106.11895)] [[Github](https://github.com/InterDigitalInc/latent-transformer)]

**Toward a Visual Concept Vocabulary for GAN Latent Space.**<br>
*Sarah Schwettmann, Evan Hernandez, David Bau, Samuel Klein, Jacob Andreas, Antonio Torralba.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/html/Schwettmann_Toward_a_Visual_Concept_Vocabulary_for_GAN_Latent_Space_ICCV_2021_paper.html)] [[Project](https://visualvocab.csail.mit.edu/)]

**WarpedGANSpace: Finding Non-linear RBF Paths in GAN Latent Space.**<br>
*Christos Tzelepis, Georgios Tzimiropoulos, Ioannis Patras.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2109.13357)] [[Github](https://github.com/chi0tzp/WarpedGANSpace)]

**Latent Transformations via NeuralODEs for GAN-based Image Editing.**<br>
*Valentin Khrulkov, Leyla Mirvakhabova, Ivan Oseledets, Artem Babenko.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Khrulkov_Latent_Transformations_via_NeuralODEs_for_GAN-Based_Image_Editing_ICCV_2021_paper.pdf)] [[Github](https://github.com/KhrulkovV/nonlinear-image-editing)]

**OroJaR: Orthogonal Jacobian Regularization for Unsupervised Disentanglement in Image Generation.**<br>
*Yuxiang Wei, Yupeng Shi, Xiao Liu, Zhilong Ji, Yuan Gao, Zhongqin Wu, Wangmeng Zuo.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2108.07668)] [[Github](https://github.com/csyxwei/OroJaR)]

**EigenGAN: Layer-Wise Eigen-Learning for GANs.**<br>
*Zhenliang He, Meina Kan, Shiguang Shan.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.12476)] [[Github](https://github.com/LynnHo/EigenGAN-Tensorflow)]

**SalS-GAN: Spatially-Adaptive Latent Space in StyleGAN for Real Image Embedding.**<br>
*Lingyun Zhang, Xiuxiu Bai, Yao Gao.*<br>
ACM MM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3474085.3475633)]

**Discovering Density-Preserving Latent Space Walks in GANs for Semantic Image Transformations.**<br>
*Guanyue Li, Yi Liu, Xiwen Wei, Yang Zhang, Si Wu, Yong Xu, Hau San Wong.*<br>
ACM MM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3474085.3475293)]

**Discovering Interpretable Latent Space Directions of GANs Beyond Binary Attributes.**<br>
*Huiting Yang, Liangyu Chai, Qiang Wen, Shuang Zhao, Zixun Sun, Shengfeng He.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_Discovering_Interpretable_Latent_Space_Directions_of_GANs_Beyond_Binary_Attributes_CVPR_2021_paper.pdf)]

**Surrogate Gradient Field for Latent Space Manipulation.**<br>
*Minjun Li, Yanghua Jin, Huachun Zhu.*<br>
CVPR 2021. [[PDF](http://arxiv.org/abs/2104.09065)]

**SeFa: Closed-Form Factorization of Latent Semantics in GANs.**<br>
*Yujun Shen, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2007.06600)] [[Github](https://github.com/genforce/sefa)] [[Project](https://genforce.github.io/sefa/)]

**L2M-GAN: Learning To Manipulate Latent Space Semantics for Facial Attribute Editing.**<br>
*Guoxing Yang, Nanyi Fei, Mingyu Ding, Guangzhen Liu, Zhiwu Lu, Tao Xiang.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_L2M-GAN_Learning_To_Manipulate_Latent_Space_Semantics_for_Facial_Attribute_CVPR_2021_paper.html)] [[Unofficial Pytorch](https://github.com/songquanpeng/L2M-GAN)]

**MoCoGAN-HD: A Good Image Generator Is What You Need for High-Resolution Video Synthesis.**<br>
*Yu Tian, Jian Ren, Menglei Chai, Kyle Olszewski, Xi Peng, Dimitris N. Metaxas, Sergey Tulyakov.*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=6puCSjH3hwA)] [[Github](https://github.com/snap-research/MoCoGAN-HD)]

**GAN Steerability without optimization.**<br>
*Nurit Spingarn-Eliezer, Ron Banner, Tomer Michaeli.*<br>
ICLR 2021. [[OpenReview](https://openreview.net/forum?id=zDy_nQCXiIj)] [[PDF](https://arxiv.org/abs/2012.05328)]

**On the "steerability" of generative adversarial networks.**<br>
*Ali Jahanian, Lucy Chai, Phillip Isola.*<br>
ICLR 2020. [[PDF](https://arxiv.org/abs/1907.07171)] [[Project](https://ali-design.github.io/gan_steerability/)]

**GANSpace: Discovering Interpretable GAN Controls.**<br>
*Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2004.02546)] [[Github](https://github.com/harskish/ganspace)]

**Interpreting the Latent Space of GANs for Semantic Face Editing.**<br>
*[Yujun Shen](http://shenyujun.github.io/), [Jinjin Gu](http://www.jasongt.com/), [Xiaoou Tang](http://www.ie.cuhk.edu.hk/people/xotang.shtml), [Bolei Zhou](http://bzhou.ie.cuhk.edu.hk/).*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1907.10786)] [[Project](https://genforce.github.io/interfacegan/)] [[Github](https://github.com/genforce/interfacegan)]

**Seeing What a GAN Cannot Generate.**<br>
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1910.11626)] [[PDF](http://ganseeing.csail.mit.edu/)]

**Unsupervised Discovery of Interpretable Directions in the GAN Latent Space.**<br>
*Andrey Voynov, Artem Babenko.*<br>
ICML 2020. [[PDF](https://arxiv.org/abs/2002.03754)] [[Github](https://github.com/anvoynov/GANLatentDiscovery)]

<p width="100%" align="right"><a href="#">🔝</a></p>

## application

### image and video generation and manipulation

**DyStyle: Dynamic Neural Network for Multi-Attribute-Conditioned Style Editing.**<br>
*Bingchuan Li, Shaofei Cai, Wei Liu, Peng Zhang, Miao Hua, Qian He, Zili Yi.*<br>
WACV 2023. [[PDF](https://arxiv.org/abs/2109.10737)] [[Github](https://github.com/phycvgan/DyStyle)]

**Generative Visual Prompt: Unifying Distributional Control of Pre-Trained Generative Models.**<br>
*Chen Henry Wu, Saman Motamed, Shaunak Srivastava, Fernando De la Torre.*<br>
NeurIPS 2022. [[PDF](https://arxiv.org/abs/2209.06970)] [[Github](https://github.com/ChenWu98/Generative-Visual-Prompt)]

**3D-FM GAN: Towards 3D-Controllable Face Manipulation.**<br>
*[Yuchen Liu](https://lychenyoko.github.io/), Zhixin Shu, Yijun Li, Zhe Lin, Richard Zhang, and Sun-Yuan Kung.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2208.11257)] [[Project](https://lychenyoko.github.io/3D-FM-GAN-Webpage/)]

**Generative Multiplane Images: Making a 2D GAN 3D-Aware.**<br>
*[Xiaoming Zhao](https://xiaoming-zhao.com/), [Fangchang Ma](https://fangchangma.github.io/), [David Güera](https://scholar.google.com/citations?user=bckYvFkAAAAJ&hl=en), [Zhile Ren](https://jrenzhile.com/), [Alexander G. Schwing](https://www.alexander-schwing.de/), [Alex Colburn](https://www.colburn.org/).*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2207.10642)] [[Project](https://xiaoming-zhao.github.io/projects/gmpi/)] [[Github](https://github.com/apple/ml-gmpi)]

**Injecting 3D Perception of Controllable NeRF-GAN into StyleGAN for Editable Portrait Image Synthesis.**<br>
*Jeong-gi Kwak, Yuanming Li, Dongsik Yoon, Donghyeon Kim, David Han, Hanseok Ko.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2207.10257)] [[Project](https://jgkwak95.github.io/surfgan/)]

**Temporally Consistent Semantic Video Editing.**<br>
*[Yiran Xu](https://twizwei.github.io/), [Badour AlBahar](https://badouralbahar.github.io/), [Jia-Bin Huang](https://jbhuang0604.github.io/).*<br>
ECCV 2022. [[PDF](https://arxiv.org/pdf/2206.10590.pdf)] [[Project](https://video-edit-gan.github.io/)] 

**Sound-Guided Semantic Video Generation.**<br>
*Seung Hyun Lee, Gyeongrok Oh, Wonmin Byeon, Jihyun Bae, Chanyoung Kim, Won Jeong Ryoo, Sang Ho Yoon, Jinkyu Kim, Sangpil Kim.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2204.09273)] [[Project](https://kuai-lab.github.io/eccv2022sound/)] [[Github]()]

**Everything is There in Latent Space: Attribute Editing and Attribute Style Manipulation by StyleGAN Latent Space Exploration.**<br>
*Rishubh Parihar, Ankit Dhiman, Tejan Karmali, R. Venkatesh Babu.*<br>
ACM MM 2022. [[PDF](https://arxiv.org/abs/2207.09855)] [[Project](https://sites.google.com/view/flamelatentediting)]

**SD-GAN: Semantic Decomposition for Face Image Synthesis with Discrete Attribute.**<br>
*Zhou Kangneng, Zhu Xiaobin, Gao Daiheng, Lee Kai, Li Xinjie, Yin Xu-Cheng.*<br>
ACM MM 2022. [[PDF](https://arxiv.org/abs/2207.05300)]

**Identity-Guided Face Generation with Multi-modal Contour Conditions.**<br>
*Qingyan Bai, Weihao Xia, Fei Yin, Yujiu Yang.*<br>
ICIP 2022. [[PDF](https://arxiv.org/abs/2110.04854)]

**Self-Conditioned Generative Adversarial Networks for Image Editing.**<br>
*Yunzhe Liu, Rinon Gal, Amit H. Bermano, Baoquan Chen, Daniel Cohen-Or.*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2202.04040)] [[Project](https://github.com/yzliu567/sc-gan)]

**SphericGAN: Semi-Supervised Hyper-Spherical Generative Adversarial Networks for Fine-Grained Image Synthesis.**<br>
*Tianyi Chen, Yunfei Zhang, Xiaoyang Huo, Si Wu, Yong Xu, Hau San Wong.*<br>
CVPR 2022. [[PDF](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_SphericGAN_Semi-Supervised_Hyper-Spherical_Generative_Adversarial_Networks_for_Fine-Grained_Image_Synthesis_CVPR_2022_paper.html)]

**Sound-Guided Semantic Image Manipulation.**<br>
*Seung Hyun Lee, Wonseok Roh, Wonmin Byeon, Sang Ho Yoon, Chan Young Kim, Jinkyu Kim, Sangpil Kim.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.00007)]

**HairCLIP: Design Your Hair by Text and Reference Image.**<br>
*Tianyi Wei, Dongdong Chen, Wenbo Zhou, Jing Liao, Zhentao Tan, Lu Yuan, Weiming Zhang, Nenghai Yu.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.05142)] [[Github](https://github.com/wty-ustc/HairCLIP)]

**HairMapper: Removing Hair from Portraits Using GANs.**<br>
*[Yiqian Wu](https://onethousandwu.com/), [Yong-Liang Yang](http://www.yongliangyang.net/), [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin).*<br>
CVPR 2022. [[PDF](http://www.cad.zju.edu.cn/home/jin/cvpr2022/HairMapper.pdf)] [[Project](http://www.cad.zju.edu.cn/home/jin/cvpr2022/cvpr2022.htm)] [[Github](https://github.com/oneThousand1000/non-hair-FFHQ/blob/main)] [[Non-hair-FFHQ Data](https://github.com/oneThousand1000/non-hair-FFHQ)]

**Attribute Group Editing for Reliable Few-shot Image Generation.**<br>
*Guanqi Ding, Xinzhe Han, Shuhui Wang, Shuzhe Wu, Xin Jin, Dandan Tu, Qingming Huang.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.08422)] [[Github](https://github.com/UniBester/AGE)]

**InsetGAN for Full-Body Image Generation.**<br>
*[Anna Frühstück](https://afruehstueck.github.io/), [Krishna Kumar Singh](http://krsingh.cs.ucdavis.edu/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Niloy J. Mitra](https://research.adobe.com/person/niloy-mitra/), [Peter Wonka](http://peterwonka.net/), [Jingwan Lu](https://research.adobe.com/person/jingwan-lu/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.07200)] [[Project](http://afruehstueck.github.io/insetgan)] [[Unofficial](https://github.com/stylegan-human/StyleGAN-Human/blob/main/insetgan.py)]

**SpaceEdit: Learning a Unified Editing Space for Open-Domain Image Editing.**<br>
*[Jing Shi](https://www.cs.rochester.edu/u/jshi31/), [Ning Xu](https://sites.google.com/view/ningxu/), [Haitian Zheng](https://www.cs.rochester.edu/u/hzheng15/haitian_homepage/index.html), Alex Smith, [Jiebo Luo](https://www.cs.rochester.edu/u/jluo/), [Chenliang Xu](https://www.cs.rochester.edu/~cxu22/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.00180)]

**In&Out: Diverse Image Outpainting via GAN Inversion.**<br>
*Yen-Chi Cheng, Chieh Hubert Lin, Hsin-Ying Lee, Jian Ren, Sergey Tulyakov, Ming-Hsuan Yang.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2104.00675)] [[Github](https://yccyenchicheng.github.io/InOut/)]

**InfinityGAN: Towards Infinite-Resolution Image Synthesis.**<br>
*Chieh Hubert Lin, Hsin-Ying Lee, Yen-Chi Cheng, Sergey Tulyakov, Ming-Hsuan Yang.*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2104.03963)] [[Project](https://hubert0527.github.io/infinityGAN/)]

**Latent to Latent: A Learned Mapper for Identity Preserving Editing of Multiple.**<br>
*Siavash Khodadadeh, Shabnam Ghadar, Saeid Motiian, Wei-An Lin, Ladislau Bölöni, Ratheesh Kalarot.*<br>
WACV 2022. [[PDF](https://openaccess.thecvf.com/content/WACV2022/html/Khodadadeh_Latent_to_Latent_A_Learned_Mapper_for_Identity_Preserving_Editing_WACV_2022_paper.html)]

**StyleVideoGAN: A Temporal Generative Model using a Pretrained StyleGAN.**<br>
*[Gereon Fox](https://www.mpi-inf.mpg.de/~gfox/), [Ayush Tewari](https://www.mpi-inf.mpg.de/~atewari/), Mohamed Elgharib, [Christian Theobalt](http://gvv.mpi-inf.mpg.de/).*<br>
BMVC 2021 (Oral). [[PDF](https://arxiv.org/abs/2107.07224)]

**Constrained Graphic Layout Generation via Latent Optimization.**<br>
*Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.*<br>
ACM MM 2021. [[PDF](https://arxiv.org/abs/2108.00871)] [[Github](https://github.com/ktrk115/const_layout)]

**Face Image Retrieval With Attribute Manipulation.**<br>
*[Alireza Zaeemzadeh](https://zaeemzadeh.com/), Shabnam Ghadar, Baldo Faieta, Zhe Lin, Nazanin Rahnavard, Mubarak Shah, Ratheesh Kalarot.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/html/Zaeemzadeh_Face_Image_Retrieval_With_Attribute_Manipulation_ICCV_2021_paper.html)]

**StyleCariGAN: Caricature Generation via StyleGAN Feature Map Modulation.**<br>
*Wongjong Jang, Gwangjin Ju, [Yucheol Jung](https://ycjung.info/), [Jiaolong Yang](http://jlyang.org/), [Xin Tong](https://www.microsoft.com/en-us/research/people/xtong/), [Seungyong Lee](http://phome.postech.ac.kr/~leesy/).*<br>
TOG 2021. [[PDF](https://arxiv.org/pdf/2107.04331.pdf)] [[Github](https://github.com/PeterZhouSZ/StyleCariGAN)]

**Coarse-to-Fine: Facial Structure Editing of Portrait Images via Latent Space Classifications.**<br>
*[Yiqian Wu](https://onethousandwu.com/), [Yongliang Yang](http://www.yongliangyang.net/), Qinjie Xiao, [Xiaogang Ji](http://www.cad.zju.edu.cn/home/jin).*<br>
TOG 2021. [[PDF](http://www.cad.zju.edu.cn/home/jin/sig2021/paper46.pdf)] [[Project](http://www.cad.zju.edu.cn/home/jin/sig2021/sig2021.htm)]

**SAM: Only a Matter of Style-Age Transformation Using a Style-Based Regression Model.**<br>
*Yuval Alaluf, Or Patashnik, [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2102.02754)] [[Github](https://github.com/yuval-alaluf/SAM)]

**Barbershop: GAN-based Image Compositing using Segmentation Masks.**<br>
*[Peihao Zhu](https://github.com/ZPdesu), [Rameen Abdal](https://github.com/RameenAbdal), [John Femiani](https://scholar.google.com/citations?user=rS1xJIIAAAAJ&hl=en), [Peter Wonka](http://peterwonka.net/).*<br>
SIGGRAPH Asia 2021. [[PDF](https://arxiv.org/abs/2106.01505)] [[Project](https://zpdesu.github.io/Barbershop/)] [[Github](https://github.com/ZPdesu/Barbershop)]

**Exploring Adversarial Fake Images on Face Manifold.**<br>
*Dongze Li, Wei Wang, Hongxing Fan, Jing Dong.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2101.03272)]

**HistoGAN: Controlling Colors of GAN-Generated and Real Images via Color Histograms.**<br>
*[Mahmoud Afifi](https://sites.google.com/view/mafifi), Marcus A. Brubaker, Michael S. Brown.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.11731)] [[Github](https://github.com/mahmoudnafifi/HistoGAN)] [[4K Landscape](https://ln2.sync.com/dl/1891becc0/uhsxtprq-33wfwmyq-dhhqeb3s-mtstuqw7/view/default/11118541390008)]

**One Shot Face Swapping on Megapixels.**<br>
*Yuhao Zhu, Qi Li, Jian Wang, Chengzhong Xu, Zhenan Sun.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2105.04932.pdf)] [[Github](https://github.com/zyainfal/One-Shot-Face-Swapping-on-Megapixels)]

**LOHO: Latent Optimization of Hairstyles via Orthogonalization.**<br>
*Rohit Saha, Brendan Duke, Florian Shkurti, Graham W. Taylor, Parham Aarabi.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2103.03891)] [[Github](https://github.com/dukebw/LOHO)]

**StyleMapGAN: Exploiting Spatial Dimensions of Latent in GAN for Real-time Image Editing.**<br>
*[Hyunsu Kim](https://github.com/blandocs), [Yunjey Choi](https://yunjey.github.io/), [Junho Kim](https://github.com/taki0112), [Sungjoo Yoo](http://cmalab.snu.ac.kr/), [Youngjung Uh](https://github.com/youngjung).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.14754)] [[Github](https://github.com/naver-ai/StyleMapGAN)]

**DeepI2I: Enabling Deep Hierarchical Image-to-Image Translation by Transferring from GANs.**<br>
*yaxing wang, Lu Yu, Joost van de Weijer.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2011.05867)] [[Github](https://github.com/yaxingwang/DeepI2I)]

**Generalized One-shot Domain Adaption of Generative Adversarial Networks.**<br>
*Zicheng Zhang, Yinglu Liu, Congying Han, Tiande Guo, Ting Yao, Tao Mei.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2209.03665)]

**Robust Sound-Guided Image Manipulation.**<br>
*Seung Hyun Lee, Chanyoung Kim, Wonmin Byeon, Gyeongrok Oh, Jooyoung Lee, Sang Ho Yoon, Jinkyu Kim, Sangpil Kim.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2208.14114)]

**Prompt-to-Prompt Image Editing with Cross Attention Control.**<br>
*Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, Daniel Cohen-Or.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2207.09446)]

**An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion.**<br>
*Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2207.09446)] [[Project](https://textual-inversion.github.io/)] [[Github](https://github.com/rinongal/textual_inversion)]

**Stitch it in Time: GAN-Based Facial Editing of Real Videos.**<br>
*Rotem Tzaban, Ron Mokady, Rinon Gal, Amit H. Bermano, Daniel Cohen-Or.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2201.08361)] [[Project](https://stitch-time.github.io/)] [[Github](https://github.com/rotemtzaban/STIT)]

**FEAT: Face Editing with Attention.**<br>
*Xianxu Hou, Linlin Shen, Or Patashnik, Daniel Cohen-Or, Hui Huang.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2202.02713)]

**Few-shot Semantic Image Synthesis Using StyleGAN Prior.**<br>
*Yuki Endo, Yoshihiro Kanamori.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2103.14877)] [[Github](https://github.com/endo-yuki-t/Fewshot-SMIS)]

**Heredity-aware Child Face Image Generation with Latent Space Disentanglement.**<br>
*Xiao Cui, Wengang Zhou, Yang Hu, Weilun Wang, Houqiang Li.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2108.11080)]

**Unsupervised Image Transformation Learning via Generative Adversarial Networks.**<br>
*Kaiwen Zha, Yujun Shen, Bolei Zhou.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2103.07751)] [[Project](https://genforce.github.io/trgan)]

**Unsupervised Image-to-Image Translation via Pre-trained StyleGAN2 Network.**<br>
*Jialu Huang, Jing Liao, Sam Kwong.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2010.05713)]

### multimodal learning

**StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators.**<br>
*[Rinon Gal](https://rinongal.github.io/), [Or Patashnik](https://orpatashnik.github.io/), [Haggai Maron](https://haggaim.github.io/), [Gal Chechik](https://research.nvidia.com/person/gal-chechik), [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2108.00946)] [[Project](https://stylegan-nada.github.io/)] [[Github](https://github.com/rinongal/StyleGAN-nada)]

**Paint by Word.**<br>
*David Bau, Alex Andonian, Audrey Cui, YeonHwan Park, Ali Jahanian, Aude Oliva, Antonio Torralba.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2103.10951)]

**CI-GAN: Cycle-Consistent Inverse GAN for Text-to-Image Synthesis.**<br>
*Hao Wang, Guosheng Lin, Steven C. H. Hoi, Chunyan Miao.*<br>
ACM MM 2021. [[PDF](https://arxiv.org/abs/2108.01361)]

**TediGAN: Text-Guided Diverse Image Generation and Manipulation.**<br>
*Weihao Xia, Yujiu Yang, Jing-Hao Xue, Baoyuan Wu.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.03308)] [[Data](https://github.com/weihaox/Multi-Modal-CelebA-HQ)] [[Github](https://github.com/weihaox/TediGAN)]

**DeepLandscape: Adversarial Modeling of Landscape Videos.**<br>
*E. Logacheva, R. Suvorov, O. Khomenko, A. Mashikhin, and V. Lempitsky.*<br>
ECCV 2020. [[PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123680256.pdf)] [[Github](https://github.com/saic-mdal/deep-landscape)] [[Project](https://saic-mdal.github.io/deep-landscape/)]

### image restoration

**High-Fidelity Image Inpainting with GAN Inversion.**<br>
*Yongsheng Yu, Libo Zhang, Heng Fan, Tiejian Luo.*<br>
ECCV 2022. [[PDF](https://arxiv.org/pdf/2203.16669)]

**Escaping Data Scarcity for High-Resolution Heterogeneous Face Hallucination.**<br>
*Yiqun Mei, Pengfei Guo, Vishal M. Patel.*<br>
CVPR 2022. [[PDF](https://arxiv.org/pdf/2203.16669)]

**Towards High-Fidelity Face Self-Occlusion Recovery via Multi-View Residual-Based GAN Inversion.**<br>
*Jinsong Chen, Hu Han, Shiguang Shan.*<br>
AAAI 2022. [[PDF](https://www.aaai.org/AAAI22Papers/AAAI-2208.ChenJ.pdf)]

**Time-Travel Rephotography.**<br>
*[Xuan Luo](https://time-travel-rephotography.github.io/), [Xuaner Zhang](https://people.eecs.berkeley.edu/~cecilia77/), [Paul Yoo](https://www.linkedin.com/in/paul-yoo-768a3715b), [Ricardo Martin-Brualla](http://www.ricardomartinbrualla.com/), [Jason Lawrence](http://jasonlawrence.info/), [Steven M. Seitz](https://homes.cs.washington.edu/~seitz/).*<br>
SIGGRAPH Asia 2021 (TOG). [[PDF](https://arxiv.org/abs/2012.12261)] [[Project](https://time-travel-rephotography.github.io/)] [[Github](https://github.com/Time-Travel-Rephotography/Time-Travel-Rephotography.github.io)]

**GPEN: GAN Prior Embedded Network for Blind Face Restoration in the Wild.**<br>
*Tao Yang, Peiran Ren, Xuansong Xie, Lei Zhang.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_GAN_Prior_Embedded_Network_for_Blind_Face_Restoration_in_the_CVPR_2021_paper.pdf)] [[Github](https://github.com/)]

**GLEAN: Generative Latent Bank for Large-Factor Image Super-Resolution.**<br>
*[Kelvin C.K. Chan](https://ckkelvinchan.github.io/), Xintao Wang, Xiangyu Xu, Jinwei Gu, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.00739)] [[Project](https://ckkelvinchan.github.io/projects/GLEAN)] [[Github](https://github.com/ckkelvinchan/GLEAN)]

**GFP-GAN: Towards Real-World Blind Face Restoration with Generative Facial Prior.**<br>
*[Xintao Wang](https://xinntao.github.io/), [Yu Li](https://yu-li.github.io/), [Honglun Zhang](https://scholar.google.com/citations?hl=en&user=KjQLROoAAAAJ), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2101.04061)] [[Project](https://xinntao.github.io/)]

**PULSE: Self-Supervised Photo Upsampling via Latent Space Exploration of Generative Models.**<br>
*Sachit Menon, Alexandru Damian, Shijia Hu, Nikhil Ravi, Cynthia Rudin.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/2003.03808)] [[Github](https://github.com/adamian98/pulse)]

**Semantic uncertainty intervals for disentangled latent spaces.**<br> 
*Swami Sankaranarayanan, Anastasios N. Angelopoulos, Stephen Bates, Yaniv Romano, Phillip Isola.*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2207.10074)] [[Github](https://github.com/swamiviv/generative_semantic_uncertainty)]

**LTT-GAN: Looking Through Turbulence by Inverting GANs.**<br> 
*[Kangfu Mei](https://kfmei.page/), [Vishal M. Patel](https://engineering.jhu.edu/vpatel36/sciencex_teams/vishalpatel/).*<br> 
arxiv 2021. [[PDF](https://arxiv.org/abs/2112.02379)] [[Project](https://kfmei.page/LTT-GAN/)]

**Style Generator Inversion for Image Enhancement and Animation.**<br>
*[Aviv Gabbay](http://www.cs.huji.ac.il/~avivga), [Yedid Hoshen](http://www.cs.huji.ac.il/~ydidh).*<br>
arxiv 2019. [[PDF](https://arxiv.org/abs/1906.11880)] [[Project](http://www.vision.huji.ac.il/style-image-prior/)] [[Github](https://github.com/avivga/style-image-prior)]

### image understanding

**Segmentation in Style: Unsupervised Semantic Image Segmentation with Stylegan and CLIP.**<br>
*Daniil Pakhomov, Sanchit Hira, Narayani Wagle, Kemar E. Green, Nassir Navab.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2107.12518.pdf)] [[Project](https://segmentation-in-style.github.io/)] [[Github](https://github.com/warmspringwinds/segmentation_in_style)]

**Finding an Unsupervised Image Segmenter in each of your Deep Generative Models.**<br> 
*Luke Melas-Kyriazi, Christian Rupprecht, Iro Laina, Andrea Vedaldi.*<br>
ICLR 2022. [[PDF](https://openreview.net/forum?id=Ug-bgjgSlKV)]

**Labels4Free: Unsupervised Segmentation using StyleGAN.**<br>
*[Rameen Abdal](https://scholar.google.com/citations?user=kEQimk0AAAAJ&hl=en), [Peihao Zhu](https://scholar.google.com/citations?user=Gn8URq0AAAAJ&hl=en), [Niloy Mitra](http://www0.cs.ucl.ac.uk/staff/n.mitra/), [Peter Wonka](http://peterwonka.net/).*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2103.14968)] [[Project](https://rameenabdal.github.io/Labels4Free)] [[Github](https://github.com/RameenAbdal/Labels4Free)]

**DatasetGAN: Efficient Labeled Data Factory with Minimal Human Effort.**<br>
*[Yuxuan Zhang](https://www.alexyuxuanzhang.com/), [Huan Ling](http://www.cs.toronto.edu/~linghuan/), [Jun Gao](http://www.cs.toronto.edu/~jungao/), [Kangxue Yin](https://kangxue.org/), [Jean-Francois Lafleche](), [Adela Barriuso](), [Antonio Torralba](https://groups.csail.mit.edu/vision/torralbalab/), [Sanja Fidler](http://www.cs.utoronto.ca/~fidler/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.06490)] [[Github](https://github.com/nv-tlabs/datasetGAN_release)] [[Project](https://nv-tlabs.github.io/datasetGAN/)]

**Repurposing GANs for One-shot Semantic Part Segmentation.**<br>
*Nontawat Tritrong, Pitchaporn Rewatbowornwong, [Supasorn Suwajanakorn](https://www.supasorn.com/).*<br>
CVPR 2021 (oral). [[PDF](https://arxiv.org/abs/2103.04379)] [[Project](https://repurposegans.github.io/)] [[Github](https://github.com/bryandlee/repurpose-gan)]

### 3D

**Monocular 3D Object Reconstruction with GAN Inversion.**<br>
*Junzhe Zhang, Daxuan Ren, Zhongang Cai, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2207.10061)] [[Project](https://www.mmlab-ntu.com/project/meshinversion/)] [[Github](https://github.com/junzhezhang/mesh-inversion)]

**StylePart: Image-based Shape Part Manipulation.**<br>
*I-Chao Shen, Li-Wen Su, Yu-Ting Wu, Bing-Yu Chen.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2111.10520)]

**CoordGAN: Self-Supervised Dense Correspondences Emerge from GANs.**<br>
*[Jiteng Mu](https://jitengmu.github.io/), Shalini De Mello, Zhiding Yu, Nuno Vasconcelos, Xiaolong Wang, Jan Kautz, Sifei Liu.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.16521)] [[Project](https://jitengmu.github.io/CoordGAN/)]

**GAN2Shape: Do 2D GANs Know 3D Shape? Unsupervised 3D shape reconstruction from 2D Image GANs.**<br>
*[Xingang Pan](https://xingangpan.github.io/), Bo Dai, Ziwei Liu, Chen Change Loy, Ping Luo.*<br>
ICLR 2021 (oral). [[PDF](https://arxiv.org/abs/2011.00844)] [[Github](https://github.com/XingangPan/GAN2Shape)] [[Project](https://xingangpan.github.io/projects/GAN2Shape.html)]

**Normalized Avatar Synthesis Using StyleGAN and Perceptual Refinement.**<br>
*Huiwen Luo, Koki Nagano, Han-Wei Kung, Mclean Goldwhite, [Qingguo Xu](https://qingguo-xu.com/), Zejian Wang, Lingyu Wei, Liwen Hu, Hao Li.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2106.11423)]

**Unsupervised 3D Shape Completion through GAN-Inversion.**<br>
*[Junzhe Zhang](https://junzhezhang.github.io/), Xinyi Chen, Zhongang Cai, Liang Pan, Haiyu Zhao, Shuai Yi, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2104.13366)] [[Project](https://junzhezhang.github.io/projects/ShapeInversion/)]

**OSTeC: One-Shot Texture Completion.**<br>
*Baris Gecer, Jiankang Deng, Stefanos Zafeiriou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.15370)] [[Github](https://github.com/barisgecer/OSTeC)]

### compressed sensing

**Generator Surgery for Compressed Sensing.**<br>
*Niklas Smedemark-Margulies, Jung Yeon Park, Max Daniels, Rose Yu, Jan-Willem van de Meent, Paul Hand.*<br>
NeurIPS 2020 Workshop Deep Inverse. [[PDF](https://arxiv.org/abs/2102.11163)] [[Github](https://github.com/nik-sm/generator-surgery)]

**Task-Aware Compressed Sensing with Generative Adversarial Networks.**<br>
*Maya Kabkab, Pouya Samangouei, Rama Chellappa.*<br>
AAAI 2018. [[PDF](https://arxiv.org/pdf/1802.01284.pdf)]

### medical imaging

**Controllable Medical Image Generation via Generative Adversarial Networks.**<br>
*Zhihang Ren, Stella X. Yu, David Whitney.*<br>
Human Vision and Electronic Imaging 2021. [[PDF](https://whitneylab.berkeley.edu/PDFs/Ren_MedImageGen.pdf)]

**High-resolution Controllable Prostatic Histology Synthesis using StyleGAN.**<br>
*Gagandeep B. Daroach, Josiah A. Yoder, Kenneth A. Iczkowski, Peter S. LaViolette.*<br>
BIOIMAGING 2021. [[PDF](https://www.scitepress.org/Papers/2021/103939/103939.pdf)]

### compression, fairness, and security

**FairStyle: Debiasing StyleGAN2 with Style Channel Manipulations.**<br>
*Cemre Karakas, Alara Dirik, Eylul Yalcinkaya, Pinar Yanardag.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2202.06240)] [[Project](https://catlab-team.github.io/fairstyle/)] [[Code](https://drive.google.com/drive/folders/1PW7w80ZKuLnjnxJNeNkYxXUFvVYi6I6H?usp=sharing)]

**Video Coding Using Learned Latent GAN Compression.**<br>
*Mustafa Shukor, Bharath Bhushan Damodaran, Xu Yao, Pierre Hellier.*<br>
ACM Multimedia 2022. [[PDF](https://arxiv.org/abs/2207.04324)]

**Differentially Private Imaging via Latent Space Manipulation.**<br>
*Tao Li, Chris Clifton.*<br>
IEEE Symposium on Security & Privacy (S&P) 2021. [[PDF](https://arxiv.org/abs/2103.05472)]

## acknowledgement

Thanks for the constructive comments from anonymous reviewers and feedback from [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Andrey Voynov](https://github.com/anvoynov), and [Rushil Anirudh](https://rushila.com/).

If you find this repo or our paper is helpful for your research, please consider to cite:

```bibtex
@article{xia2022gan,
    author  = {Xia, Weihao and Zhang, Yulun and Yang, Yujiu and Xue, Jing-Hao and Zhou, Bolei and Yang, Ming-Hsuan},
    title   = {GAN Inversion: A Survey},
    journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)},
    year={2022}
  }
```
<p width="100%" align="right"><a href="#">🔝</a></p>
