# Recombination-model-for-charm-meson-production-at-2.76-5.02-TeV-PbPb-collisions
This is my undergraduate scientific training in the Physics Department of Sichuan University. I am grateful for the guidance and advice provided by Lilin Zhu (SCU) and Hua Zheng (SNNU) during this training period.

Our study using the Recombination Model (RM) consider the production of charm meson at 2.76 & 5.02TeV Pb-Pb collisionm, the experiment data can be found at Alice web

Here is a breakdown of the details in terms of files:

1. Reference
Contains main references to initial prerequisites, charm quark work, and data reference
2. Data
Includes the required data for the LHC work.
3. minutes of the weekly meeting
Contains several beams during our work.
4. Numerical program
recombination_v16.f90 can calculate the spectrum of inclusive meson in different collision. I get the former version of the program for upperclassman Huanjing Gong，and change the mistaken and imporper assumption. Meanwhile, we get the dependence of parameters by interpolation. Please change the several ID in the beginning of this program, like IDparticle, and the loop range of pT, when you need to calculate the different meson.

parameter_##_.f90 is used for scanning parameters like Cc, T to fit the spectrum，needing the experiment data. these part of program can apply for other particals you need in the futrue, after a little bit changging. However, if you just want to recurrent my study, the only thing you need is recombination_v16.f90。

5. result
final result and summary of my study
