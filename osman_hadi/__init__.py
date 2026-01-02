# osman_hadi/__init__.py

from .osman_bio import bio
from .osman_edu import edu
from .osman_career import career
from .osman_family import family
from .osman_july import july_uprising as july_hadi
from .osman_quotes import quotes
from .osman_initiatives import initiatives
from .osman_martyrdom import martyrdom

# ছবি দেখানোর কমান্ডসমূহ
from .styles import his_face1, his_face2, his_face3, his_face4, his_face5

def show_all():
    """
    একসাথে সব তথ্য দেখার জন্য।
    """
    bio()
    edu()
    career()
    family()
    july_hadi()
    initiatives()
    quotes()
    martyrdom()

def help():
    print("""
    --- SHAHEED OSMAN BIN HADI ARCHIVE HELP ---
    
    [বি.দ্র: প্রতিটি ফাংশন কল করলে বাংলা ও ইংরেজি উভয় তথ্য প্রদর্শিত হবে]
    
    Commands:
    1. bio()         -> Biography (জীবন পরিচিতি)
    2. edu()         -> Education (শিক্ষাজীবন - ঢাবি ও মাদরাসা)
    3. career()      -> Career (কর্মজীবন ও লেখক সত্তা)
    4. family()      -> Family (পরিবার ও একমাত্র পুত্র সন্তান)
    5. july_hadi()   -> July Uprising (জুলাই বিপ্লব ও প্রতিরোধ)
    6. initiatives() -> Initiatives (ইনকিলাব মঞ্চ ও উদ্যোগসমূহ)
    7. quotes()      -> Quotes & Philosophy (ঐতিহাসিক উক্তি ও দর্শন)
    8. martyrdom()   -> Martyrdom (শাহাদাত ও আওয়ামী ষড়যন্ত্র)
    9. show_all()    -> Display all information at once.
    
    Face Art: his_face1() to his_face5()
    """)
