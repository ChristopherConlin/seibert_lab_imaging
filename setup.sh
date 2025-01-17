#!/usr/bin/tcsh

mv .tcshrc ~/
source ~/.tcshrc
mkdir -p ~/Documents/MATLAB
mv startup.m ~/Documents/MATLAB/

cd ../
git clone https://github.com/ChristopherConlin/cmig_utils.git
git clone https://github.com/ChristopherConlin/rsi_prostate.git



