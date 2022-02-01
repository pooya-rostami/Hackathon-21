# Project Info for MSR2022: Team NAP
Name - Bot Detection in GitHub Repositories

Members - Natarajan Chidambaram, Pooya Rostami Mazrae

Affiliation - Software Engineering Lab, University of Mons, Belgium

Tool location - https://github.com/mehdigolzadeh/BoDeGHa

Associated Publication - 

        @article{Golzadeh2021JSS,
            title={A ground-truth dataset and classification model for detecting bots in GitHub issue and PR comments}, 
            author={Golzadeh, Mehdi and Decan, Alexandre and Legay, Damien and Mens, Tom},
            year={2021},
            volume = 175,
            month = {may},
            journal = {Journal of Systems and Software},
            doi = {https://doi.org/10.1016/j.jss.2021.110911}
        }


# Idea:
1. Adding the machine learning part of BoDeGHa bot detection tool as a plugin to the GrimoireLab tool for identifying bot accounts in GitHub repositories

2. Use Grimoirelab's tool for Visualization and find room for its improvement to further study about bots

# Usage:
Execute the Code/MSR2022.ipynb file.

Note: A list of repositories and a GitHub API token has to be provided in the file immediately after the imports for querying

# Description:
The script will query the repositories given in the list of repositories using Perceval, extracts the required data and stores it in < owner >_< repo >.csv format in /Data/ folder. 
        
Then the user need to enter the file name < owner > _ < repo >.csv for which they need to predict the type of the account using BoDeGHa's trained machine learning classifier. The corresponding predictions will be stored in \Predicitons\ folder under < owner > _ < repo >.csv filename.

Then the user need to enter a list of filenames in \Predicitons\ folder that need to be visualized using Kibana. Finally, follow the instructions given under Visualization section to work with Kibana.  
