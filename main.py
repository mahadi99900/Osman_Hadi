# main.py

import osman_hadi as oh

def start_archive():
    print("Welcome to Shaheed Osman Bin Hadi Digital Archive")
    print("================================================")
    
    # ১. সাহায্য বা কমান্ড লিস্ট দেখানো
    oh.help()
    
    # ২. ছবি বা আর্ট দেখানো
    print("\nDisplaying Portrait...")
    oh.his_face1()
    
    # ৩. বাংলা ও ইংরেজি উভয় ভাষায় তথ্য দেখা
    print("\n--- Biography / জীবনী ---")
    oh.bio()
    
    print("\n--- Education / শিক্ষাজীবন ---")
    oh.edu()
    
    print("\n--- Quotes / উক্তি ---")
    oh.quotes()

if __name__ == "__main__":
    start_archive()
