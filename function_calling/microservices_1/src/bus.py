bus_routes: dict[int, list[str]] = {
    1: ["Railway Station", "Ek Moriya", "Nawaz Sharif Hospital", "Kashmiri Gate", "Lari Adda", "Azadi Chowk", "Texali Chowk", "Bhatti Chowk"],
    2: ["Samanabad Morr", "Corporation Chowk", "Taj Company", "Sanda", "Double Sarkan", "Moon Market", "Ganda Nala", "Bhatti Chowk"],
    3: ["Railway Station", "Ek Moriya", "Nawaz Sharif Hospital", "Kashmiri Gate", "Lari Adda", "Azadi Chowk", "Timber Market", "METRO", "Niazi Chowk", "Shahdara Metro Station", "Shahdara Lari Adda"],
    4: ["R.A Bazar", "Nadeem Chowk", "Defence Morr", "Shareef Market", "Walton", "Qainchi", "Ghazi Chowk", "Chungi Amar Sidhu"],
    5: ["Shad Bagh Underpass", "Rajput Park", "Madina Chowk", "Lohay Wali Pulley", "Badami Bagh", "Lari Adda Gol Chakar", "Azadi Chowk", "Taxali Chowk", "Bhatti Chowk"],
    6: ["Babu Sabu", "Niazi Adda", "City Bus Stand", "Chowk Yateem Khana", "Bhala Stop", "Samanabad Morr", "Chauburji", "Riwaz Garden", "M.A.O College", "Firdous Cinema", "Raj Garh Chowk"],
    7: ["Bagrian", "Depot Chowk", "Minhaj University", "Hamdard Chowk", "Rehmat Eye Hospital", "Pindi Stop", "Peco Morr", "Kot Lakhpat Railway Station", "Phatak Mandi", "Qainchi", "Ghazi Chowk", "Chungi Amar Sidhu"],
    8: ["Doctor Hospital", "Wafaqi Colony", "IBA Stop", "Hailey College", "Campus Pull", "Barkat Market", "Kalma Chowk", "Qaddafi Stadium", "Canal"],
    9: ["Railway Station", "Haji Camp", "Shimla Pahari", "Lahore Zoo", "Chairing Cross", "Ganga Ram Hospital", "Qartaba Chowk", "Chauburji", "Sham Nagar"],
    10: ["Multan Chungi", "Mustafa Town", "Karim Block Market", "PU Examination Center", "Bhekewal Morr", "Wahdat Colony", "Naqsha Stop", "Canal", "Ichra", "Shama", "Qartaba Chowk"],
    11: ["Babu Sabu", "Niazi Adda", "City Bus Stand", "Chowk Yateem Khana", "Scheme Morr", "Flat Stop", "Dubai Chowk", "Bhekewal Morr", "Sheikh Zaid Hospital", "Campus Pull", "Barkat Market", "Kalma Chowk", "Liberty Chowk", "Hafeez Center", "Mini Market", "Main Market, Gulberg"],
    12: ["R.A Bazar", "PAF Market", "Girja Chowk", "Afshan Chowk", "Fortress Stadium", "Gymkhana", "Aitchison College", "PC Hotel", "Lahore Zoo", "Chairing Cross", "GPO", "Anarkali", "Civil Secretariat"],
    13: ["Bagrian", "Ghazi Chowk", "UMT Stop", "Khokhar Chowk", "Akbar Chowk", "Pindi Stop", "Peco Morr", "Phatak Mandi", "Ittefaq Hospital", "Model Town", "Kalma Chowk"],
    14: ["R.A Bazar", "Fauji Foundation", "Ali View Garden", "Bhatta Chowk", "DHA Nursery", "LESCO", "Chota Ishara Stop", "Naka Stop", "Ghazi Chowk", "Chungi Amar Sidhu"],
    15: ["Qartba Chowk", "Hakeem M. Ajmal Khan Road", "Gulshan Ravi Road", "Kacha Ferozepur Road", "Babu Sabu"],
    16: ["Railway Station", "Circular Road", "Ek Moriya", "Bhatti Chowk"],
    17: ["Canal", "Main Boulevard Shadman", "Davis Road", "Shimla Pahari", "Haji Camp", "Railway Station"],
    18: ["Bhatti Chowk", "Circular Road", "Nisbat Road", "Abbot Road", "Shimla Pahari"],
    19: ["Main Market", "Jail Road", "Lytton Road", "Crust Road", "Lower Mall Road", "Bhatti Chowk"],
    20: ["Jain Mandar", "Al-Mumtaz Road", "Poonch Road", "Lake Road", "Chowk Yateem Khana"],
    21: ["Depot Chowk", "Madar-e-Millat Road", "Ali Road", "Baig Road", "Canal Bank Road", "Thokar Niaz Baig"],
    22: ["Depot Chowk", "Madar-e-Millat Road", "Sutlej Avenue", "Shahrah Nazria-e- Pakistan Avenue", "Thokar Niaz Baig"],
    23: ["Valencia", "Valencia Main Boulevard", "Khayaban-e-Jinnah", "Raiwind Road", "Thokar Niaz Baig"],
    24: ["Multan Chungi", "College Road", "Maulana Shaukat Ali Road", "Wahdat Road", "Ghazi Chowk"],
    25: ["R.A Bazar", "Lahore-Bedian Road", "Allama Iqbal Road", "Railway Station"],
    26: ["R.A Bazar", "G.T Road", "Shalimar Link Road", "Tufail Road", "Sarfraz Rafique Road", "Daroghawala"],
    27: ["BataPur", "GT Road", "Daroghawala"],
    28: ["Quaid e Azam Interchange", "Harbanspura Road", "Zarar Shaheed Road", "Airport"],
    29: ["Niazi Interchange", "Lahore Ring Road", "Band Road", "Sue Wala Road", "Salamat Pura"],
    30: ["Daroghawala", "G.T. Road", "Shalimar Link Road", "Airport"],
    31: ["Daroghawala", "Chamra Mandi", "Cooper Store", "UET", "Shalimar Chowk", "Lari Adda"],
    32: ["Shimla Pahari", "Durand Road", "Queen Mary Road", "Garhi Shahu Bridge", "Cooper Store", "Chamra Mandi", "Ek Moriya"],
    33: ["Cooper Store", "Workshop Road", "Mughalpura Road", "Mughalpura"],
    34: ["Singhpura", "Wheatman Road", "Griffin Road", "Mughalpura"],
}


# fare_details:dict[str,int] = {
#     "fare": 25,
    
# }

# schedule:dict[str,str] = {
#     "start_time": "6 AM",
#     "end_time": "10 PM",
#     "frequency": "5 to 10 minutes"
# }

# helpline_info:dict[str,str] = {
#     "contact_number": "(042) 111-222-627"
# }
