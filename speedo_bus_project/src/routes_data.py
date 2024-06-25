routes:dict[str,dict[str,list[str]|int]] = {
    'R1': {'stops': ["Railway Station", "Ek Moriya", "Nawaz Sharif Hospital", "Kashmiri Gate", "Lari Adda", "Azadi Chowk", "Texali Chowk", "Bhatti Chowk" ],'fare': 25},
    'R2': {'stops': ["Samanabad Morr", "Corporation Chowk", "Taj Company", "Sanda", "Double Sarkan", "Moon Market", "Ganda Nala", "Bhatti Chowk" ],'fare': 25},
    'R3': {'stops': ["Railway Station", "Ek Moriya", "Nawaz Sharif Hospital", "Kashmiri Gate", "Lari Adda", "Azadi Chowk", "Timber Market", "METRO", "Niazi Chowk", "Shahdara Metro Station", "Shahdara Lari Adda" ],'fare': 25},
    'R4': {'stops': ["R.A Bazar", "Nadeem Chowk", "Defence Morr", "Shareef Market", "Walton", "Qainchi", "Ghazi Chowk", "Chungi Amar Sidhu" ],'fare': 25},
    'R5': {'stops': ["Shad Bagh Underpass", "Rajput Park", "Madina Chowk", "Lohay Wali Pulley", "Badami Bagh", "Lari Adda Gol Chakar", "Azadi Chowk", "Taxali Chowk", "Bhatti Chowk" ],'fare': 25},
    'R6': {'stops': ["Babu Sabu", "Niazi Adda", "City Bus Stand", "Chowk Yateem Khana", "Bhala Stop", "Samanabad Morr", "Chauburji", "Riwaz Garden", "M.A.O College", "Firdous Cinema", "Raj Garh Chowk" ],'fare': 25},
    'R7': {'stops': ["Bagrian", "Depot Chowk", "Minhaj University", "Hamdard Chowk", "Rehmat Eye Hospital", "Pindi Stop", "Peco Morr", "Kot Lakhpat Railway Station", "Phatak Mandi", "Qainchi", "Ghazi Chowk", "Chungi Amar Sidhu" ],'fare': 25},
    'R8': {'stops': ["Doctor Hospital", "Wafaqi Colony", "IBA Stop", "Hailey College", "Campus Pull", "Barkat Market", "Kalma Chowk", "Qaddafi Stadium", "Canal" ],'fare': 25},
    'R9': {'stops': ["Railway Station", "Haji Camp", "Shimla Pahari", "Lahore Zoo", "Chairing Cross", "Ganga Ram Hospital", "Qartaba Chowk", "Chauburji", "Sham Nagar" ],'fare': 25},
    'R10': {'stops': ["Multan Chungi", "Mustafa Town", "Karim Block Market", "PU Examination Center", "Bhekewal Morr", "Wahdat Colony", "Naqsha Stop", "Canal", "Ichra", "Shama", "Qartaba Chowk" ],'fare': 25},
    'R11': {'stops': ["Babu Sabu", "Niazi Adda", "City Bus Stand", "Chowk Yateem Khana", "Scheme Morr", "Flat Stop", "Dubai Chowk", "Bhekewal Morr", "Sheikh Zaid Hospital", "Campus Pull", "Barkat Market", "Kalma Chowk", "Liberty Chowk", "Hafeez Center", "Mini Market", "Main Market, Gulberg" ],'fare': 25},
    'R12': {'stops': ["R.A Bazar", "PAF Market", "Girja Chowk", "Afshan Chowk", "Fortress Stadium", "Gymkhana", "Aitchison College", "PC Hotel", "Lahore Zoo", "Chairing Cross", "GPO", "Anarkali", "Civil Secretariat" ],'fare': 25},
    'R13': {'stops': ["Bagrian", "Ghazi Chowk", "UMT Stop", "Khokhar Chowk", "Akbar Chowk", "Pindi Stop", "Peco Morr", "Phatak Mandi", "Ittefaq Hospital", "Model Town", "Kalma Chowk" ],'fare': 25},
    'R14': {'stops': ["R.A Bazar", "Fauji Foundation", "Ali View Garden", "Bhatta Chowk", "DHA Nursery", "LESCO", "Chota Ishara Stop", "Naka Stop", "Ghazi Chowk", "Chungi Amar Sidhu" ],'fare': 25},
    'R15': {'stops': ["Qartba Chowk", "Hakeem M. Ajmal Khan Road", "Gulshan Ravi Road", "Kacha Ferozepur Road", "Babu Sabu" ],'fare': 25},
    'R16': {'stops': ["Railway Station", "Circular Road", "Ek Moriya", "Bhatti Chowk" ],'fare': 25},
    'R17': {'stops': ["Canal", "Main Boulevard Shadman", "Davis Road", "Shimla Pahari", "Haji Camp", "Railway Station" ],'fare': 25},
    'R18': {'stops': ["Bhatti Chowk", "Circular Road", "Nisbat Road", "Abbot Road", "Shimla Pahari" ],'fare': 25},
    'R19': {'stops': ["Main Market", "Jail Road", "Lytton Road", "Crust Road", "Lower Mall Road", "Bhatti Chowk" ],'fare': 25},
    'R20': {'stops': ["Jain Mandar", "Al-Mumtaz Road", "Poonch Road", "Lake Road", "Chowk Yateem Khana" ],'fare': 25},
    'R21': {'stops': ["Depot Chowk", "Madar-e-Millat Road", "Ali Road", "Baig Road", "Canal Bank Road", "Thokar Niaz Baig" ],'fare': 25},
    'R22': {'stops': ["Depot Chowk", "Madar-e-Millat Road", "Sutlej Avenue", "Shahrah Nazria-e- Pakistan Avenue", "Thokar Niaz Baig" ],'fare': 25},
    'R23': {'stops': ["Valencia", "Valencia Main Boulevard", "Khayaban-e-Jinnah", "Raiwind Road", "Thokar Niaz Baig" ],'fare': 25},
    'R24': {'stops': ["Multan Chungi", "College Road", "Maulana Shaukat Ali Road", "Wahdat Road", "Ghazi Chowk" ],'fare': 25},
    'R25': {'stops': ["R.A Bazar", "Lahore-Bedian Road", "Allama Iqbal Road", "Railway Station" ],'fare': 25},
    'R26': {'stops': ["R.A Bazar", "G.T Road", "Shalimar Link Road", "Tufail Road", "Sarfraz Rafique Road", "Daroghawala" ],'fare': 25},
    'R27': {'stops': ["BataPur", "GT Road", "Daroghawala" ],'fare': 25},
    'R28': {'stops': ["Quaid e Azam Interchange", "Harbanspura Road", "Zarar Shaheed Road", "Airport" ],'fare': 25},
    'R29': {'stops': ["Niazi Interchange", "Lahore Ring Road", "Band Road", "Sue Wala Road", "Salamat Pura" ],'fare': 25},
    'R30': {'stops': ["Daroghawala", "G.T. Road", "Shalimar Link Road", "Airport" ],'fare': 25},
    'R31': {'stops': ["Daroghawala", "Chamra Mandi", "Cooper Store", "UET", "Shalimar Chowk", "Lari Adda" ],'fare': 25},
    'R32': {'stops': ["Shimla Pahari", "Durand Road", "Queen Mary Road", "Garhi Shahu Bridge", "Cooper Store", "Chamra Mandi", "Ek Moriya" ],'fare': 25},
    'R33': {'stops': ["Cooper Store", "Workshop Road", "Mughalpura Road", "Mughalpura" ],'fare': 25},
    'R34': {'stops': ["Singhpura", "Wheatman Road", "Griffin Road", "Mughalpura" ],'fare': 25},
}
fare_details:dict[str,int] = {
    "fare": 25,
    
}

schedule:dict[str,str] = {
    "start_time": "6 AM",
    "end_time": "10 PM",
    "frequency": "5 to 10 minutes"
}

helpline_info:dict[str,str] = {
    "contact_number": "(042) 111-222-627"
}