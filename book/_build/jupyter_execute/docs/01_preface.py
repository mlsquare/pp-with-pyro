#!/usr/bin/env python
# coding: utf-8

# (preface)=
# 
# # Preface
# 
# Welcome to the lecture notes on *probabilistic programming with pyro a case-based approach* 
# 
# In these lectures notes, we will pick problems from various domains like Biology, Engineering, Physical Sciences and many others.  We will pick frameworks like _pyro_ to declaratively specify the models and perform the inference, almost automatically.  Along the way, we learn and apply concepts from the Bayesian paradigm like the Bayesian Generalized Linear Models, Hierarchical Models, and the classical statistical methods like Survival Analysis, Spatial Statistics, Time Series Forecasting.  Not just that, we'll also learn how to solve Stochastic Differential Equations and learn about the recently emerging techniques like Physics Inspired Neural Networks or PINs as they're called.
# 
# 
# > \"Pyro inline"
# 
# 
# ## The Pedagogy
# 
# The pedagogy that we follow here  is that of a case-based approach -- meaning we'll pick a particular problem and solve it end-to-end. That is we look at the context,  the data,  do a little bit of an exploratory data analysis, followed by eliciting a model.  Inspiration could come from a baseline or a literature, then we fit those models using pyro or similar frameworks.  Apply due diligence in assessing  how good the fit was. Follow it up with model checking, moral comparison, and inference. Discuss why did we make a particular choice, what are the other alternatives, can we go with a different modeling approach altogether. 
# 
# This is the case-based approach we we follow unlike how it is  probabilistic programming traditionally is taught,  which is you learn the theory then come back and apply it on a couple of problems. So that means over a period of time, we will solve maybe 50 60 problems each being a standalone  module by itself. That is, we will have the necessary and sufficient theory to look at that particular problem and along with it check out the technologies that are needed to solve it. That is the structure we follow uh in the in these lectures notes.
# 
# 
# ## Learnign Objectives
# 
# 1. Elicit generative models
# 2. Declaratively specify them in Pyro
# 3. Translate models from one framework to another
# 4. Understand end-to-end modeling pipeline
# 5. Learn and apply variety of modeling techniques to problems from many domains
# 
# 
# ## Why PPL and why now
# 
# A very important question, indeed. Due to the success of Deep Learning, particularly computer vision, AI/ML is becoming mainstream. AI/ML is almost becoming a commodity.  Come with it are lots of challenges.  For example, if you deploy model and make a prediction, sometimes, it is good to say that "i don't know how to make a prediction" on a particular example. But typical Machine Learning systems were not generally caring about uncertainty quantification.  Mostly, they'll be happy just making a prediction. But that's no longer the case. -- it could be regulatory compliance or legal compliance or simply the ability to know that that the algorithm is not confident in the prediction itself is very important. In such scenarios, Bayesian modelling is a very natural alternative.  Because, fundamentally every statement (hypothesis) can be attached with a probability measure, such as  prediction intervals, credible intervals. In general, quantify uncertainty of any function of the data in terms of probabilities.
# 
# ## Why Pyro
# 
# Thanks to some recent advancements in the Bayesian inference, the theoretical side itself like the Hamiltonian Monte Carlo, that exploits the gradients to sampling the posterior,  we can fit large models automatically. It is akin to Back Propogation for fitting plain Deep Learning models. 
# 
# That's a tremendous advantage but the disadvantage for a long time was that you have to write your own inference engine -- meaning it's not simple to obtain those posterior summaries or estimate any analytical quantity that is of importance.  But fortunately tools like winBUGS, stan and pyro make Bayesian inference possible because they do all the hard work. That is, have general purpose samplers written underneath them.
# 
# Therefore, a data scientist or a modeler can focus on the modeling exercise and not worry so much on how do to implement a sampler specifically for that particular model. It saves a lot of time, money and effort. So in a nutshell, that is a motivation for learning probabilistic programming languages because you can declaratively specify the model and let the inference be done now by the tool automatically.
