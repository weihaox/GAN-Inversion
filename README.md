<!-- # <p align=center>`awesome gan-inversion`</p> -->
<!-- [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)  -->
<!-- ![visitors](https://visitor-badge.glitch.me/badge?style=flat-square&page_id=weihaox/awesome-gan-inversion) -->
<!-- <br/> -->

<p align="center">
  <h1 align="center">GAN Inversion: A Survey</h1>
  <p align="center">
    TPAMI 2022
    <br />
    <a href="https://weihaox.github.io/"><strong>Weihao Xia</strong></a>
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
      <img src='https://img.shields.io/badge/Paper-PDF-green?style=flat&logo=arxiv&logoColor=green' alt='arxiv PDF'>
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

This repo is a collection of resources on GAN inversion, as a supplement for our [survey](https://arxiv.org/abs/2101.05278).  If you find any work missing or have any suggestions (papers, implementations and other resources), feel free to [pull requests](https://github.com/weihaox/awesome-gan-inversion/pulls). You could manually edit items or use the [script](https://github.com/weihaox/arxiv_daily_tools) to produce them in the markdown format.

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

- [Inverted Pretrained Models](#inverted-pretrained-models)
  * [2D GANs](#2d-gans)
  * [3D GANs](#3d-aware-gans)
- [GAN Inversion Methods](#gan-inversion-methods)
  * [3D GAN Inversion](#3d-gan-inverson)
  * [2D GAN Inversion](#2d-gan-inversion)
- [Diffusion Inversion](#diffusion-inversion)
- [GAN Latent Space Editing](#gan-latent-space-editing)
- [Diffusion Latent Space Editing](#diffusion-latent-space-editing)
- [Applications](#applications)
  * [Image and Video Generation and Manipulation](#image-and-video-generation-and-manipulation)
  * [Image Restoration](#image-restoration)
  * [Image Understanding](#image-understanding)
  * [Face Recognition](#face-recognition)
  * [3D Reconstruction](#3d-reconstruction)
  * [Other Applications](#other-applications)
    + [Compressed Sensing](#compressed-sensing)
    + [Medical Imaging](#medical-imaging)
    + [Compression, Fairness, and Security](#compression--fairness--and-security)
- [Acknowledgement](#acknowledgement)
</p></details><p></p>

## Inverted Pretrained Models

### 2D GANs

**Scaling up GANs for Text-to-Image Synthesis.**<br>
*[Minguk Kang](https://mingukkang.github.io/), [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Richard Zhang](https://richzhang.github.io/), [Jaesik Park](https://jaesik.info/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Sylvain Paris](https://research.adobe.com/person/sylvain-paris/), [Taesung Park](https://taesung.me/).*<br>
CVPR 2023 (Highlight). [[PDF](https://arxiv.org/abs/2303.05511)] [[Project](https://mingukkang.github.io/GigaGAN/)]

**StyleGAN-T: Unlocking the Power of GANs for Fast Large-Scale Text-to-Image Synthesis.**<br>
*[Axel Sauer](https://axelsauer.com/), [Tero Karras](https://research.nvidia.com/person/tero-karras), [Samuli Laine](https://research.nvidia.com/person/samuli-laine), [Andreas Geiger](https://www.cvlibs.net/), [Timo Aila](https://research.nvidia.com/person/timo-aila).*<br>
ICML 2023. [[Project](https://sites.google.com/view/stylegan-t/)]    [[PDF](https://arxiv.org/abs/2301.09515)]   [[Code](https://github.com/autonomousvision/stylegan-t)]

**StyleGAN-XL: Scaling StyleGAN to Large Diverse Datasets.**<br>
*[Axel Sauer](https://axelsauer.com/), [Katja Schwarz](https://katjaschwarz.github.io/), [Andreas Geiger](http://www.cvlibs.net/).*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2202.00273)] [[Project](https://sites.google.com/view/stylegan-xl/)] [[Code](https://github.com/autonomousvision/stylegan_xl)]

**Self-Distilled StyleGAN: Towards Generation from Internet Photos.**<br>
*[Ron Mokady](https://rmokady.github.io/), Michal Yarom, Omer Tov, Oran Lang, Daniel Cohen-Or, Tali Dekel, Michal Irani, Inbar Mosseri.*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2202.12211)] [[Project](https://self-distilled-stylegan.github.io/)] [[Code](https://github.com/self-distilled-stylegan/self-distilled-internet-photos)]

**Ensembling Off-the-shelf Models for GAN Training.**<br>
[Nupur Kumari](https://nupurkmr9.github.io/), [Richard Zhang](https://richzhang.github.io/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/)<br>
CVPR 2022. [[PDF](https://arxiv.org/pdf/2112.09130.pdf)] [[Project](https://www.cs.cmu.edu/~vision-aided-gan/)] [[Code](https://github.com/nupurkmr9/vision-aided-gan)]

**StyleGAN3: Alias-Free Generative Adversarial Networks.**<br>
*Tero Karras, Miika Aittala, Samuli Laine, Erik Härkönen, Janne Hellsten, Jaakko Lehtinen, Timo Aila.*<br>
NeurIPS 2021. [[PDF](https://arxiv.org/abs/2106.12423)] [[Project](https://nvlabs.github.io/alias-free-gan)] [[Code](https://github.com/NVlabs/stylegan3)] [[Rosinality](https://github.com/rosinality/alias-free-gan-pytorch)]

**StyleGAN2-Ada: Training Generative Adversarial Networks with Limited Data.**<br>
*Tero Karras, Miika Aittala, Janne Hellsten, Samuli Laine, Jaakko Lehtinen, Timo Aila.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2006.06676)] [[Code](https://github.com/NVlabs/stylegan2-ada)] [[Steam StyleGAN2-ADA](https://github.com/woctezuma/steam-stylegan2-ada)]

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

Please check our 3D-aware image synthesis [survey](https://arxiv.org/abs/2210.14267), [paper list](https://github.com/weihaox/3D-aware-Gen), and [project](https://weihaox.github.io/3D-aware-Gen/) for more details. 

**EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks.**<br>
*[Eric R. Chan](https://ericryanchan.github.io/), [Connor Z. Lin](https://connorzlin.com/), [Matthew A. Chan](https://matthew-a-chan.github.io/), [Koki Nagano](https://luminohope.org/), [Boxiao Pan](https://cs.stanford.edu/~bxpan/), [Shalini De Mello](https://research.nvidia.com/person/shalini-gupta), [Orazio Gallo](https://oraziogallo.github.io/), [Leonidas Guibas](https://geometry.stanford.edu/member/guibas/), [Jonathan Tremblay](https://research.nvidia.com/person/jonathan-tremblay), [Sameh Khamis](https://www.samehkhamis.com/), [Tero Karras](https://research.nvidia.com/person/tero-karras), [Gordon Wetzstein](https://stanford.edu/~gordonwz/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.07945)] [[Project](https://matthew-a-chan.github.io/EG3D)] [[Code](https://github.com/NVlabs/eg3d)]

**StyleSDF: High-Resolution 3D-Consistent Image and Geometry Generation.**<br>
*[Roy Or-El](https://homes.cs.washington.edu/~royorel/), [Xuan Luo](https://roxanneluo.github.io/), Mengyi Shan, Eli Shechtman, Jeong Joon Park, Ira Kemelmacher-Shlizerman.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.11427)] [[Project](https://stylesdf.github.io/)] [[Code](https://github.com/royorel/StyleSDF)]

**StyleNeRF: A Style-based 3D-Aware Generator for High-resolution Image Synthesis.**<br>
*[Jiatao Gu](http://jiataogu.me/), [Lingjie Liu](https://lingjie0206.github.io/), [Peng Wang](https://totoro97.github.io/about.html), [Christian Theobalt](http://people.mpi-inf.mpg.de/~theobalt/).*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2110.08985)] [[Project](http://jiataogu.me/style_nerf/)]

**pi-GAN: Periodic Implicit Generative Adversarial Networks for 3D-Aware Image Synthesis.**<br>
*[Eric R. Chan](https://ericryanchan.github.io/), [Marco Monteiro](https://marcoamonteiro.github.io/pi-GAN-website/), [Petr Kellnhofer](https://kellnhofer.xyz/), [Jiajun Wu](https://jiajunwu.com/), [Gordon Wetzstein](https://stanford.edu/~gordonwz/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.00926)] [[Project](https://marcoamonteiro.github.io/pi-GAN-website/)] [[Code](https://github.com/lucidrains/pi-GAN-pytorch)]

## GAN Inversion Methods

The section primarily encompasses general-purpose 2D or 3D inversion techniques, whereas the methods presented in the following section cater to particular applications.

### 3D GAN Inversion

**TriPlaneNet: An Encoder for EG3D Inversion.**<br>
*Ananta R. Bhattarai, Matthias Nießner, Artem Sevastopolsky.*<br> 
WACV 2024. [[PDF](https://arxiv.org/abs/2303.13497)] [[Project](https://anantarb.github.io/triplanenet)]

**In-N-Out: Faithful 3D GAN Inversion with Volumetric Decomposition for Face Editing.**<br>
*[Yiran Xu](https://twizwei.github.io/), [Zhixin Shu](https://zhixinshu.github.io/), [Cameron Smith](https://research.adobe.com/person/cameron-smith/), [Jia-Bin Huang](https://jbhuang0604.github.io/), [Seoung Wug Oh]().*<br> 
CVPR 2024. [[PDF](https://arxiv.org/abs/2302.04871)] [[Project](https://in-n-out-3d.github.io/)]

**Make Encoder Great Again in 3D GAN Inversion through Geometry and Occlusion-Aware Encoding.**<br>
*Ziyang Yuan, Yiming Zhu, Yu Li, Hongyu Liu, Chun Yuan.*<br> 
ICCV 2023. [[PDF](https://arxiv.org/abs/2303.12326)] [[Project](https://eg3d-goae.github.io/)] [[Code](https://github.com/jiangyzy/GOAE)]

**LatentSwap3D: Semantic Edits on 3D Image GANs.**<br>
*Enis Simsar, Alessio Tonioni, Evin Pınar Örnek, Federico Tombari.*<br> 
ICCV 2023 Workshops on AI3DCC. [[PDF](https://arxiv.org/abs/2212.01381)] [[Code](https://github.com/enisimsar/latentswap3d)]

**High-fidelity 3D GAN Inversion by Pseudo-multi-view Optimization.**<br>
*[Jiaxin Xie](https://jiaxinxie97.github.io/Jiaxin-Xie/), [Hao Ouyang](https://ken-ouyang.github.io/), [Jingtan Piao](https://ken-ouyang.github.io/HFGI3D/index.html), [Chenyang Lei](https://chenyanglei.github.io/), [Qifeng Chen](https://cqf.io/).*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.15662)] [[Project](https://ken-ouyang.github.io/HFGI3D/index.html)] [[Code](https://github.com/jiaxinxie97/HFGI3D/)]

**Learning Detailed Radiance Manifolds for High-Fidelity and 3D-Consistent Portrait Synthesis from Monocular Image.**<br>
*Yu Deng, Baoyuan Wang, Heung-Yeung Shum.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.13901)] [[Project](https://yudeng.github.io/GRAMInverter/)]

**E3DGE: Self-Supervised Geometry-Aware Encoder for Style-based 3D GAN Inversion.**<br>
*Yushi Lan, Xuyi Meng, Shuai Yang, Chen Change Loy, Bo Dai.*<br> 
CVPR 2023. [[PDF](https://arxiv.org/abs/2212.07409)]
[[Project](https://nirvanalan.github.io/projects/E3DGE/index.html)]
[[Code](https://github.com/NIRVANALAN/E3DGE)]

**3D GAN Inversion with Pose Optimization.**<br>
*[Jaehoon Ko](https://scholar.google.com/citations?view_op=list_works&hl=en&user=ySBl-10AAAAJ), [Kyusun Cho](https://scholar.google.com/citations?user=ToQ-jEIAAAAJ&hl=en&oi=ao), [Daewon Choi](https://github.com/ChoiDae1), [Kwangrok Ryoo](https://cvlab.korea.ac.kr/members), [Seungryong Kim](https://cvlab.korea.ac.kr/members).*<br>
WACV 2023. [[PDF](https://arxiv.org/abs/2210.07301)] [[Project](https://3dgan-inversion.github.io/)] [[Code](https://github.com/KU-CVLAB/3DGAN-Inversion)]

**3D GAN Inversion for Controllable Portrait Image Animation.**<br>
*[Connor Z. Lin](https://connorzlin.com/), David B. Lindell, Eric R. Chan, [Gordon Wetzstein](https://stanford.edu/~gordonwz/).*<br>
ECCV 2022 Workshop on [Learn3DG](https://learn3dg.github.io/). [[PDF](https://arxiv.org/abs/2203.13441)] [[Project](https://www.computationalimaging.org/publications/3dganinversion/)]

**Pix2NeRF: Unsupervised Conditional π-GAN for Single Image to Neural Radiance Fields Translation.**<br>
*Shengqu Cai, Anton Obukhov, Dengxin Dai, Luc Van Gool.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2202.13162)]

### 2D GAN Inversion

**StyleRes: Transforming the Residuals for Real Image Editing with StyleGAN.**<br>
*Hamza Pehlivan, Yusuf Dalva, Aysegul Dundar.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2212.14359)] [[Code](https://github.com/hamzapehlivan/StyleRes)]

**ReGANIE: Rectifying GAN Inversion Errors for Accurate Real Image Editing.**<br>
*[Bingchuan Li](https://tianxiangma.github.io/), Tianxiang Ma, Peng Zhang, Miao Hua, Wei Liu, Qian He, Zili Yi.*<br>
AAAI 2023. [[PDF](https://arxiv.org/abs/2301.13402)]

**Intra-Source Style Augmentation for Improved Domain Generalization.**<br>
*Yumeng Li, Dan Zhang, Margret Keuper, Anna Khoreva.*<br>
WACV 2023. [[PDF](https://arxiv.org/pdf/2210.10175.pdf)] [[Code](https://github.com/boschresearch/ISSA)]

**Pivotal Tuning for Latent-based Editing of Real Images.**<br>
*Daniel Roich, Ron Mokady, Amit H. Bermano, Daniel Cohen-Or.*<br>
TOG 2022. [[PDF](https://arxiv.org/pdf/2106.05744.pdf)] [[Code](https://github.com/danielroich/PTI)]

**E2Style: Improve the Efficiency and Effectiveness of StyleGAN Inversion.**<br> 
*Tianyi Wei, Dongdong Chen, Wenbo Zhou, Jing Liao, Weiming Zhang, Lu Yuan, Gang Hua, Nenghai Yu.*<br> 
TIP 2022. [[PDF](https://arxiv.org/abs/2104.07661)] [[Project](https://wty-ustc.github.io/inversion/)] [[Code](https://github.com/wty-ustc/e2style)]

**High-fidelity GAN Inversion with Padding Space.**<br>
*[Qingyan Bai](https://ezioby.github.io/padinv/), Yinghao Xu, Jiapeng Zhu, Weihao Xia, Yujiu Yang, Yujun Shen.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2203.11105)] [[Project](https://github.com/EzioBy/padinv)] [[Code](https://github.com/EzioBy/padinv)]

**Editing Out-of-Domain GAN Inversion via Differential Activations.**<br>
*Haorui Song, Yong Du, Tianyi Xiang, Junyu Dong, Jing Qin, Shengfeng He.*<br>
ECCV 2022. [[PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/5504_ECCV_2022_paper.php)] [[Code](https://github.com/HaoruiSong622/Editing-Out-of-Domain)]

**IntereStyle: Encoding an Interest Region for Robust StyleGAN Inversion.**<br>
*Seungjun Moon, GyeongMoon Park.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2209.10811)] 

**Chunkmogrify: Real image inversion via Segments.**<br>
*[David Futschik](https://dcgi.fel.cvut.cz/people/futscdav), [Michal Lukáč](https://research.adobe.com/person/michal-lukac/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Daniel Sýkora](https://dcgi.fel.cvut.cz/home/sykorad/).*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2110.06269)] [[Code](https://github.com/futscdav/Chunkmogrify)]

**A Style-Based GAN Encoder for High Fidelity Reconstruction of Images and Videos.**<br>
*Xu Yao, Alasdair Newson, Yann Gousseau, Pierre Hellier.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2202.02183)] [[Code](https://github.com/InterDigitalInc/FeatureStyleEncoder)]

**Cycle Encoding of a StyleGAN Encoder for Improved Reconstruction and Editability.**<br>
*Xudong Mao, Liujuan Cao, Aurele Tohokantche Gnanha, Zhenguo Yang, Qing Li, Rongrong Ji.*<br>
ACM MM 2022. [[PDF](https://arxiv.org/abs/2207.09367)] [[Code](https://github.com/xudonmao/CycleEncoding)]

**Spatially-Adaptive Multilayer Selection for GAN Inversion and Editing.**<br>
*[Gaurav Parmar](https://gauravparmar.com/), [Yijun Li](https://yijunmaverick.github.io/), [Jingwan Lu](https://research.adobe.com/person/jingwan-lu/), [Richard Zhang](http://richzhang.github.io/), [Jun-Yan Zhu](https://www.cs.cmu.edu/~junyanz/), [Krishna Kumar Singh](http://krsingh.cs.ucdavis.edu/).*<br>
CVPR 2022. [[PDF](https://openaccess.thecvf.com/content/CVPR2022/papers/Parmar_Spatially-Adaptive_Multilayer_Selection_for_GAN_Inversion_and_Editing_CVPR_2022_paper.pdf)] [[Project](https://www.cs.cmu.edu/~SAMInversion)] [[Code](https://github.com/adobe-research/sam_inversion)]

**Style Transformer for Image Inversion and Editing.**<br>
*Xueqi Hu, Qiusheng Huang, Zhengyi Shi, Siyuan Li, Changxin Gao, Li Sun, Qingli Li.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.07932)] [[Code](https://github.com/sapphire497/style-transformer)]

**High-Fidelity GAN Inversion for Image Attribute Editing.**<br>
*[Tengfei Wang](https://tengfei-wang.github.io), Yong Zhang, Yanbo Fan, Jue Wang, Qifeng Chen.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2109.06590)] [[Project](https://tengfei-wang.github.io/HFGI/)] [[Code](https://github.com/Tengfei-Wang/HFGI)]

**HyperInverter: Improving StyleGAN Inversion via Hypernetwork.**<br>
*[Tan M. Dinh](https://di-mi-ta.github.io/), [Anh Tuan Tran](https://sites.google.com/site/anhttranusc/), [Rang Nguyen](https://sites.google.com/site/rangmanhonguyen/), [Binh-Son Hua](https://sonhua.github.io/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.00719)] [[Project](https://di-mi-ta.github.io/HyperInverter/)]

**HyperStyle: StyleGAN Inversion with HyperNetworks for Real Image Editing.**<br>
*Yuval Alaluf, Omer Tov, Ron Mokady, Rinon Gal, Amit H. Bermano.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2111.15666)] [[Project](http://yuval-alaluf.github.io/hyperstyle/)] [[Code](https://github.com/yuval-alaluf/hyperstyle)]

**Overparameterization Improves StyleGAN Inversion.**<br>
*Yohan Poirier-Ginter, Alexandre Lessard, Ryan Smith, Jean-François Lalonde.*<br>
CVPR 2022 Workshop on AI for Content Creation. [[PDF](https://arxiv.org/abs/2205.06304)] [[Code](https://lvsn.github.io/OverparamStyleGAN/)]

**StyleAlign: Analysis and Applications of Aligned StyleGAN Models.**<br>
*Zongze Wu, Yotam Nitzan, Eli Shechtman, Dani Lischinski.*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2110.11323)]

**GAN-Control: Explicitly Controllable GANs.**<br>
*Alon Shoshan, Nadav Bhonker, Igor Kviatkovsky, Gerard Medioni.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2101.02477)]

**From Continuity to Editability: Inverting GANs with Consecutive Images.**<br>
*[Yangyang Xu](https://cnnlstm.github.io/), [Yong Du](https://www.csyongdu.com/), Wenpeng Xiao, Xuemiao Xu and [Shengfeng He](hengfenghe.com).*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2107.13812)] [[Code](https://github.com/Qingyang-Xu/InvertingGANs_with_ConsecutiveImgs)]

**Explaining in Style: Training a GAN to explain a classifier in StyleSpace.**<br> 
*Oran Lang, Yossi Gandelsman, Michal Yarom, Yoav Wald, Gal Elidan, Avinatan Hassidim, William T. Freeman, Phillip Isola, Amir Globerson, Michal Irani, Inbar Mosseri.*<br> 
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.13369)] [[Project](https://explaining-in-style.github.io/)]

**BDInvert: GAN Inversion for Out-of-Range Images with Geometric Transformations.**<br>
*[Kyoungkook Kang](https://kkang831.github.io/), Seongtae Kim, [Sunghyun Cho](https://www.scho.pe.kr/).*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2108.08998)] [[Project](https://kkang831.github.io/publication/ICCV_2021_BDInvert/)]

**ReStyle: A Residual-Based StyleGAN Encoder via Iterative Refinement.**<br> 
*[Yuval Alaluf](https://yuval-alaluf.github.io/), [Or Patashnik](https://orpatashnik.github.io/), [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br> 
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.02699)] [[Project](https://yuval-alaluf.github.io/restyle-encoder/)] [[Code](https://github.com/yuval-alaluf/restyle-encoder)]

**LatentCLR: A Contrastive Learning Approach for Unsupervised Discovery of Interpretable Directions.**<br> 
*Oğuz Kaan Yüksel, [Enis Simsar](https://enis.dev), Ezgi Gülperi Er, Pinar Yanardag.*<br> 
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.00820)] [[Code](https://github.com/catlab-team/latentclr)]

**Lifting 2D StyleGAN for 3D-Aware Face Generation.**<br>
*[Yichun Shi](https://seasonsh.github.io/), Divyansh Aggarwal, [Anil K. Jain](http://www.cse.msu.edu/~jain/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.13126)]

**Ensembling with Deep Generative Views.**<br> 
*Lucy Chai, Jun-Yan Zhu, Eli Shechtman, Phillip Isola, Richard Zhang.*<br> 
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.14551)] [[Code](https://github.com/chail/gan-ensembling)] [[Project](https://chail.github.io/gan-ensembling/)]

**Navigating the GAN Parameter Space for Semantic Image Editing.**<br>
*Anton Cherepkov, Andrey Voynov, Artem Babenko.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.13786)] [[Code](https://github.com/yandex-research/navigan)]

**StyleSpace Analysis: Disentangled Controls for StyleGAN Image Generation.**<br>
*Zongze Wu, Dani Lischinski, Eli Shechtman.*<br>
CVPR 2021 (oral). [[PDF]](https://arxiv.org/abs/2011.12799) [[Code](https://github.com/betterze/StyleSpace)]

**Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation.**<br>
*Elad Richardson, Yuval Alaluf, Or Patashnik, Yotam Nitzan, Yaniv Azar, Stav Shapiro, Daniel Cohen-Or.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2008.00951)] [[Code](https://github.com/eladrich/pixel2style2pixel)] [[Project](eladrich.github.io/pixel2style2pixel/)]

**GHFeat: Generative Hierarchical Features from Synthesizing Images.**<br>
*Yinghao Xu, Yujun Shen, Jiapeng Zhu, Ceyuan Yang, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2007.10379.pdf)] [[Code](https://github.com/genforce/ghfeat)] [[Project](https://genforce.github.io/ghfeat/)]

**Hijack-GAN: Unintended-Use of Pretrained, Black-Box GANs.**<br>
*Hui-Po Wang, Ning Yu, Mario Fritz.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.14107)]

**Prior Image-Constrained Reconstruction using Style-Based Generative Models.**<br> 
*Varun A Kelkar, Mark Anastasio.*<br>
ICML 2021. [[PDF](https://arxiv.org/pdf/2102.12525.pdf)]

**Intermediate Layer Optimization for Inverse Problems using Deep Generative Models.**<br>
*Giannis Daras, Joseph Dean, Ajil Jalal, Alexandros G. Dimakis.*<br>
ICML 2021. [[PDF](https://arxiv.org/abs/2102.07364)] [[Code](https://github.com/giannisdaras/ilo)]

**Using Latent Space Regression to Analyze and Leverage Compositionality in GANs.**<br> 
*[Lucy Chai](http://people.csail.mit.edu/lrchai/), [Jonas Wulff](http://people.csail.mit.edu/jwulff/), [Phillip Isola](http://web.mit.edu/phillipi/).*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=sjuuTm4vj0)] [[Code](https://github.com/chail/latent-composition)] [[Project](https://chail.github.io/latent-composition/)] [[Colab](https://colab.research.google.com/drive/1p-L2dPMaqMyr56TYoYmBJhoyIyBJ7lzH?usp=sharing)]

**Enjoy Your Editing: Controllable GANs for Image Editing via Latent Space Navigation.**<br>
*Peiye Zhuang, Oluwasanmi Koyejo, Alexander G. Schwing.*<br>
ICLR 2021. [[PDF](https://arxiv.org/abs/2102.01187)]

**Disentangled Face Attribute Editing via Instance-Aware Latent Space Search.**<br>
*Yuxuan Han, [Jiaolong Yang](http://jlyang.org/), Ying Fu.*<br>
IJCAI 2021. [[PDF](https://arxiv.org/abs/2105.12660)] [[Code](https://github.com/yxuhan/IALS)]

**High Fidelity GAN Inversion via Prior Multi-Subspace Feature Composition.**<br> 
*Guanyue Li, Qianfen Jiao, Sheng Qian, Si Wu, Hau-San Wong.*<br> 
AAAI 2021. [[PDF](https://ojs.aaai.org/index.php/AAAI/article/view/17017)]

**e4e: Designing an Encoder for StyleGAN Image Manipulation.**<br>
*[Omer Tov](https://yotamnitzan.github.io/), Yuval Alaluf, Yotam Nitzan, Or Patashnik, Daniel Cohen-Or.*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2102.02766)] [[Code](https://github.com/omertov/encoder4editing)]

**StyleFlow: Attribute-conditioned Exploration of StyleGAN-Generated Images using Conditional Continuous Normalizing Flows.**<br>
*Rameen Abdal, Peihao Zhu, Niloy Mitra, Peter Wonka.*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2008.02401)] [[Code](https://rameenabdal.github.io/StyleFlow)]

**PIE: Portrait Image Embedding for Semantic Control.**<br> 
*[A. Tewari](http://people.mpi-inf.mpg.de/~atewari/), M. Elgharib, M. BR, F. Bernard, H-P. Seidel, P. P‌érez, M. Zollhöfer, C.Theobalt.*<br>
TOG 2020. [[PDF](http://gvv.mpi-inf.mpg.de/projects/PIE/data/paper.pdf)] [[Project](http://gvv.mpi-inf.mpg.de/projects/PIE/)]

**Face Identity Disentanglement via Latent Space Mapping.**<br>
*[Yotam Nitzan](https://yotamnitzan.github.io/), [Amit Bermano](https://www.cs.tau.ac.il/~amberman/), [Yangyan Li](https://yangyan.li/), Daniel Cohen-Or.*<br>
SIGGRAPH Asia 2020. [[PDF](https://arxiv.org/abs/2005.07728)] [[Project](https://yotamnitzan.github.io/ID-disentanglement/)] [[Code](https://github.com/YotamNitzan/ID-disentanglement)]

**Understanding the Role of Individual Units in a Deep Neural Network.**<br>
*David Bau, Jun-Yan Zhu, Hendrik Strobelt, Agata Lapedriza, Bolei Zhou, Antonio Torralba.*<br>
National Academy of Sciences 2020. [[PDF](https://arxiv.org/abs/2009.05041)] [[Code](https://github.com/davidbau/dissect/)] [[Project](https://dissect.csail.mit.edu/)]

**Face Identity Disentanglement via Latent Space Mapping.**<br>
*Yotam Nitzan, Amit Bermano, Yangyan Li, Daniel Cohen-Or.*<br>
TOG 2020. [[PDF](https://arxiv.org/abs/2005.07728)] [[Code](https://github.com/YotamNitzan/ID-disentanglement)]

**Transforming and Projecting Images into Class-conditional Generative Networks.**<br>
*[Minyoung Huh](http://minyounghuh.com/), [Richard Zhang](https://richzhang.github.io/), [Jun-Yan Zhu](https://people.csail.mit.edu/junyanz/), [Sylvain Paris](http://people.csail.mit.edu/sparis/), [Aaron Hertzmann](https://www.dgp.toronto.edu/~hertzman/).*<br>
ECCV 2020. [[PDF](http://arxiv.org/abs/2005.01703)] [[Code](https://github.com/minyoungg/GAN-Transform-and-Project)] [[Project](https://minyoungg.github.io/GAN-Transform-and-Project/)]

**MimicGAN: Robust Projection onto Image Manifolds with Corruption Mimicking.**<br>
*[Rushil Anirudh](https://rushila.com/), [Jayaraman J. Thiagarajan](https://jjthiagarajan.com/), [Bhavya Kailkhura](https://people.llnl.gov/kailkhura1), [Timo Bremer](https://people.llnl.gov/bremer5).*<br>
IJCV 2020. [[PDF](https://link.springer.com/article/10.1007/s11263-020-01310-5)]

**Rewriting a Deep Generative Model.**<br>
*David Bau, Steven Liu, Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2007.15646)] [[Code](https://github.com/davidbau/rewriting)]

**StyleGAN2 Distillation for Feed-forward Image Manipulation.**<br>
*Yuri Viazovetskyi, Vladimir Ivashkin, Evgeny Kashin.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2003.03581)] [[Code](https://github.com/EvgenyKashin/stylegan2-distillation)]

**In-Domain GAN Inversion for Real Image Editing.**<br>
*Jiapeng Zhu, Yujun Shen, Deli Zhao, Bolei Zhou.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2004.00049)] [[Project](https://genforce.github.io/idinvert/)] [[Code](https://github.com/genforce/idinvert)]

**Exploiting Deep Generative Prior for Versatile Image Restoration and Manipulation.**<br>
*Xingang Pan, Xiaohang Zhan, Bo Dai, Dahua Lin, Chen Change Loy, Ping Luo.*<br>
ECCV 2020. [[PDF](https://arxiv.org/abs/2003.13659)] [[Code](https://github.com/XingangPan/deep-generative-prior)]

**Your Local GAN: Designing Two Dimensional Local Attention Mechanisms for Generative Models.**<br>
*Giannis Daras, Augustus Odena, Han Zhang, Alexandros G. Dimakis.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1911.12287)]

**A Disentangling Invertible Interpretation Network for Explaining Latent Representations.**<br>
*Patrick Esser, Robin Rombach, Björn Ommer.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/2004.13166)] [[Project](https://compvis.github.io/iin/)] [[Code](https://github.com/CompVis/iin)]

**Editing in Style: Uncovering the Local Semantics of GANs.**<br>
*Edo Collins, Raja Bala, Bob Price, Sabine Süsstrunk.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/2004.14367)] [[Code](https://github.com/IVRL/GANLocalEditing)]

**Image Processing Using Multi-Code GAN Prior.**<br>
*[Jinjin Gu](http://www.jasongt.com/), Yujun Shen, Bolei Zhou.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1912.07116)] [[Project](https://genforce.github.io/mganprior/)] [[Code](https://github.com/genforce/mganprior)]

**Image2StyleGAN++: How to Edit the Embedded Images?**<br>
*Rameen Abdal, [Yipeng Qin](http://yipengqin.github.io/), Peter Wonka.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1911.11544)]

**Semantic Photo Manipulation with a Generative Image Prior.**<br>
*David Bau, Hendrik Strobelt, William Peebles, Jonas, Bolei Zhou, Jun-Yan Zhu, Antonio Torralba.*<br>
TOG 2019. [[PDF](https://arxiv.org/abs/2005.07727)]

**Image2StyleGAN: How to Embed Images Into the StyleGAN Latent Space?**<br>
*Rameen Abdal, [Yipeng Qin](http://yipengqin.github.io/), Peter Wonka.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1904.03189)] [[Code](https://github.com/RameenAbdal/image2stylegan-v2)]

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
TNNLS 2018. [[PDF](https://arxiv.org/abs/1802.05701)] [[Code](https://github.com/ToniCreswell/InvertingGAN)]

**Invertibility of Convolutional Generative Networks from Partial Measurements.**<br>
*Fangchang Ma, Ulas Ayaz, Sertac Karaman.*<br>
NeurIPS 2018. [[PDF](https://papers.nips.cc/paper/8171-invertibility-of-convolutional-generative-networks-from-partial-measurements)] [[Code](https://github.com/fangchangma/invert-generative-networks)]

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
ICLR 2017 workshop. [[PDF](https://arxiv.org/abs/1702.04782)] [[Code](https://github.com/SubarnaTripathi/ReverseGAN)]

**Inverting The Generator Of A Generative Adversarial Network.**<br>
*Antonia Creswell, Anil Anthony Bharath.*<br>
NeurIPS 2016 Workshop. [[PDF](https://arxiv.org/abs/1611.05644)]

**Generative Visual Manipulation on the Natural Image Manifold.**<br>
*Jun-Yan Zhu, Philipp Krähenbühl, Eli Shechtman, Alexei A. Efros.*<br>
ECCV 2016. [[PDF](https://arxiv.org/abs/1609.03552v2)]

**Improved StyleGAN Embedding: Where Are The Good Latents?.**<br>
*[Peihao Zhu](https://github.com/ZPdesu), [Rameen Abdal](https://github.com/RameenAbdal), [Yipeng Qin](https://scholar.google.com/citations?user=ojgWPpgAAAAJ&hl=en), [John Femiani](https://scholar.google.com/citations?user=rS1xJIIAAAAJ&hl=en), [Peter Wonka](http://peterwonka.net/).*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2012.09036)] [[Code](https://github.com/ZPdesu/II2S)]

**Improving Inversion and Generation Diversity in StyleGAN Using A Gaussianized Latent Space.**<br>
*[Jonas Wulff](http://people.csail.mit.edu/jwulff/), Antonio Torralba.*<br>
arxiv 2020. [[PDF](https://arxiv.org/abs/2009.06529)]

<p width="100%" align="right"><a href="#">🔝</a></p>

## GAN Latent Space Editing

Inversion isn't the ultimate goal; it's a means to enable real image or video editing within a GAN's latent space. Commonly referred to as GAN latent space editing, navigation, traversal, steerability, or other names in the literature, this task, although sometimes seen as a standalone research domain, acts as an indispensable component of GAN inversion based editing. This section is about GAN latent space editing. Recent studies reveal diffusion model can be used for real image and video editing in a similar way. Please refer to [Diffusion Inversion](https://github.com/weihaox/GAN-Inversion#diffusion-inversion) and [Diffusion Latent Space Editing](https://github.com/weihaox/GAN-Inversion/#diffusion-latent-space-editing) for more details.

**Deep Curvilinear Editing: Commutative and Nonlinear Image Manipulation for Pretrained Deep Generative Model.**<br>
*Takehiro Aoshima, Takashi Matsubara.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.14573)]

**Fantastic Style Channels and Where to Find Them: A Submodular Framework for Discovering Diverse Directions in GANs.**<br>
*[Enis Simsar](https://enis.dev/), [Umut Kocasari](https://catlab-team.github.io/), [Ezgi Gülperi Er](https://catlab-team.github.io/), [Pinar Yanardag](https://pinguar.org/).*<br>
WACV 2023. [[PDF](https://arxiv.org/abs/2203.08516)] [[Project](https://catlab-team.github.io/fantasticstyles/)] [[Demo](https://catlab-team.github.io/styleatlas/classes/FFHQ/)]

**Latent Traversals in Generative Models as Potential Flows.**<br>
*Yue Song, Andy Keller, Nicu Sebe, Max Welling.*<br>
ICML 2023. [[PDF](https://arxiv.org/abs/2304.12944)] [[Code](https://github.com/KingJamesSong/PDETraversal)] 

**PandA: Unsupervised Learning of Parts and Appearances in the Feature Maps of GANs.**<br>
*[James Oldfield](http://eecs.qmul.ac.uk/~jo001/), Christos Tzelepis, Yannis Panagakis, Mihalis A. Nicolaou, Ioannis Patras.*<br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2206.00048)] [[Project](http://eecs.qmul.ac.uk/~jo001/PandA/)] [[Code](https://github.com/james-oldfield/PandA)]

**Rayleigh EigenDirections (REDs): GAN Latent Space Traversals for Multidimensional Features.**<br>
*Guha Balakrishnan, Raghudeep Gadde, Aleix Martinez, Pietro Perona.*<br>
ECCV 2022. [[PDF](https://arxiv.org/pdf/2201.10423.pdf)]

**Rayleigh EigenDirections (REDs): Nonlinear GAN Latent Space Traversals for Multidimensional Features.**<br>
*Guha Balakrishnan, Raghudeep Gadde, Aleix Martinez, Pietro Perona.*<br>
ECCV 2022. [[PDF](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/7277_ECCV_2022_paper.php)]

**Exploring Gradient-based Multi-directional Controls in GANs.**<br>
*Zikun Chen, Ruowei Jiang, Brendan Duke, Han Zhao, Parham Aarabi.*<br>
ECCV 2022 (oral). [[PDF](https://arxiv.org/abs/2209.00698)] [[Project](https://github.com/zikuncshelly/GradCtrl)] 

**Hierarchical Semantic Regularization of Latent Spaces in StyleGANs.**<br>
*Tejan Karmali, Rishubh Parihar, Susmit Agrawal, Harsh Rangwani, Varun Jampani, Maneesh Singh, R. Venkatesh Babu.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2208.03764)] [[Project](https://sites.google.com/view/hsr-eccv22/)] 
 
**CLIP2StyleGAN: Unsupervised Extraction of StyleGAN Edit Directions.**<br>
*Rameen Abdal, Peihao Zhu, John Femiani, Niloy J. Mitra, Peter Wonka.*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2112.05219)] [[Code](https://github.com/RameenAbdal/CLIP2StyleGAN)]

**Region-Based Semantic Factorization in GANs.**<br>
*Jiapeng Zhu, Yujun Shen, Yinghao Xu, Deli Zhao, Qifeng Chen.*<br>
ICML 2022. [[PDF](https://arxiv.org/abs/2202.09649)] [[Code](https://github.com/zhujiapeng/resefa)]

**Latent Image Animator: Learning to Animate Image via Latent Space Navigation.**<br>
*Yaohui Wang, Di Yang, Francois Bremond, Antitza Dantcheva.*<br>
ICLR 2022. [[PDF](https://openreview.net/forum?id=7r6kDq0mK_)] [[Project](https://wyhsirius.github.io/LIA-project)] [[Code](https://github.com/wyhsirius/LIA)]

**Do Not Escape From the Manifold: Discovering the Local Coordinates on the Latent Space of GANs.**<br>
*Jaewoong Choi, Changyeon Yoon, Junho Lee, Jung Ho Park, Geonho Hwang, Myungjoo Kang.*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2106.06959)]

**Tensor-based Emotion Editing in the StyleGAN Latent Space.**<br>
*René Haas, Stella Graßhof, Sami S. Brandt.*<br>
CVPR 2022 Workshop on AI for Content Creation. [[PDF](https://arxiv.org/pdf/2205.06102.pdf)]

**PaintInStyle: One-Shot Discovery of Interpretable Directions by Painting.**<br>
*Berkay Doner, Elif Sema Balcioglu, Merve Rabia Barin, Umut Kocasari, Mert Tiftikci, Pinar Yanardag.*<br>
CVPR 2022 Workshop. [[PDF](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/html/Doner_PaintInStyle_One-Shot_Discovery_of_Interpretable_Directions_by_Painting_CVPRW_2022_paper.html)]

**Rank in Style: A Ranking-Based Approach To Find Interpretable Directions.**<br>
*Umut Kocasari, Kerem Zaman, Mert Tiftikci, Enis Simsar, Pinar Yanardag.*<br>
CVPR 2022 Workshop. [[PDF](https://openaccess.thecvf.com/content/CVPR2022W/CVFAD/html/Kocasari_Rank_in_Style_A_Ranking-Based_Approach_To_Find_Interpretable_Directions_CVPRW_2022_paper.html)]

**LARGE: Latent-Based Regression through GAN Semantics.**<br>
*[Yotam Nitzan](https://yotamnitzan.github.io), [Rinon Gal](https://rinongal.github.io/), [Ofir Brenner](https://scholar.google.com/citations?user=iLLlWr8AAAAJ), [Daniel Cohen-Or](https://danielcohenor.com/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2107.11186)] [[Code](https://github.com/YotamNitzan/LARGE)] [[Project](https://yotamnitzan.github.io/LARGE)]

**StyleFusion: Disentangling Spatial Segments in StyleGAN-Generated Images.**<br>
*Omer Kafri, Or Patashnik, Yuval Alaluf, Daniel Cohen-Or.*<br>
TOG 2022. [[PDF](https://arxiv.org/abs/2107.07437)] [[Code](https://github.com/OmerKafri/StyleFusion)]

**Optimizing Latent Space Directions For GAN-based Local Image Editing.**<br>
*Ehsan Pajouheshgar, Tong Zhang, Sabine Süsstrunk.*<br>
ICASSP 2022. [[PDF](https://arxiv.org/abs/2111.12583)]

**Tensor Component Analysis for Interpreting the Latent Space of GANs.**<br>
*[James Oldfield](https://james-oldfield.github.io/), Markos Georgopoulos, Yannis Panagakis, Mihalis A. Nicolaou, Ioannis Patras.*<br>
BMVC 2021. [[PDF](https://arxiv.org/abs/2111.11736)] [[Project](http://eecs.qmul.ac.uk/~jo001/TCA-latent-space/)] [[Code](https://github.com/james-oldfield/TCA-latent-space)]

**Tensor-based Subspace Factorization for StyleGAN.**<br>
*Rene Haas, Stella Graßhof and Sami S. Brandt.*<br>
FG 2021. [[PDF](https://arxiv.org/abs/2111.04554)]

**Exploratory Search of GANs with Contextual Bandits.**<br> 
*Ivan Kropotov, Alan Medlar, Dorota Glowacka.*<br> 
CIKM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3459637.3482103)]

**LowRankGAN: Low-Rank Subspaces in GANs.**<br> 
*Jiapeng Zhu, Ruili Feng, Yujun Shen, Deli Zhao, Zhengjun Zha, Jingren Zhou, Qifeng Chen.*<br> 
NeurIPS 2021. [[PDF](https://arxiv.org/abs/2106.04488)] [[Code](https://github.com/zhujiapeng/LowRankGAN)]

**Controllable and Compositional Generation with Latent-Space Energy-Based Models.**<br>
*Weili Nie, Arash Vahdat, Anima Anandkumar.*<br>
NeurIPS 2021. [[PDF](https://arxiv.org/abs/2110.10873)]

**A Latent Transformer for Disentangled Face Editing in Images and Videos.**<br>
*Xu Yao, Alasdair Newson, Yann Gousseau, Pierre Hellier.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/html/Yao_A_Latent_Transformer_for_Disentangled_Face_Editing_in_Images_and_ICCV_2021_paper.html)] [[arxiv](https://arxiv.org/abs/2106.11895)] [[Code](https://github.com/InterDigitalInc/latent-transformer)]

**Toward a Visual Concept Vocabulary for GAN Latent Space.**<br>
*Sarah Schwettmann, Evan Hernandez, David Bau, Samuel Klein, Jacob Andreas, Antonio Torralba.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/html/Schwettmann_Toward_a_Visual_Concept_Vocabulary_for_GAN_Latent_Space_ICCV_2021_paper.html)] [[Project](https://visualvocab.csail.mit.edu/)]

**WarpedGANSpace: Finding Non-linear RBF Paths in GAN Latent Space.**<br>
*Christos Tzelepis, Georgios Tzimiropoulos, Ioannis Patras.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2109.13357)] [[Code](https://github.com/chi0tzp/WarpedGANSpace)]

**Latent Transformations via NeuralODEs for GAN-based Image Editing.**<br>
*Valentin Khrulkov, Leyla Mirvakhabova, Ivan Oseledets, Artem Babenko.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/papers/Khrulkov_Latent_Transformations_via_NeuralODEs_for_GAN-Based_Image_Editing_ICCV_2021_paper.pdf)] [[Code](https://github.com/KhrulkovV/nonlinear-image-editing)]

**OroJaR: Orthogonal Jacobian Regularization for Unsupervised Disentanglement in Image Generation.**<br>
*Yuxiang Wei, Yupeng Shi, Xiao Liu, Zhilong Ji, Yuan Gao, Zhongqin Wu, Wangmeng Zuo.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2108.07668)] [[Code](https://github.com/csyxwei/OroJaR)]

**EigenGAN: Layer-Wise Eigen-Learning for GANs.**<br>
*Zhenliang He, Meina Kan, Shiguang Shan.*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2104.12476)] [[Code](https://github.com/LynnHo/EigenGAN-Tensorflow)]

**SSFlow: Style-guided Neural Spline Flows for Face Image Manipulation.**<br>
*Hanbang Liang, Xianxu Hou, Linlin Shen.*<br>
ACM MM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3474085.3475454)]

**SalS-GAN: Spatially-Adaptive Latent Space in StyleGAN for Real Image Embedding.**<br>
*Lingyun Zhang, Xiuxiu Bai, Yao Gao.*<br>
ACM MM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3474085.3475633)]

**Discovering Density-Preserving Latent Space Walks in GANs for Semantic Image Transformations.**<br>
*Guanyue Li, Yi Liu, Xiwen Wei, Yang Zhang, Si Wu, Yong Xu, Hau San Wong.*<br>
ACM MM 2021. [[PDF](https://dl.acm.org/doi/abs/10.1145/3474085.3475293)]

**Discovering Interpretable Latent Space Directions of GANs Beyond Binary Attributes.**<br>
*Huiting Yang, Liangyu Chai, Qiang Wen, Shuang Zhao, Zixun Sun, Shengfeng He.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_Discovering_Interpretable_Latent_Space_Directions_of_GANs_Beyond_Binary_Attributes_CVPR_2021_paper.pdf)] [[Code](https://github.com/BERYLSHEEP/AdvStyle)]

**Surrogate Gradient Field for Latent Space Manipulation.**<br>
*Minjun Li, Yanghua Jin, Huachun Zhu.*<br>
CVPR 2021. [[PDF](http://arxiv.org/abs/2104.09065)]

**SeFa: Closed-Form Factorization of Latent Semantics in GANs.**<br>
*Yujun Shen, Bolei Zhou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2007.06600)] [[Code](https://github.com/genforce/sefa)] [[Project](https://genforce.github.io/sefa/)]

**L2M-GAN: Learning To Manipulate Latent Space Semantics for Facial Attribute Editing.**<br>
*Guoxing Yang, Nanyi Fei, Mingyu Ding, Guangzhen Liu, Zhiwu Lu, Tao Xiang.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/html/Yang_L2M-GAN_Learning_To_Manipulate_Latent_Space_Semantics_for_Facial_Attribute_CVPR_2021_paper.html)] [[Unofficial Pytorch](https://github.com/songquanpeng/L2M-GAN)]

**MoCoGAN-HD: A Good Image Generator Is What You Need for High-Resolution Video Synthesis.**<br>
*Yu Tian, Jian Ren, Menglei Chai, Kyle Olszewski, Xi Peng, Dimitris N. Metaxas, Sergey Tulyakov.*<br>
ICLR 2021. [[PDF](https://openreview.net/pdf?id=6puCSjH3hwA)] [[Code](https://github.com/snap-research/MoCoGAN-HD)]

**GAN Steerability without optimization.**<br>
*Nurit Spingarn-Eliezer, Ron Banner, Tomer Michaeli.*<br>
ICLR 2021. [[OpenReview](https://openreview.net/forum?id=zDy_nQCXiIj)] [[PDF](https://arxiv.org/abs/2012.05328)]

**On the "steerability" of generative adversarial networks.**<br>
*Ali Jahanian, Lucy Chai, Phillip Isola.*<br>
ICLR 2020. [[PDF](https://arxiv.org/abs/1907.07171)] [[Project](https://ali-design.github.io/gan_steerability/)]

**GANSpace: Discovering Interpretable GAN Controls.**<br>
*Erik Härkönen, Aaron Hertzmann, Jaakko Lehtinen, Sylvain Paris.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2004.02546)] [[Code](https://github.com/harskish/ganspace)]

**Interpreting the Latent Space of GANs for Semantic Face Editing.**<br>
*[Yujun Shen](http://shenyujun.github.io/), [Jinjin Gu](http://www.jasongt.com/), [Xiaoou Tang](http://www.ie.cuhk.edu.hk/people/xotang.shtml), [Bolei Zhou](http://bzhou.ie.cuhk.edu.hk/).*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/1907.10786)] [[Project](https://genforce.github.io/interfacegan/)] [[Code](https://github.com/genforce/interfacegan)]

**Seeing What a GAN Cannot Generate.**<br>
*David Bau, Jun-Yan Zhu, Jonas Wulff, William Peebles, Hendrik Strobelt, Bolei Zhou, Antonio Torralba.*<br>
ICCV 2019. [[PDF](https://arxiv.org/abs/1910.11626)] [[PDF](http://ganseeing.csail.mit.edu/)]

**Unsupervised Discovery of Interpretable Directions in the GAN Latent Space.**<br>
*Andrey Voynov, Artem Babenko.*<br>
ICML 2020. [[PDF](https://arxiv.org/abs/2002.03754)] [[Code](https://github.com/anvoynov/GANLatentDiscovery)]

**Multi-level Latent Space Structuring for Generative Control.**<br>
*[Oren Katzir](https://orenkatzir.github.io/), Vicky Perepelook, Dani Lischinski, Daniel Cohen-Or.*<br>
arxiv 2022. [[PDF](https://arxiv.org/abs/2202.05910)]

<p width="100%" align="right"><a href="#">🔝</a></p>

## Diffusion Inversion

**An Edit Friendly DDPM Noise Space: Inversion and Manipulations.**<br>
*[Inbar Huberman-Spiegelglas](https://inbarhub.github.io/www/), Vladimir Kulikov, Tomer Michaeli.*<br> 
CVPR 2024. [[PDF](http://arxiv.org/abs/2305.15391)] [[Project](https://inbarhub.github.io/DDPM_inversion/)] [[Code](https://github.com/inbarhub/DDPM_inversion)]

**Direct Inversion: Boosting Diffusion-based Editing with 3 Lines of Code.**<br>
*Xuan Ju, Ailing Zeng, Yuxuan Bian, Shaoteng Liu, Qiang Xu.*<br> 
ICLR 2024. [[PDF](https://arxiv.org/abs/2310.01506)] [[Code](https://github.com/cure-lab/DirectInversion)]

**NULL-text Inversion for Editing Real Images using Guided Diffusion Models.**<br>
*Ron Mokady, Amir Hertz, Kfir Aberman, Yael Pritch, Daniel Cohen-Or.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.09794)] [[Project](https://null-text-inversion.github.io/)] [[Code](https://github.com/google/prompt-to-prompt/#null-text-inversion-for-editing-real-images)]

**EDICT: Exact Diffusion Inversion via Coupled Transformations.**<br>
*Bram Wallace, Akash Gokul, Nikhil Naik.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.12446)] [[Code](https://github.com/salesforce/EDICT)]

**An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion.**<br>
*Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik, Daniel Cohen-Or.*<br>
ICLR 2023 (Oral). [[PDF](https://arxiv.org/abs/2208.01618)] [[Project](https://textual-inversion.github.io/)] [[Code](https://github.com/rinongal/textual_inversion)]

**Prompt-to-Prompt Image Editing with Cross Attention Control.**<br>
*Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, Daniel Cohen-Or.*<br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2208.01626)] [[Project](https://prompt-to-prompt.github.io/)] [[Code](https://github.com/google/prompt-to-prompt/)]

**A Neural Space-Time Representation for Text-to-Image Personalization.**<br>
*Yuval Alaluf, Elad Richardson, Gal Metzer, Daniel Cohen-Or.*<br> 
SIGGRAPH Asia 2023. [[PDF](https://arxiv.org/abs/2304.06140)] [[Project](https://neuraltextualinversion.github.io/NeTI/)]

**Discovering Interpretable Directions in the Semantic Latent Space of Diffusion Models.**<br>
*René Haas, Inbar Huberman-Spiegelglas, Rotem Mulayoff, and Tomer Michaeli.*<br> 
arxiv 2023. [[PDF](https://arxiv.org/abs/2303.11073)]

## Diffusion Latent Space Editing

Semantic Editing in Diffusion Latent Spaces.

**Self-Discovering Interpretable Diffusion Latent Directions for Responsible Text-to-Image Generation.**<br>
*Hang Li, Chengzhi Shen, Philip Torr, Volker Tresp, Jindong Gu.*<br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2311.17216)] [[Project](https://interpretdiffusion.github.io/)] [[Code](https://github.com/hangligit/InterpretDiffusion)]

**NoiseCLR: A Contrastive Learning Approach for Unsupervised Discovery of Interpretable Directions in Diffusion Models.**<br> 
*Yusuf Dalva, Pinar Yanardag.*<br> 
CVPR 2024 (Oral). [[PDF](https://arxiv.org/abs/2312.05390)] [[Project](https://noiseclr.github.io/)]

**An Edit Friendly DDPM Noise Space: Inversion and Manipulations.**<br>
*Inbar Huberman-Spiegelglas, Vladimir Kulikov, Tomer Michaeli.*<br> 
CVPR 2024. [[PDF](http://arxiv.org/abs/2304.06140)] [[Code](https://github.com/inbarhub/DDPM_inversion)]

**Diffusion Models Already Have A Semantic Latent Space.**<br>
*Mingi Kwon, Jaeseok Jeong, Youngjung Uh.*<br> 
ICLR 2023. [[PDF](http://arxiv.org/abs/2210.10960v2)]

**Unifying Diffusion Models' Latent Space, with Applications to CycleDiffusion and Guidance.**<br>
*Chen Henry Wu, Fernando De la Torre.*<br> 
ICCV 2023. [[PDF](http://arxiv.org/abs/2210.05559v2)] [[Code](https://github.com/ChenWu98/cycle-diffusion)]

**Generative Visual Prompt: Unifying Distributional Control of Pre-Trained Generative Models.**<br>
*Chen Henry Wu, Saman Motamed, Shaunak Srivastava, Fernando De la Torre.*<br> 
NeurIPS 2022. [[PDF](http://arxiv.org/abs/2209.06970v2)]

**$P+$: Extended Textual Conditioning in Text-to-Image Generation.**<br>
*Andrey Voynov, Qinghao Chu, Daniel Cohen-Or, Kfir Aberman.*<br> 
arxiv 2023. [[PDF](http://arxiv.org/abs/2303.09522v2)] [[Project](https://prompt-plus.github.io/)]

<p width="100%" align="right"><a href="#">🔝</a></p>

## Applications

### Image and Video Generation and Manipulation

**Diffusion-driven GAN Inversion for Multi-Modal Face Image Generation.**<br>
*Jihyun Kim, Changjae Oh, Hoseok Do, Soohyun Kim, Kwanghoon Sohn.*<br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2405.04356)] [[Project](https://github.com/1211sh/Diffusion-driven_GAN-Inversion/)]

**The Devil is in the Details: StyleFeatureEditor for Detail-Rich StyleGAN Inversion and High Quality Image Editing.**<br>
*Denis Bobkov, Vadim Titov, Aibek Alanov, Dmitry Vetrov.*<br>
CVPR 2024. [[PDF]()] [[Project]()]

**Robust One-Shot Face Video Re-enactment using Hybrid Latent Spaces of StyleGAN2.**<br>
*[Trevine Oorloff](https://trevineoorloff.github.io/), [Yaser Yacoob](https://www.umiacs.umd.edu/people/yaser).*<br> 
ICCV 2023. [[PDF](https://arxiv.org/abs/2302.07848)] [[Project](https://trevineoorloff.github.io/FaceVideoReenactment_HybridLatents.io/)]

**Expressive Talking Head Video Encoding in StyleGAN2 Latent-Space.**<br>
*[Trevine Oorloff](https://trevineoorloff.github.io/), [Yaser Yacoob](https://www.umiacs.umd.edu/people/yaser).*<br>
ICCVW 2023. [[PDF](https://arxiv.org/abs/2203.14512)] [[Project](https://trevineoorloff.github.io/Encode-in-Style.io/)] [[Code](https://github.com/trevineoorloff/Encode-in-Style)] [[Data](https://trevineoorloff.github.io/Encode-in-Style.io/)]

**CLIP-Guided StyleGAN Inversion for Text-Driven Real Image Editing.**<br>
*Ahmet Canberk Baykal, Abdul Basit Anees, Duygu Ceylan, Erkut Erdem, Aykut Erdem, Deniz Yuret.*<br> 
TOG 2023. [[PDF](https://dl.acm.org/doi/full/10.1145/3610287)]

**NeRFInvertor: High Fidelity NeRF-GAN Inversion for Single-shot Real Image Animation.**<br>
*Yu Yin, Kamran Ghasedi, HsiangTao Wu, Jiaolong Yang, Xin Tong, Yun Fu.*<br> 
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.17235)]

**Fine-Grained Face Swapping via Regional GAN Inversion.**<br>
*Zhian Liu, Maomao Li, Yong Zhang, Cairong Wang, Qi Zhang, Jue Wang, Yongwei Nie.*<br> 
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.14068)] [[Project](http://e4s2022.github.io)]

**VIVE3D: Viewpoint-Independent Video Editing using 3D-Aware GANs.**<br>
*Anna Frühstück, Nikolaos Sarafianos, Yuanlu Xu, Peter Wonka, Tony Tung.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2303.15893)] [[Project](http://afruehstueck.github.io/vive3D)] [[Code]()]

**Delving StyleGAN Inversion for Image Editing: A Foundation Latent Space Viewpoint.**<br>
*Hongyu Liu, Yibing Song, Qifeng Chen.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.11448)] [[Project](https://github.com/KumapowerLIU/CLCAE)] [[Code](https://github.com/KumapowerLIU/CLCAE)]

**Balancing Reconstruction and Editing Quality of GAN Inversion for Real Image Editing with StyleGAN Prior Latent Space.**<br>
*Kai Katsumata, Duc Minh Vo, Bei Liu, Hideki Nakayama.*<br> 
CVPR 2023 Workshop on AI4CC. [[PDF](http://arxiv.org/abs/2306.00241)]

**Modeling the Latent Dynamics of StyleGAN using Neural ODEs.**<br>
*Weihao Xia, Yujiu Yang, Jing-Hao Xue.*<br> 
NeurIPSW 2023. [[PDF](https://arxiv.org/abs/2208.11197)] [[Code](https://github.com/weihaox/dynode_released)]

**Dr.3D: Adapting 3D GANs to Artistic Drawings.**<br>
*Wonjoon Jin, Nuri Ryu, Geonung Kim, Seung-Hwan Baek, Sunghyun Cho.*<br>
SIGGRAPH Asia 2022. [[PDF](https://arxiv.org/abs/2211.16798)] [[Project](https://jinwonjoon.github.io/dr3d/)] 

**Stitch it in Time: GAN-Based Facial Editing of Real Videos.**<br>
*Rotem Tzaban, Ron Mokady, Rinon Gal, Amit H. Bermano, Daniel Cohen-Or.*<br>
SIGGRAPH Asia 2022. [[PDF](https://arxiv.org/abs/2201.08361)] [[Project](https://stitch-time.github.io/)] [[Code](https://github.com/rotemtzaban/STIT)]

**DyStyle: Dynamic Neural Network for Multi-Attribute-Conditioned Style Editing.**<br>
*Bingchuan Li, Shaofei Cai, Wei Liu, Peng Zhang, Miao Hua, Qian He, Zili Yi.*<br>
WACV 2023. [[PDF](https://arxiv.org/abs/2109.10737)] [[Code](https://github.com/phycvgan/DyStyle)]

**Generative Visual Prompt: Unifying Distributional Control of Pre-Trained Generative Models.**<br>
*Chen Henry Wu, Saman Motamed, Shaunak Srivastava, Fernando De la Torre.*<br>
NeurIPS 2022. [[PDF](https://arxiv.org/abs/2209.06970)] [[Code](https://github.com/ChenWu98/Generative-Visual-Prompt)]

**Generalized One-shot Domain Adaption of Generative Adversarial Networks.**<br>
*Zicheng Zhang, Yinglu Liu, Congying Han, Tiande Guo, Ting Yao, Tao Mei.*<br>
NeurIPS 2022. [[PDF](https://arxiv.org/abs/2209.03665)] [[Code](https://github.com/zhangzc21/Generalized-One-shot-GAN-Adaptation)]

**3D-FM GAN: Towards 3D-Controllable Face Manipulation.**<br>
*[Yuchen Liu](https://lychenyoko.github.io/), Zhixin Shu, Yijun Li, Zhe Lin, Richard Zhang, and Sun-Yuan Kung.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2208.11257)] [[Project](https://lychenyoko.github.io/3D-FM-GAN-Webpage/)]

**JoJoGAN: One Shot Face Stylization.**<br>
*Min Jin Chong, David Forsyth.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2112.11641)] [[Code](https://github.com/mchong6/JoJoGAN)]

**Generative Multiplane Images: Making a 2D GAN 3D-Aware.**<br>
*[Xiaoming Zhao](https://xiaoming-zhao.com/), [Fangchang Ma](https://fangchangma.github.io/), [David Güera](https://scholar.google.com/citations?user=bckYvFkAAAAJ&hl=en), [Zhile Ren](https://jrenzhile.com/), [Alexander G. Schwing](https://www.alexander-schwing.de/), [Alex Colburn](https://www.colburn.org/).*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2207.10642)] [[Project](https://xiaoming-zhao.github.io/projects/gmpi/)] [[Code](https://github.com/apple/ml-gmpi)]

**Injecting 3D Perception of Controllable NeRF-GAN into StyleGAN for Editable Portrait Image Synthesis.**<br>
*Jeong-gi Kwak, Yuanming Li, Dongsik Yoon, Donghyeon Kim, David Han, Hanseok Ko.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2207.10257)] [[Project](https://jgkwak95.github.io/surfgan/)]

**Temporally Consistent Semantic Video Editing.**<br>
*[Yiran Xu](https://twizwei.github.io/), [Badour AlBahar](https://badouralbahar.github.io/), [Jia-Bin Huang](https://jbhuang0604.github.io/).*<br>
ECCV 2022. [[PDF](https://arxiv.org/pdf/2206.10590.pdf)] [[Project](https://video-edit-gan.github.io/)] 

**Sound-Guided Semantic Video Generation.**<br>
*Seung Hyun Lee, Gyeongrok Oh, Wonmin Byeon, Jihyun Bae, Chanyoung Kim, Won Jeong Ryoo, Sang Ho Yoon, Jinkyu Kim, Sangpil Kim.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2204.09273)] [[Project](https://kuai-lab.github.io/eccv2022sound/)] [[Code]()]

**Third Time's the Charm? Image and Video Editing with StyleGAN3.**<br>
*Yuval Alaluf, Or Patashnik, Zongze Wu, Asif Zamir, Eli Shechtman, Dani Lischinski, Daniel Cohen-Or.*<br>
ECCV 2022 Workshop on Advances in Image Manipulation. [[PDF](https://arxiv.org/abs/2201.13433)] [[Project](https://yuval-alaluf.github.io/stylegan3-editing/)] [[Code](https://github.com/yuval-alaluf/stylegan3-editing)]

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

**StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators.**<br>
*[Rinon Gal](https://rinongal.github.io/), [Or Patashnik](https://orpatashnik.github.io/), [Haggai Maron](https://haggaim.github.io/), [Gal Chechik](https://research.nvidia.com/person/gal-chechik), [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br>
SIGGRAPH 2022. [[PDF](https://arxiv.org/abs/2108.00946)] [[Project](https://stylegan-nada.github.io/)] [[Code](https://github.com/rinongal/StyleGAN-nada)]

**SphericGAN: Semi-Supervised Hyper-Spherical Generative Adversarial Networks for Fine-Grained Image Synthesis.**<br>
*Tianyi Chen, Yunfei Zhang, Xiaoyang Huo, Si Wu, Yong Xu, Hau San Wong.*<br>
CVPR 2022. [[PDF](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_SphericGAN_Semi-Supervised_Hyper-Spherical_Generative_Adversarial_Networks_for_Fine-Grained_Image_Synthesis_CVPR_2022_paper.html)]

**Sound-Guided Semantic Image Manipulation.**<br>
*Seung Hyun Lee, Wonseok Roh, Wonmin Byeon, Sang Ho Yoon, Chan Young Kim, Jinkyu Kim, Sangpil Kim.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.00007)]

**HairCLIP: Design Your Hair by Text and Reference Image.**<br>
*Tianyi Wei, Dongdong Chen, Wenbo Zhou, Jing Liao, Zhentao Tan, Lu Yuan, Weiming Zhang, Nenghai Yu.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.05142)] [[Code](https://github.com/wty-ustc/HairCLIP)]

**HairMapper: Removing Hair from Portraits Using GANs.**<br>
*[Yiqian Wu](https://onethousandwu.com/), [Yong-Liang Yang](http://www.yongliangyang.net/), [Xiaogang Jin](http://www.cad.zju.edu.cn/home/jin).*<br>
CVPR 2022. [[PDF](http://www.cad.zju.edu.cn/home/jin/cvpr2022/HairMapper.pdf)] [[Project](http://www.cad.zju.edu.cn/home/jin/cvpr2022/cvpr2022.htm)] [[Code](https://github.com/oneThousand1000/non-hair-FFHQ/blob/main)] [[Non-hair-FFHQ Data](https://github.com/oneThousand1000/non-hair-FFHQ)]

**Attribute Group Editing for Reliable Few-shot Image Generation.**<br>
*Guanqi Ding, Xinzhe Han, Shuhui Wang, Shuzhe Wu, Xin Jin, Dandan Tu, Qingming Huang.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.08422)] [[Code](https://github.com/UniBester/AGE)]

**InsetGAN for Full-Body Image Generation.**<br>
*[Anna Frühstück](https://afruehstueck.github.io/), [Krishna Kumar Singh](http://krsingh.cs.ucdavis.edu/), [Eli Shechtman](https://research.adobe.com/person/eli-shechtman/), [Niloy J. Mitra](https://research.adobe.com/person/niloy-mitra/), [Peter Wonka](http://peterwonka.net/), [Jingwan Lu](https://research.adobe.com/person/jingwan-lu/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.07293)] [[Project](http://afruehstueck.github.io/insetgan)] [[Unofficial](https://github.com/stylegan-human/StyleGAN-Human/blob/main/insetgan.py)]

**SpaceEdit: Learning a Unified Editing Space for Open-Domain Image Editing.**<br>
*[Jing Shi](https://www.cs.rochester.edu/u/jshi31/), [Ning Xu](https://sites.google.com/view/ningxu/), [Haitian Zheng](https://www.cs.rochester.edu/u/hzheng15/haitian_homepage/index.html), Alex Smith, [Jiebo Luo](https://www.cs.rochester.edu/u/jluo/), [Chenliang Xu](https://www.cs.rochester.edu/~cxu22/).*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2112.00180)]

**In&Out: Diverse Image Outpainting via GAN Inversion.**<br>
*Yen-Chi Cheng, Chieh Hubert Lin, Hsin-Ying Lee, Jian Ren, Sergey Tulyakov, Ming-Hsuan Yang.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2104.00675)] [[Code](https://yccyenchicheng.github.io/InOut/)]

**InfinityGAN: Towards Infinite-Resolution Image Synthesis.**<br>
*Chieh Hubert Lin, Hsin-Ying Lee, Yen-Chi Cheng, Sergey Tulyakov, Ming-Hsuan Yang.*<br>
ICLR 2022. [[PDF](https://arxiv.org/abs/2104.03963)] [[Project](https://hubert0527.github.io/infinityGAN/)]

**Latent to Latent: A Learned Mapper for Identity Preserving Editing of Multiple.**<br>
*Siavash Khodadadeh, Shabnam Ghadar, Saeid Motiian, Wei-An Lin, Ladislau Bölöni, Ratheesh Kalarot.*<br>
WACV 2022. [[PDF](https://openaccess.thecvf.com/content/WACV2022/html/Khodadadeh_Latent_to_Latent_A_Learned_Mapper_for_Identity_Preserving_Editing_WACV_2022_paper.html)]

**StyleVideoGAN: A Temporal Generative Model using a Pretrained StyleGAN.**<br>
*[Gereon Fox](https://www.mpi-inf.mpg.de/~gfox/), [Ayush Tewari](https://www.mpi-inf.mpg.de/~atewari/), Mohamed Elgharib, [Christian Theobalt](http://gvv.mpi-inf.mpg.de/).*<br>
BMVC 2021 (Oral). [[PDF](https://arxiv.org/abs/2107.07224)]

**Face Image Retrieval With Attribute Manipulation.**<br>
*[Alireza Zaeemzadeh](https://zaeemzadeh.com/), Shabnam Ghadar, Baldo Faieta, Zhe Lin, Nazanin Rahnavard, Mubarak Shah, Ratheesh Kalarot.*<br>
ICCV 2021. [[PDF](https://openaccess.thecvf.com/content/ICCV2021/html/Zaeemzadeh_Face_Image_Retrieval_With_Attribute_Manipulation_ICCV_2021_paper.html)]

**StyleCariGAN: Caricature Generation via StyleGAN Feature Map Modulation.**<br>
*Wongjong Jang, Gwangjin Ju, [Yucheol Jung](https://ycjung.info/), [Jiaolong Yang](http://jlyang.org/), [Xin Tong](https://www.microsoft.com/en-us/research/people/xtong/), [Seungyong Lee](http://phome.postech.ac.kr/~leesy/).*<br>
TOG 2021. [[PDF](https://arxiv.org/pdf/2107.04331.pdf)] [[Code](https://github.com/PeterZhouSZ/StyleCariGAN)]

**Coarse-to-Fine: Facial Structure Editing of Portrait Images via Latent Space Classifications.**<br>
*[Yiqian Wu](https://onethousandwu.com/), [Yongliang Yang](http://www.yongliangyang.net/), Qinjie Xiao, [Xiaogang Ji](http://www.cad.zju.edu.cn/home/jin).*<br>
TOG 2021. [[PDF](http://www.cad.zju.edu.cn/home/jin/sig2021/paper46.pdf)] [[Project](http://www.cad.zju.edu.cn/home/jin/sig2021/sig2021.htm)]

**SAM: Only a Matter of Style-Age Transformation Using a Style-Based Regression Model.**<br>
*Yuval Alaluf, Or Patashnik, [Daniel Cohen-Or](https://www.cs.tau.ac.il/~dcor/).*<br>
TOG 2021. [[PDF](https://arxiv.org/abs/2102.02754)] [[Code](https://github.com/yuval-alaluf/SAM)]

**Barbershop: GAN-based Image Compositing using Segmentation Masks.**<br>
*[Peihao Zhu](https://github.com/ZPdesu), [Rameen Abdal](https://github.com/RameenAbdal), [John Femiani](https://scholar.google.com/citations?user=rS1xJIIAAAAJ&hl=en), [Peter Wonka](http://peterwonka.net/).*<br>
SIGGRAPH Asia 2021. [[PDF](https://arxiv.org/abs/2106.01505)] [[Project](https://zpdesu.github.io/Barbershop/)] [[Code](https://github.com/ZPdesu/Barbershop)]

**Constrained Graphic Layout Generation via Latent Optimization.**<br>
*Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.*<br>
ACM MM 2021. [[PDF](https://arxiv.org/abs/2108.00871)] [[Code](https://github.com/ktrk115/const_layout)]

**CI-GAN: Cycle-Consistent Inverse GAN for Text-to-Image Synthesis.**<br>
*Hao Wang, Guosheng Lin, Steven C. H. Hoi, Chunyan Miao.*<br>
ACM MM 2021. [[PDF](https://arxiv.org/abs/2108.01361)]

**Exploring Adversarial Fake Images on Face Manifold.**<br>
*Dongze Li, Wei Wang, Hongxing Fan, Jing Dong.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2101.03272)]

**HistoGAN: Controlling Colors of GAN-Generated and Real Images via Color Histograms.**<br>
*[Mahmoud Afifi](https://sites.google.com/view/mafifi), Marcus A. Brubaker, Michael S. Brown.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2011.11731)] [[Code](https://github.com/mahmoudnafifi/HistoGAN)] [[4K Landscape](https://ln2.sync.com/dl/1891becc0/uhsxtprq-33wfwmyq-dhhqeb3s-mtstuqw7/view/default/11118541390008)]

**One Shot Face Swapping on Megapixels.**<br>
*Yuhao Zhu, Qi Li, Jian Wang, Chengzhong Xu, Zhenan Sun.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2105.04932.pdf)] [[Code](https://github.com/zyainfal/One-Shot-Face-Swapping-on-Megapixels)]

**LOHO: Latent Optimization of Hairstyles via Orthogonalization.**<br>
*Rohit Saha, Brendan Duke, Florian Shkurti, Graham W. Taylor, Parham Aarabi.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2103.03891)] [[Code](https://github.com/dukebw/LOHO)]

**StyleMapGAN: Exploiting Spatial Dimensions of Latent in GAN for Real-time Image Editing.**<br>
*[Hyunsu Kim](https://github.com/blandocs), [Yunjey Choi](https://yunjey.github.io/), [Junho Kim](https://github.com/taki0112), [Sungjoo Yoo](http://cmalab.snu.ac.kr/), [Youngjung Uh](https://github.com/youngjung).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.14754)] [[Code](https://github.com/naver-ai/StyleMapGAN)]

**TediGAN: Text-Guided Diverse Image Generation and Manipulation.**<br>
*Weihao Xia, Yujiu Yang, Jing-Hao Xue, Baoyuan Wu.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.03308)] [[Data](https://github.com/weihaox/Multi-Modal-CelebA-HQ)] [[Code](https://github.com/weihaox/TediGAN)]

**DeepI2I: Enabling Deep Hierarchical Image-to-Image Translation by Transferring from GANs.**<br>
*yaxing wang, Lu Yu, Joost van de Weijer.*<br>
NeurIPS 2020. [[PDF](https://arxiv.org/abs/2011.05867)] [[Code](https://github.com/yaxingwang/DeepI2I)]

**DeepLandscape: Adversarial Modeling of Landscape Videos.**<br>
*E. Logacheva, R. Suvorov, O. Khomenko, A. Mashikhin, and V. Lempitsky.*<br>
ECCV 2020. [[PDF](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123680256.pdf)] [[Code](https://github.com/saic-mdal/deep-landscape)] [[Project](https://saic-mdal.github.io/deep-landscape/)]

**Few-shot Semantic Image Synthesis Using StyleGAN Prior.**<br>
*Yuki Endo, Yoshihiro Kanamori.*<br>
arxiv 2021. [[PDF](https://arxiv.org/abs/2103.14877)] [[Code](https://github.com/endo-yuki-t/Fewshot-SMIS)]

**Paint by Word.**<br>
*David Bau, Alex Andonian, Audrey Cui, YeonHwan Park, Ali Jahanian, Aude Oliva, Antonio Torralba.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2103.10951)] [[Project](http://paintbyword.csail.mit.edu/)] [[Project](https://github.com/alexandonian/paint-by-word)]

### Image Restoration

**LTT-GAN: Looking Through Turbulence by Inverting GANs.**<br> 
*[Kangfu Mei](https://kfmei.page/), [Vishal M. Patel](https://engineering.jhu.edu/vpatel36/sciencex_teams/vishalpatel/).*<br> 
J-STSP 2023. [[PDF](https://arxiv.org/abs/2112.02379)] [[Project](https://kfmei.page/LTT-GAN/)]

**Semantic Uncertainty Intervals for Disentangled Latent Spaces.**<br> 
*Swami Sankaranarayanan, Anastasios N. Angelopoulos, Stephen Bates, Yaniv Romano, Phillip Isola.*<br> 
NeurIPS 2022. [[PDF](https://arxiv.org/abs/2207.10074)] [[Code](https://github.com/swamiviv/generative_semantic_uncertainty)]

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
SIGGRAPH Asia 2021 (TOG). [[PDF](https://arxiv.org/abs/2012.12261)] [[Project](https://time-travel-rephotography.github.io/)] [[Code](https://github.com/Time-Travel-Rephotography/Time-Travel-Rephotography.github.io)]

**GPEN: GAN Prior Embedded Network for Blind Face Restoration in the Wild.**<br>
*Tao Yang, Peiran Ren, Xuansong Xie, Lei Zhang.*<br>
CVPR 2021. [[PDF](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_GAN_Prior_Embedded_Network_for_Blind_Face_Restoration_in_the_CVPR_2021_paper.pdf)] [[Code](https://github.com/)]

**GLEAN: Generative Latent Bank for Large-Factor Image Super-Resolution.**<br>
*[Kelvin C.K. Chan](https://ckkelvinchan.github.io/), Xintao Wang, Xiangyu Xu, Jinwei Gu, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.00739)] [[Project](https://ckkelvinchan.github.io/projects/GLEAN)] [[Code](https://github.com/ckkelvinchan/GLEAN)]

**GFP-GAN: Towards Real-World Blind Face Restoration with Generative Facial Prior.**<br>
*[Xintao Wang](https://xinntao.github.io/), [Yu Li](https://yu-li.github.io/), [Honglun Zhang](https://scholar.google.com/citations?hl=en&user=KjQLROoAAAAJ), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2101.04061)] [[Project](https://xinntao.github.io/)]

**PULSE: Self-Supervised Photo Upsampling via Latent Space Exploration of Generative Models.**<br>
*Sachit Menon, Alexandru Damian, Shijia Hu, Nikhil Ravi, Cynthia Rudin.*<br>
CVPR 2020. [[PDF](https://arxiv.org/abs/2003.03808)] [[Code](https://github.com/adamian98/pulse)]

**Style Generator Inversion for Image Enhancement and Animation.**<br>
*[Aviv Gabbay](http://www.cs.huji.ac.il/~avivga), [Yedid Hoshen](http://www.cs.huji.ac.il/~ydidh).*<br>
arxiv 2019. [[PDF](https://arxiv.org/abs/1906.11880)] [[Project](http://www.vision.huji.ac.il/style-image-prior/)] [[Code](https://github.com/avivga/style-image-prior)]

### Image Understanding

**Finding an Unsupervised Image Segmenter in each of your Deep Generative Models.**<br> 
*Luke Melas-Kyriazi, Christian Rupprecht, Iro Laina, Andrea Vedaldi.*<br>
ICLR 2022. [[PDF](https://openreview.net/forum?id=Ug-bgjgSlKV)]

**Labels4Free: Unsupervised Segmentation using StyleGAN.**<br>
*[Rameen Abdal](https://scholar.google.com/citations?user=kEQimk0AAAAJ&hl=en), [Peihao Zhu](https://scholar.google.com/citations?user=Gn8URq0AAAAJ&hl=en), [Niloy Mitra](http://www0.cs.ucl.ac.uk/staff/n.mitra/), [Peter Wonka](http://peterwonka.net/).*<br>
ICCV 2021. [[PDF](https://arxiv.org/abs/2103.14968)] [[Project](https://rameenabdal.github.io/Labels4Free)] [[Code](https://github.com/RameenAbdal/Labels4Free)]

**DatasetGAN: Efficient Labeled Data Factory with Minimal Human Effort.**<br>
*[Yuxuan Zhang](https://www.alexyuxuanzhang.com/), [Huan Ling](http://www.cs.toronto.edu/~linghuan/), [Jun Gao](http://www.cs.toronto.edu/~jungao/), [Kangxue Yin](https://kangxue.org/), [Jean-Francois Lafleche](), [Adela Barriuso](), [Antonio Torralba](https://groups.csail.mit.edu/vision/torralbalab/), [Sanja Fidler](http://www.cs.utoronto.ca/~fidler/).*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2104.06490)] [[Code](https://github.com/nv-tlabs/datasetGAN_release)] [[Project](https://nv-tlabs.github.io/datasetGAN/)]

**Repurposing GANs for One-shot Semantic Part Segmentation.**<br>
*Nontawat Tritrong, Pitchaporn Rewatbowornwong, [Supasorn Suwajanakorn](https://www.supasorn.com/).*<br>
CVPR 2021 (oral). [[PDF](https://arxiv.org/abs/2103.04379)] [[Project](https://repurposegans.github.io/)] [[Code](https://github.com/bryandlee/repurpose-gan)]

**Segmentation in Style: Unsupervised Semantic Image Segmentation with Stylegan and CLIP.**<br>
*Daniil Pakhomov, Sanchit Hira, Narayani Wagle, Kemar E. Green, Nassir Navab.*<br>
arxiv 2021. [[PDF](https://arxiv.org/pdf/2107.12518.pdf)] [[Project](https://segmentation-in-style.github.io/)] [[Code](https://github.com/warmspringwinds/segmentation_in_style)]

### Face Recognition

**How to Boost Face Recognition with StyleGAN?**<br>
*Artem Sevastopolsky, Yury Malkov, Nikita Durasov, Luisa Verdoliva, Matthias Nießner.*<br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2210.10090)] [[Code](https://github.com/seva100/stylegan-for-facerec)]

### 3D Reconstruction

**StyleGAN Knows Normal, Depth, Albedo, and More.**<br>
*[Anand Bhattad](https://anandbhattad.github.io/), [Daniel McKee](https://www.danielbmckee.com/), [Derek Hoiem](https://dhoiem.cs.illinois.edu/), [D. A. Forsyth](http://luthuli.cs.uiuc.edu/~daf/).*<br> 
NeurIPS 2023. [[PDF](http://arxiv.org/abs/2306.00987)]

**Shape, Pose, and Appearance from a Single Image via Bootstrapped Radiance Field Inversion.**<br>
*Dario Pavllo, David Joseph Tan, Marie-Julie Rakotosaona, Federico Tombari.*<br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.11674)] [[Code](https://github.com/google-research/nerf-from-image)]

**Monocular 3D Object Reconstruction with GAN Inversion.**<br>
*Junzhe Zhang, Daxuan Ren, Zhongang Cai, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2207.10061)] [[Project](https://www.mmlab-ntu.com/project/meshinversion/)] [[Code](https://github.com/junzhezhang/mesh-inversion)]

**CoordGAN: Self-Supervised Dense Correspondences Emerge from GANs.**<br>
*[Jiteng Mu](https://jitengmu.github.io/), Shalini De Mello, Zhiding Yu, Nuno Vasconcelos, Xiaolong Wang, Jan Kautz, Sifei Liu.*<br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2203.16521)] [[Project](https://jitengmu.github.io/CoordGAN/)]

**Normalized Avatar Synthesis Using StyleGAN and Perceptual Refinement.**<br>
*Huiwen Luo, Koki Nagano, Han-Wei Kung, Mclean Goldwhite, [Qingguo Xu](https://qingguo-xu.com/), Zejian Wang, Lingyu Wei, Liwen Hu, Hao Li.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2106.11423)]

**Unsupervised 3D Shape Completion through GAN-Inversion.**<br>
*[Junzhe Zhang](https://junzhezhang.github.io/), Xinyi Chen, Zhongang Cai, Liang Pan, Haiyu Zhao, Shuai Yi, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2104.13366)] [[Project](https://junzhezhang.github.io/projects/ShapeInversion/)]

**Unsupervised 3D Shape Completion through GAN-Inversion.**<br>
*[Junzhe Zhang](https://junzhezhang.github.io/), Xinyi Chen, Zhongang Cai, Liang Pan, Haiyu Zhao, Shuai Yi, Chai Kiat Yeo, Bo Dai, Chen Change Loy.*<br>
CVPR 2021. [[PDF](https://arxiv.org/pdf/2104.13366)] [[Project](https://junzhezhang.github.io/projects/ShapeInversion/)]

**OSTeC: One-Shot Texture Completion.**<br>
*Baris Gecer, Jiankang Deng, Stefanos Zafeiriou.*<br>
CVPR 2021. [[PDF](https://arxiv.org/abs/2012.15370)] [[Code](https://github.com/barisgecer/OSTeC)]

**GAN2Shape: Do 2D GANs Know 3D Shape? Unsupervised 3D shape reconstruction from 2D Image GANs.**<br>
*[Xingang Pan](https://xingangpan.github.io/), Bo Dai, Ziwei Liu, Chen Change Loy, Ping Luo.*<br>
ICLR 2021 (oral). [[PDF](https://arxiv.org/abs/2011.00844)] [[Code](https://github.com/XingangPan/GAN2Shape)] [[Project](https://xingangpan.github.io/projects/GAN2Shape.html)]

### Other Applications

#### Compressed Sensing

**Generator Surgery for Compressed Sensing.**<br>
*Niklas Smedemark-Margulies, Jung Yeon Park, Max Daniels, Rose Yu, Jan-Willem van de Meent, Paul Hand.*<br>
NeurIPS 2020 Workshop on Deep Inverse. [[PDF](https://arxiv.org/abs/2102.11163)] [[Code](https://github.com/nik-sm/generator-surgery)]

**Task-Aware Compressed Sensing with Generative Adversarial Networks.**<br>
*Maya Kabkab, Pouya Samangouei, Rama Chellappa.*<br>
AAAI 2018. [[PDF](https://arxiv.org/pdf/1802.01284.pdf)]

#### Medical Imaging

**Controllable Medical Image Generation via Generative Adversarial Networks.**<br>
*Zhihang Ren, Stella X. Yu, David Whitney.*<br>
Human Vision and Electronic Imaging 2021. [[PDF](https://whitneylab.berkeley.edu/PDFs/Ren_MedImageGen.pdf)]

**High-resolution Controllable Prostatic Histology Synthesis using StyleGAN.**<br>
*Gagandeep B. Daroach, Josiah A. Yoder, Kenneth A. Iczkowski, Peter S. LaViolette.*<br>
Bioimaging 2021. [[PDF](https://www.scitepress.org/Papers/2021/103939/103939.pdf)]

#### Compression, Fairness, and Security

**FairStyle: Debiasing StyleGAN2 with Style Channel Manipulations.**<br>
*Cemre Karakas, Alara Dirik, Eylul Yalcinkaya, Pinar Yanardag.*<br>
ECCV 2022. [[PDF](https://arxiv.org/abs/2202.06240)] [[Project](https://catlab-team.github.io/fairstyle/)] [[Code](https://drive.google.com/drive/folders/1PW7w80ZKuLnjnxJNeNkYxXUFvVYi6I6H?usp=sharing)]

**Video Coding Using Learned Latent GAN Compression.**<br>
*Mustafa Shukor, Bharath Bhushan Damodaran, Xu Yao, Pierre Hellier.*<br>
ACM MM 2022. [[PDF](https://arxiv.org/abs/2207.04324)]

**Differentially Private Imaging via Latent Space Manipulation.**<br>
*Tao Li, Chris Clifton.*<br>
IEEE Symposium on Security & Privacy (S&P) 2021. [[PDF](https://arxiv.org/abs/2103.05472)]

## Acknowledgement

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
