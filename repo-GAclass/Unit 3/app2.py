#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:56:40 2021

@author: harleyhoffmann
"""

import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/JonathanBechtel/dat-02-22/main/ClassMaterial/Unit3/data/ks2.csv', nrows=2000)

st.header("Exploring Kickstarter Campaigns")

st.write(df)