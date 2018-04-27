## About this repo.
This is my note for the the machine learning courses taught by 
Prof. Hsuan-Tien Lin.

2018 April

## Outline
When Can Machines Learn? 何時可以使用機器學習?

- 第一講：The Learning Problem [機器學習問題](./course01.ipynb)
- 第二講：Learning to Answer Yes/No [二元分類](./course02.ipynb)
- 第三講：Types of Learning [各式機器學習問題](./course03.ipynb)
- 第四講：Feasibility of Learning [機器學習的可行性](./course04.ipynb)

Why Can Machines Learn? 為什麼機器可以學習?

- 第五講：Training versus Testing [訓練與測試]
- 第六講：Theory of Generalization [舉一反三的一般化理論]
- 第七講：The VC Dimension [VC 維度]
- 第八講：Noise and Error [雜訊與錯誤]

## What should you have?

機率統計、線性代數、微分之基本知識. A summary can be found ![here]{./homework/homework0.pdf}.

## References

Learning from Data: A Short Course , Abu-Mostafa, Magdon-Ismail, Lin, 2013.

經典文獻

F. Rosenblatt. The perceptron: A probabilistic model for information storage and organization in the brain. Psychological Review, 65(6):386-408, 1958. (第二講：Perceptron 的出處)

W. Hoeffding. Probability inequalities for sums of bounded random variables. Journal of the American Statistical Association, 58(301):13–30, 1963. (第四講：Hoeffding's Inequality)

Y. S. Abu-Mostafa, X. Song , A. Nicholson, M. Magdon-ismail. The bin model, 1995. (第四講：bin model 的出處)

V. Vapnik. The nature of statistical learning theory, 2nd edition, 2000. (第五到八講：VC dimension 與 VC bound 的完整數學推導及延伸)

Y. S. Abu-Mostafa. The Vapnik-Chervonenkis dimension: information versus complexity in learning. Neural Computation, 1(3):312-317, 1989. (第七講：VC Dimension 的概念與重要性)

參考文獻

A. Sadilek, S. Brennan, H. Kautz, and V. Silenzio. nEmesis: Which restaurants should you avoid today? First AAAI Conference on Human Computation and Crowdsourcing, 2013. (第一講：ML 在「食」的應用)

Y. S. Abu-Mostafa. Machines that think for themselves. Scientific American, 289(7):78-81, 2012. (第一講：ML 在「衣」的應用)

A. Tsanas, A. Xifara. Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools. Energy and Buildings, 49: 560-567, 2012. (第一講：ML 在「住」的應用)

J. Stallkamp, M. Schlipsing, J. Salmen, C. Igel. Introduction to the special issue on machine learning for traffic sign recognition. IEEE Transactions on Intelligent Transportation Systems 13(4): 1481-1483, 2012. (第一講：ML 在「行」的應用)

R. Bell, J. Bennett, Y. Koren, and C. Volinsky. The million dollar programming prize. IEEE Spectrum, 46(5):29-33, 2009. (第一講：Netflix 大賽)

S. I. Gallant. Perceptron-based learning algorithms. IEEE Transactions on Neural Networks, 1(2):179-191, 1990. (第二講：pocket 的出處，注意到實際的 pocket 演算法比我們介紹的要複雜)

R. Xu, D. Wunsch II. Survey of clustering algorithms. IEEE Transactions on Neural Networks 16(3), 645-678, 2005. (第三講：Clustering)

X. Zhu. Semi-supervised learning literature survey. University of Wisconsin Madison, 2008. (第三講：Semi-supervised)

Z. Ghahramani. Unsupervised learning. In Advanced Lectures in Machine Learning (MLSS ’03), pages 72–112, 2004. (第三講：Unsupervised)

L. Kaelbling, M. Littman, A. Moore. reinforcement learning: a survey. Journal of Artificial Intelligence Research, 4: 237-285. (第三講：Reinforcement)

A. Blum. On-Line algorithms in machine learning. Carnegie Mellon University,1998. (第三講：Online)

B. Settles. Active learning literature survey. University of Wisconsin Madison, 2010. (第三講：Active)

D. Wolpert. The lack of a priori distinctions between learning algorithms. Neural Computation, 8(7): 1341-1390. (第四講：No free lunch 的正式版)

T. M. Cover. Geometrical and statistical properties of systems of linear inequalities with applications in pattern recognition. IEEE Transactions on Electronic Computers, 14(3):326–334, 1965. (第五到六講：Growth Function)

B. Zadrozny, J. Langford, N. Abe. Cost sensitive learning by cost-proportionate example weighting. IEEE International Conference on Data Mining, 2003. (第八講：Weighted Classification)
