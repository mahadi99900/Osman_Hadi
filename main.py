# main.py

import osman_hadi as oh

def start_archive():
    print("Welcome to Shaheed Osman Bin Hadi Digital Archive")
    print("================================================")
    
    
    oh.help()
    
   
    print("\nDisplaying Portrait...")
    oh.his_face1()
    
   
    print("\n--- Biography / জীবনী ---")
    oh.bio()
    
    print("\n--- Education / শিক্ষাজীবন ---")
    oh.edu()
    
    print("\n--- Quotes / উক্তি ---")
    oh.quotes()

if __name__ == "__main__":
    start_archive()
