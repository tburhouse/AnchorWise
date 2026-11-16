# AnchorWise

## Project Overview

The AnchorWise Project will guide by suggesting which anchorages will be sheltered and best to use based on the weather forecast. The completed version aims to include ratings, facilities overview and suggest based on needs and how long the anchorage will be in sheltered weather conditions.

## Current Features

The current version of AnchorWise allows users to save and load a vessel profile which asks for relevant information like vessel length, boat draft and anchor chain length. When creating the boat profile, the information gets validated, then saved using JSON. The save and load functions are in separate functions. 

## Technology Stack

This version current uses:
Python 3.13
Python standard library, including the json module
Modular programming using separate Python files

## Installation & Usage

Requirements: Python installed on the computer, current version tested on Python 3.13.
Obtaining the project: Download or clone the repository from GitHub.
Stating Anchorwise: Open a teminal in project folder and run anchorwise_v01.py using Python: python anchorwise_v01.py
Creating a vessel: Select Option 1 enter the five vessel attributes it asks for and save the profile.
Loading a vessel: Run the application again and select Option 2 to retreive the saved profile. 

You must create a vessel profile before one ccan be loaded. 

## Development Roadmap

V0.2 - Weather API intergration and wind forecast retrieval.

V1.0 - Harbour searches, canditate anchorage mapping and preliminary shelter rankings.

V2.0 - Historical data analysis, data pipelines and databases.

V3.0 - Microsoft Azure integration.

V4.0 - Mobile application and facilities information. 


## Limitations & Status

V0.1 only manages vessel profiles, it does not yet recommend anchorages.
Only one vessel profile can be saved at a time, and creating another overwrites it.
Non-Numerical measurement inputs and missing profile files aren't yet handled gracefully.
The application is an early development prototype and self-learning tool, not a maritime navigation or safety system. 