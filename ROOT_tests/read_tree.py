#!/usr/bin/env python3
import ROOT
ROOT.gROOT.Reset()

#browser = ROOT.TBrowser()
file = ROOT.TFile("data/D0_Signal_MonteCarlo.root")
tree = file.Get("ntpD0")
#tree.Show(0) #Reading only one event with index (i)
tree.Print()


''' Don't delete input() below, comment if there is no need for GUI instances.'''
#input()
